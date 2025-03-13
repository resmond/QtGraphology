#!/usr/bin/python
from __future__ import annotations
from typing     import Self, Any

from PySide6 import QtWidgets, QtCore

from QtGraphology.widgets.dialogs import FileDialog
from .prop_widgets_abstract import BaseProperty


class PropFilePath(BaseProperty):
    """
    Displays a node property as a "QFileDialog" open widget in the
    PropertiesBin.
    """

    def __init__(self: Self, parent: QtWidgets.QWidget | None = None):
        super(PropFilePath, self).__init__(parent)
        self._ledit = QtWidgets.QLineEdit()
        self._ledit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self._ledit.editingFinished.connect(self._on_value_change)
        self._ledit.clearFocus()

        icon = self.style().standardIcon(QtWidgets.QStyle.StandardPixmap(21))
        _button = QtWidgets.QPushButton()
        _button.setIcon(icon)
        _button.clicked.connect(self._on_select_file)

        hbox = QtWidgets.QHBoxLayout(self)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self._ledit)
        hbox.addWidget(_button)

        self._ext = '*'
        self._file_directory = None

    def _on_select_file(self: Self) -> None:
        file_path = FileDialog.getOpenFileName(self,
                                               file_dir=self._file_directory,
                                               ext_filter=self._ext)
        file = file_path[0] or None
        if file:
            self.set_value(file)

    def _on_value_change(self: Self, value: Any = None) -> None:
        if value is None:
            value = self._ledit.text()
        self.set_file_directory(value)
        self.value_changed.emit(self.toolTip(), value)

    def set_file_ext(self, ext: str | None = None) -> None:
        self._ext = ext or '*'

    def set_file_directory(self, directory: str | None) -> None:
        self._file_directory = directory

    def get_value(self) -> str:
        return self._ledit.text()

    def set_value(self, value: Any) -> None:
        _value = str(value)
        if _value != self.get_value():
            self._ledit.setText(_value)
            self._on_value_change(_value)


class PropFileSavePath(PropFilePath):
    """
    Displays a node property as a "QFileDialog" save widget in the
    PropertiesBin.
    """

    def _on_select_file(self: Self) -> None:
        file_path = FileDialog.getSaveFileName(self,
                                               file_dir=self._file_directory,
                                               ext_filter=self._ext)
        file = file_path[0] or None
        if file:
            self.set_value(file)
