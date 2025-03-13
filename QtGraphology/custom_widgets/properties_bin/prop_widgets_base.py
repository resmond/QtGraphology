#!/usr/bin/python
from __future__ import annotations
from typing     import TYPE_CHECKING

from typing     import Self, Any

from QtGraphology.custom_widgets import CustomCheckBox
from PySide6 import QtWidgets, QtCore, QtGui

class PropLabel(QtWidgets.QLabel):
    """
    Displays a node property as a "QLabel" widget in the PropertiesBin widget.
    """

    value_changed: QtCore.Signal = QtCore.Signal(str, object)

    def __repr__(self: Self):
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def get_value(self: Self):
        return self.text()

    def set_value(self: Self, value: Any):
        if value != self.get_value():
            self.setText(str(value))
            self.value_changed.emit(self.toolTip(), value)


class PropLineEdit(QtWidgets.QLineEdit):
    """
    Displays a node property as a "QLineEdit" widget in the PropertiesBin
    widget.
    """

    value_changed: QtCore.Signal = QtCore.Signal(str, object)

    def __init__(self: Self, parent:QtWidgets.QWidget | None=None):
        super(PropLineEdit, self).__init__(parent)
        self.editingFinished.connect(self._on_editing_finished)

    def __repr__(self: Self):
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def _on_editing_finished(self: Self):
        self.value_changed.emit(self.toolTip(), self.text())

    def get_value(self: Self):
        return self.text()

    def set_value(self: Self, value: Any):
        _value = str(value)
        if _value != self.get_value():
            self.setText(_value)
            self.value_changed.emit(self.toolTip(), _value)


class PropTextEdit(QtWidgets.QTextEdit):
    """
    Displays a node property as a "QTextEdit" widget in the PropertiesBin
    widget.
    """

    value_changed: QtCore.Signal = QtCore.Signal(str, object)

    def __init__(self: Self, parent: QtWidgets.QWidget | None = None):
        super(PropTextEdit, self).__init__(parent)
        self._prev_text = ''

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def focusInEvent(self: Self, event: QtGui.QFocusEvent) -> None:
        super(PropTextEdit, self).focusInEvent(event)
        self._prev_text = self.toPlainText()

    def focusOutEvent(self: Self, event: QtGui.QFocusEvent) -> None:
        super(PropTextEdit, self).focusOutEvent(event)
        if self._prev_text != self.toPlainText():
            self.value_changed.emit(self.toolTip(), self.toPlainText())
        self._prev_text = ''

    def get_value(self: Self) -> str:
        return self.toPlainText()

    def set_value(self: Self, value: Any):
        _value = str(value)
        if _value != self.get_value():
            self.setPlainText(_value)
            self.value_changed.emit(self.toolTip(), _value)


class PropComboBox(QtWidgets.QComboBox):
    """
    Displays a node property as a "QComboBox" widget in the PropertiesBin
    widget.
    """

    value_changed = QtCore.Signal(str, object)

    def __init__(self: Self, parent: QtWidgets.QWidget | None = None):
        super(PropComboBox, self).__init__(parent)
        self.currentIndexChanged.connect(self._on_index_changed)

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def _on_index_changed(self: Self) -> None:
        self.value_changed.emit(self.toolTip(), self.get_value())

    def items(self: Self) -> list[str]:
        """
        Returns items from the combobox.

        Returns:
            list[str]: list of strings.
        """
        return [self.itemText(i) for i in range(self.count())]

    def set_items(self: Self, items):
        """
        Set items on the combobox.

        Args:
            items (list[str]): list of strings.
        """
        self.clear()
        self.addItems(items)

    def get_value(self: Self) -> str:
        return self.currentText()

    def set_value(self: Self, value: Any):
        if value != self.get_value():
            idx = self.findText(value, QtCore.Qt.MatchFlag.MatchExactly)
            self.setCurrentIndex(idx)
            if idx >= 0:
                self.value_changed.emit(self.toolTip(), value)


class PropCheckBox(CustomCheckBox):
    """
    Displays a node property as a "QCheckBox" widget in the PropertiesBin
    widget.
    """

    value_changed = QtCore.Signal(str, object)

    def __init__(self: Self, parent=None):
        super(PropCheckBox, self).__init__(parent)
        self.clicked.connect(self._on_clicked)

    def __repr__(self: Self) -> str:
        return '<{}() object at {}>'.format(
            self.__class__.__name__, hex(id(self)))

    def _on_clicked(self: Self) -> None:
        self.value_changed.emit(self.toolTip(), self.get_value())

    def get_value(self: Self) -> bool:
        return self.isChecked()

    def set_value(self: Self, value: Any):
        _value = bool(value)
        if _value != self.get_value():
            self.setChecked(_value)
            self.value_changed.emit(self.toolTip(), _value)


class PropSpinBox(QtWidgets.QSpinBox):
    """
    Displays a node property as a "QSpinBox" widget in the PropertiesBin widget.
    """

    value_changed = QtCore.Signal(str, object)

    def __init__(self: Self, parent: QtWidgets.QWidget | None = None) -> None:
        super(PropSpinBox, self).__init__(parent)
        self.setButtonSymbols(self.ButtonSymbols.NoButtons)
        self.valueChanged.connect(self._on_value_change)

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def _on_value_change(self: Self, value: int) -> None:
        self.value_changed.emit(self.toolTip(), value)

    def get_value(self: Self) -> int:
        return self.value()

    def set_value(self: Self, value: Any) -> None:
        if value != self.get_value():
            self.setValue(value)

class PropDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    """
    Displays a node property as a "QDoubleSpinBox" widget in the PropertiesBin
    widget.
    """

    value_changed = QtCore.Signal(str, object)

    def __init__(self: Self, parent: QtWidgets.QWidget | None = None) -> None:
        super(PropDoubleSpinBox, self).__init__(parent)
        self.setButtonSymbols(self.ButtonSymbols.NoButtons)
        self.valueChanged.connect(self._on_value_change)

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def _on_value_change(self: Self, value: float) -> None:
        self.value_changed.emit(self.toolTip(), value)

    def get_value(self: Self) -> float:
        return self.value()

    def set_value(self: Self, value: Any) -> None:
        if value != self.get_value():
            self.setValue(value)


# class PropPushButton(QtWidgets.QPushButton):
#     """
#     Displays a node property as a "QPushButton" widget in the PropertiesBin
#     widget.
#     """
#
#     value_changed = QtCore.Signal(str, object)
#     button_clicked = QtCore.Signal(str, object)
#
#     def __init__(self, parent=None):
#         super(PropPushButton, self).__init__(parent)
#         self.clicked.connect(self.button_clicked.emit)
#
#     def set_on_click_func(self, func, node):
#         """
#         Sets slot function for the PropPushButton widget.
#
#         Args:
#             func (function): property slot function.
#             node (QtGraphology.NodeObject): node object.
#         """
#         if not callable(func):
#             raise TypeError('var func is not a function.')
#         self.clicked.connect(lambda: func(node))
#
#     def get_value(self):
#         return
#
#     def set_value(self, value):
#         return
