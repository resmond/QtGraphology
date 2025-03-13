#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

from typing     import Self, Any, Callable
from collections.abc import Callable

from PySide6 import QtWidgets, QtCore, QtGui

from .prop_widgets_abstract import BaseProperty


class PropSlider(BaseProperty):
    """
    Displays a node property as a "Slider" widget in the PropertiesBin
    widget.
    """

    def __init__(self, parent: QtWidgets.QWidget | None, disable_scroll: bool = True, realtime_update: bool = False) -> None:
        super(PropSlider, self).__init__(parent)
        self._block: bool = False
        self._realtime_update: bool = realtime_update
        self._disable_scroll: bool = disable_scroll
        self._slider: QtWidgets.QSlider = QtWidgets.QSlider()
        self._spinbox: QtWidgets.QSpinBox = QtWidgets.QSpinBox()
        self._init()
        self._init_signal_connections()

    def _init(self: Self) -> None:
        self._slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self._slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow) # type: ignore
        self._slider.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                   QtWidgets.QSizePolicy.Policy.Preferred)
        self._spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._spinbox)
        layout.addWidget(self._slider)
        # store the original press event.
        self._slider_mouse_press_event: Callable[[QtGui.QMouseEvent], None] = self._slider.mousePressEvent
        self._slider.mousePressEvent = self._on_slider_mouse_press
        self._slider.mouseReleaseEvent = self._on_slider_mouse_release

        if self._disable_scroll:
            self._slider.wheelEvent = lambda _: None
            self._spinbox.wheelEvent = lambda _: None

    def _init_signal_connections(self: Self) -> None:
        self._spinbox.valueChanged.connect(self._on_spnbox_changed)
        self._slider.valueChanged.connect(self._on_slider_changed)

    def _on_slider_mouse_press(self: Self, event: QtGui.QMouseEvent) -> None:
        self._block = True
        self._slider_mouse_press_event(event)

    def _on_slider_mouse_release(self: Self, event: QtGui.QMouseEvent) -> None:
        if not self._realtime_update:
            self.value_changed.emit(self.toolTip(), self.get_value())
        self._block = False

    def _on_slider_changed(self: Self, value: int) -> None:
        self._spinbox.setValue(value)
        if self._realtime_update:
            self.value_changed.emit(self.toolTip(), self.get_value())

    def _on_spnbox_changed(self: Self, value: int) -> None:
        if value != self._slider.value():
            self._slider.setValue(value)
            if not self._block:
                self.value_changed.emit(self.toolTip(), self.get_value())

    def get_value(self: Self) -> int:
        return self._spinbox.value()

    def set_value(self: Self, value: int) -> None:
        if value != self.get_value():
            self._block = True
            self._spinbox.setValue(value)
            self.value_changed.emit(self.toolTip(), value)
            self._block = False

    def set_min(self: Self, value: int = 0) -> None:
        self._spinbox.setMinimum(value)
        self._slider.setMinimum(value)

    def set_max(self: Self, value: int = 0) -> None:
        self._spinbox.setMaximum(value)
        self._slider.setMaximum(value)


class QDoubleSlider(QtWidgets.QSlider):
    double_value_changed = QtCore.Signal(float)

    def __init__(self: Self, decimals: int =2, *args, **kargs: dict[str, Any]) -> None:
        super(QDoubleSlider, self).__init__(*args, **kargs)
        self._multiplier = 10 ** decimals

        self.valueChanged.connect(self._on_value_change)

    def _on_value_change(self: Self, value: int) -> None:
        value = float(super(QDoubleSlider, self).value()) / self._multiplier
        self.double_value_changed.emit(value)

    def value(self: Self) -> int:
        return float(super(QDoubleSlider, self).value()) / self._multiplier

    def setMinimum(self: Self, value: int) -> None:
        return super(QDoubleSlider, self).setMinimum(value * self._multiplier)

    def setMaximum(self: Self, value: int) -> None:
        return super(QDoubleSlider, self).setMaximum(value * self._multiplier)

    def setSingleStep(self: Self, value: int) -> None:
        return super(QDoubleSlider, self).setSingleStep(value * self._multiplier)

    def singleStep(self: Self) -> int:
        return float(super(QDoubleSlider, self).singleStep()) / self._multiplier

    def setValue(self: Self, value: float) -> None:
        super(QDoubleSlider, self).setValue(int(value * self._multiplier))


class PropDoubleSlider(PropSlider):
    def __init__(self: Self, parent: QtWidgets.QWidget | None=None, decimals: int = 2, disable_scroll: bool = True, realtime_update: bool = False) -> None:
        # Do not initialize Propslider, just its parents
        super(PropDoubleSlider, self).__init__(parent)
        self._block: bool = False
        self._realtime_update: bool = realtime_update
        self._disable_scroll: bool = disable_scroll
        self._slider = QDoubleSlider(decimals=decimals)
        self._spinbox = QtWidgets.QDoubleSpinBox() # type: ignore
        self._init()
        self._init_signal_connections()

    def _init_signal_connections(self):
        self._spinbox.valueChanged.connect(self._on_spnbox_changed)
        # Connect to double_value_changed instead valueChanged
        self._slider.double_value_changed.connect(self._on_slider_changed) # type: ignore
