#!/usr/bin/python
from __future__ import annotations
from typing     import TYPE_CHECKING

from typing     import Self, Any

from PySide6 import QtWidgets, QtCore


class BaseProperty(QtWidgets.QWidget):
    """
    Base class for a custom node property widget to be displayed in the
    PropertiesBin widget.

    Inherits from: :class:`PySide6.QtWidgets.QWidget`
    """

    value_changed = QtCore.Signal(str, object)

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}() object at {hex(id(self))}>'

    def get_value(self: Self) -> Any:
        """

        Returns:
            object:
        """
        raise NotImplementedError

    def set_value(self: Self, value: Any) -> None:
        """

        Args:
            value (object):

        Returns:
            object:
        """
        raise NotImplementedError
