#!/usr/bin/python
from __future__ import annotations
from typing     import Self, Any

from PySide6 import QtWidgets, QtCore, QtGui

"""
    A custom QMenu implementation for selecting numerical step values.

    This menu displays a list of numerical step values that can be selected
    by the user. It tracks mouse movement over menu items and emits signals
    when the step value changes or when the mouse is released.

    Signals:
        mouseMove (object): Emitted when the mouse moves over the menu.
        mouseRelease (object): Emitted when the mouse is released.
        stepChange: Emitted when the selected step value changes.

    Attributes:
        step (int, float): The current selected step value.
        steps (list): List of available step values.
        last_action (QAction): Reference to the last hovered menu action.

    Example:
        menu = _NumberValueMenu()
        menu.set_steps([0.1, 0.5, 1.0, 5.0, 10.0])
        menu.mouseMove.connect(my_mouse_move_handler)
        menu.stepChange.connect(my_step_change_handler)

"""
class _NumberValueMenu(QtWidgets.QMenu):

    mouseMove = QtCore.Signal(object)
    mouseRelease = QtCore.Signal(object)
    stepChange = QtCore.Signal()

    def __init__(self: Self, parent=None):
        super().__init__(parent)
        self.step = 1
        self.steps = []
        self.last_action = None

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def mousePressEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        """
        Disabling the mouse press event.
        """
        return

    def mouseReleaseEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        """
        Additional functionality to emit signal.
        """
        self.mouseRelease.emit(event)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        """
        Handle mouse move events to track actions and emit appropriate signals.

        This overrides the parent's mouseMoveEvent to add functionality for tracking
        actions under the mouse cursor and emitting signals when the step changes.

        Args:
            event: The mouse move event containing position information

        Emits:
            mouseMove: Signal emitted with the event object
            stepChange: Signal emitted when the mouse moves to a different action

        Additional functionality to emit step changed signal.
        """
        self.mouseMove.emit(event)
        super().mouseMoveEvent(event)
        action: QtGui.QAction = self.actionAt(event.pos())
        if action:
            if action is not self.last_action:
                self.stepChange.emit()
            self.last_action = action
            self.step = action.step  # type: ignore
        elif self.last_action:
            self.setActiveAction(self.last_action)

    def _add_step_action(self: Self, step: float) -> None:
        action = QtGui.QAction(str(step), self)
        action.step = step   # type: ignore
        self.addAction(action)

    def set_steps(self, steps: list[float]) -> None:
        self.clear()
        self.steps = steps
        for step in steps:
            self._add_step_action(step)

    def set_data_type(self: Self, data_type: type) -> None:
        if data_type is int:
            new_steps = []
            for step in self.steps:
                if '.' not in str(step):
                    new_steps.append(step)
            self.set_steps(new_steps)
        elif data_type is float:
            self.set_steps(self.steps)

class _NumberValueEdit(QtWidgets.QLineEdit):

    value_changed = QtCore.Signal(str, object)

    def __init__(self: Self, parent=None, data_type=float) -> None:
        super().__init__(parent)
        self._tooltip = '"MMB + Drag Left/Right" to change values.'
        self.setText('0')

        self._MMB_STATE = False
        self._previous_x = None
        self._previous_value = None
        self._step = 1
        self._speed = 0.1
        self._data_type = float

        self._menu = _NumberValueMenu()
        self._menu.mouseMove.connect(self.mouseMoveEvent)
        self._menu.mouseRelease.connect(self.mouseReleaseEvent)
        self._menu.stepChange.connect(self._reset_previous_x)
        self._menu.set_steps([0.001, 0.01, 0.1, 1, 10, 100, 1000])

        self.editingFinished.connect(self._on_text_changed)

        self.set_data_type(data_type)

    def __repr__(self: Self) -> str:
        return '<{}() object at {}>'.format(
            self.__class__.__name__, hex(id(self))
        )

    def event(self: Self, event: QtCore.QEvent) -> bool:
        """
        Handle widget events, specifically customizing tooltip behavior.

        Overrides the standard event handling to provide custom tooltip display
        with the content from self._tooltip when a tooltip event occurs.

        Args:
            event (QtCore.QEvent): The event to be processed

        Returns:
            bool: True if the event was handled, otherwise the result of the parent's event handling
        """
        if event.type() == QtCore.QEvent.Type.ToolTip:
            QtWidgets.QToolTip.hideText()
            QtWidgets.QToolTip.showText(
                QtGui.QCursor.pos(),
                self._tooltip,
                msecShowTime=3500,
            )
            return True

        return super().event(event)

    def mouseMoveEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        if self._MMB_STATE:
            if self._previous_x is None:
                self._previous_x = event.x()
                self._previous_value = self.get_value()
            else:
                self._step = self._menu.step
                delta = event.x() - self._previous_x
                value = self._previous_value or 0
                value = value + int(delta * self._speed) * self._step
                self.set_value(value)
                self._on_text_changed()
        super().mouseMoveEvent(event)

    def mousePressEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.MiddleButton:
            self._MMB_STATE = True
            self._reset_previous_x()
            self._menu.exec_(QtGui.QCursor.pos())
        super().mousePressEvent(event)

    def mouseReleaseEvent(self: Self, event: QtGui.QMouseEvent) -> None:
        self._menu.close()
        self._MMB_STATE = False
        super().mouseReleaseEvent(event)

    def keyPressEvent(self: Self, event: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key.Key_Up:
            return
        elif event.key() == QtCore.Qt.Key.Key_Down:
            return

    # private

    def _reset_previous_x(self: Self) -> None:
        self._previous_x = None

    def _on_text_changed(self: Self) -> None:
        self.value_changed.emit(self.toolTip(), self.get_value())

    def _convert_text(self, text: str) -> float | int:
        # int("1.0") will return error
        # so we use int(float("1.0"))
        # FIXME: Better to raise exception and handle the
        #  data type casting in subclasses reimplementation
        try:
            value = float(text)
        except ValueError:
            value = 0.0

        if self._data_type is int:
            value = int(value)

        return value

    # public

    def set_data_type(self: Self, data_type: type) -> None:
        self._data_type = data_type
        self._menu.set_data_type(data_type)
        self.setValidator(
            QtGui.QIntValidator() if data_type is int
            else QtGui.QDoubleValidator()
        )

    def set_steps(self: Self, steps: list[float] = []) -> None:
        steps = steps or [0.001, 0.01, 0.1, 1, 10, 100, 1000]
        self._menu.set_steps(steps)

    def get_value(self: Self) -> float:
        if self.text().startswith('.'):
            text = '0' + self.text()
            self.setText(text)
        return self._convert_text(self.text())

    def set_value(self: Self, value: float) -> None:
        if value != self.get_value():
#            foo: Any = self._convert_text(value)
            self.setText(f'{value}')


class IntValueEdit(_NumberValueEdit):

    def __init__(self: Self, parent=None) -> None:
        super().__init__(parent, data_type=int)


class FloatValueEdit(_NumberValueEdit):

    def __init__(self: Self, parent=None) -> None:
        super().__init__(parent, data_type=float)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    int_edit = IntValueEdit()
    int_edit.set_steps([1, 10])
    float_edit = FloatValueEdit()

    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(widget)
    layout.addWidget(int_edit)
    layout.addWidget(float_edit)
    widget.show()

    app.exec_()
