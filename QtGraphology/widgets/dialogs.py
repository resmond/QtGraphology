from __future__ import annotations
from typing import TYPE_CHECKING

import os

from PySide6 import QtWidgets
from QtGraphology.widgets.viewer import NodeViewer

_current_user_directory = os.path.expanduser('~')


def set_dir(file: str) -> None:
    global _current_user_directory
    if os.path.isdir(file):
        _current_user_directory = file
    elif os.path.isfile(file):
        _current_user_directory = os.path.split(file)[0]

class FileDialog(object):

    @staticmethod
    def getSaveFileName(parent: NodeViewer | None=None, title: str = 'Save File', file_dir: str | None = None, ext_filter: str = '*'):
        if not file_dir:
            file_dir = _current_user_directory
        file_dlg = QtWidgets.QFileDialog.getSaveFileName(
            parent, title, file_dir, ext_filter)
        file = file_dlg[0] or None
        if file:
            set_dir(file)
        return file_dlg

    @staticmethod
    def getOpenFileName(parent: NodeViewer | None=None, title: str = 'Open File', file_dir: str | None = None, ext_filter: str = '*'):
        if not file_dir:
            file_dir = _current_user_directory
        file_dlg: tuple[str, str] = QtWidgets.QFileDialog.getOpenFileName(parent, title, file_dir, ext_filter)
        file: str | None = file_dlg[0] or None
        if file:
            set_dir(file)
        return file_dlg


class BaseDialog(object):

    @staticmethod
    def message_dialog(text: str = '', title: str = 'Message'):
        dlg: QtWidgets.QMessageBox = QtWidgets.QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setInformativeText(text)
        dlg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        dlg.exec_()

    @staticmethod
    def question_dialog(text: str = '', title: str = 'Are you sure?'):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowTitle(title)
        dlg.setInformativeText(text)
        dlg.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        result = dlg.exec_()
        return bool(result == QtWidgets.QMessageBox.StandardButton.Yes)
