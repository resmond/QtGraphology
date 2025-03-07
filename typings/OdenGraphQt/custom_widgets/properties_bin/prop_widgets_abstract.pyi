"""
This type stub file was generated by pyright.
"""

from PySide6 import QtWidgets

class BaseProperty(QtWidgets.QWidget):
    """
    Base class for a custom node property widget to be displayed in the
    PropertiesBin widget.

    Inherits from: :class:`PySide6.QtWidgets.QWidget`
    """
    value_changed = ...
    def __repr__(self): # -> str:
        ...

    def get_value(self):
        """

        Returns:
            object:
        """
        ...

    def set_value(self, value):
        """

        Args:
            value (object):

        Returns:
            object:
        """
        ...
