"""
This type stub file was generated by pyright.
"""

from typing import TypedDict
from PySide6 import QtGui
from .prop_widgets_abstract import BaseProperty

class TValidator(TypedDict):
    pattern: str
    placeholder: str
    tooltip: str
    is_case_sensitive: bool
    checkbox_visible: bool
    tool_btn_visible: bool
    ...


class PropLineEditValidatorCheckBox(BaseProperty):
    def __init__(self, parent=...) -> None:
        ...

    def set_validator(self, validator_data: TValidator): # -> None:
        ...

    def set_checkbox_label(self, label: str): # -> None:
        ...

    def set_tool_btn(self, func, icon: QtGui.QIcon = ..., tooltip: str = ...): # -> None:
        ...

    def get_value(self): # -> tuple[str, bool, str | Any, str | Any, str | Any, bool | Any, str | Any, bool | Any, bool | Any]:
        ...

    def set_value(self, value): # -> None:
        ...
