"""
This type stub file was generated by pyright.
"""

from PySide6 import QtWidgets
from .prop_widgets_abstract import BaseProperty

class PropSlider(BaseProperty):
    """
    Displays a node property as a "Slider" widget in the PropertiesBin
    widget.
    """
    def __init__(self, parent=..., disable_scroll=..., realtime_update=...) -> None:
        ...

    def get_value(self): # -> int:
        ...

    def set_value(self, value): # -> None:
        ...

    def set_min(self, value=...): # -> None:
        ...

    def set_max(self, value=...): # -> None:
        ...



class QDoubleSlider(QtWidgets.QSlider):
    double_value_changed = ...
    def __init__(self, decimals=..., *args, **kargs) -> None:
        ...

    def value(self): # -> Any:
        ...

    def setMinimum(self, value): # -> None:
        ...

    def setMaximum(self, value): # -> None:
        ...

    def setSingleStep(self, value): # -> None:
        ...

    def singleStep(self): # -> Any:
        ...

    def setValue(self, value): # -> None:
        ...



class PropDoubleSlider(PropSlider):
    def __init__(self, parent=..., decimals=..., disable_scroll=..., realtime_update=...) -> None:
        ...
