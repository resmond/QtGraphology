"""
This type stub file was generated by pyright.
"""

from enum import Enum

"""
This type stub file was generated by pyright.
"""
__doc__ = ...
MIME_TYPE = ...
URI_SCHEME = ...
URN_SCHEME = ...
BASE_PATH = ...
ICON_PATH = ...
ICON_DOWN_ARROW = ...
ICON_NODE_BASE = ...
Z_VAL_BACKDROP = ...
Z_VAL_PIPE = ...
Z_VAL_NODE = ...
Z_VAL_PORT = ...
Z_VAL_NODE_WIDGET = ...
ITEM_CACHE_MODE = ...
class VersionEnum(Enum):
    """
    Current framework version.
    :py:mod:`QtGraphology.constants.VersionEnum`
    """
    VERSION = ...
    MAJOR = ...
    MINOR = ...
    PATCH = ...


class LayoutDirectionEnum(Enum):
    """
    Node graph nodes layout direction:
    :py:mod:`QtGraphology.constants.ViewerLayoutEnum`
    """
    HORIZONTAL = ...
    VERTICAL = ...


class ViewerEnum(Enum):
    """
    Node graph viewer styling layout:
    :py:mod:`QtGraphology.constants.ViewerEnum`
    """
    BACKGROUND_COLOR = ...
    GRID_DISPLAY_NONE = ...
    GRID_DISPLAY_DOTS = ...
    GRID_DISPLAY_LINES = ...
    GRID_SIZE = ...
    GRID_COLOR = ...


class ViewerNavEnum(Enum):
    """
    Node graph viewer navigation styling layout:
    :py:mod:`QtGraphology.constants.ViewerNavEnum`
    """
    BACKGROUND_COLOR = ...
    ITEM_COLOR = ...


class NodeEnum(Enum):
    """
    Node styling layout:
    :py:mod:`QtGraphology.constants.NodeEnum`
    """
    WIDTH = ...
    HEIGHT = ...
    ICON_SIZE = ...
    SELECTED_COLOR = ...
    SELECTED_BORDER_COLOR = ...


class PortEnum(Enum):
    """
    Port styling layout:
    :py:mod:`QtGraphology.constants.PortEnum`
    """
    SIZE = ...
    COLOR = ...
    BORDER_COLOR = ...
    ACTIVE_COLOR = ...
    ACTIVE_BORDER_COLOR = ...
    HOVER_COLOR = ...
    HOVER_BORDER_COLOR = ...
    CLICK_FALLOFF = ...


class PortTypeEnum(Enum):
    """
    Port connection types:
    :py:mod:`QtGraphology.constants.PortTypeEnum`
    """
    IN = ...
    OUT = ...


class PipeEnum(Enum):
    """
    Pipe styling layout:
    :py:mod:`QtGraphology.constants.PipeEnum`
    """
    WIDTH = ...
    COLOR = ...
    DISABLED_COLOR = ...
    ACTIVE_COLOR = ...
    HIGHLIGHT_COLOR = ...
    DRAW_TYPE_DEFAULT = ...
    DRAW_TYPE_DASHED = ...
    DRAW_TYPE_DOTTED = ...


class PipeSlicerEnum(Enum):
    """
    Slicer Pipe styling layout:
    :py:mod:`QtGraphology.constants.PipeSlicerEnum`
    """
    WIDTH = ...
    COLOR = ...


class PipeLayoutEnum(Enum):
    """
    Pipe connection drawing layout:
    :py:mod:`QtGraphology.constants.PipeLayoutEnum`
    """
    STRAIGHT = ...
    CURVED = ...
    ANGLE = ...


class NodePropWidgetEnum(Enum):
    """
    Mapping used for the :class:`QtGraphology.PropertiesBinWidget` to display a
    node property in the specified widget type.

    :py:mod:`QtGraphology.constants.NodePropWidgetEnum`
    """
    HIDDEN = ...
    QLABEL = ...
    QLINE_EDIT = ...
    QTEXT_EDIT = ...
    QCOMBO_BOX = ...
    QCHECK_BOX = ...
    QSPIN_BOX = ...
    QDOUBLESPIN_BOX = ...
    COLOR_PICKER = ...
    COLOR4_PICKER = ...
    SLIDER = ...
    DOUBLE_SLIDER = ...
    FILE_OPEN = ...
    FILE_SAVE = ...
    VECTOR2 = ...
    VECTOR3 = ...
    VECTOR4 = ...
    FLOAT = ...
    INT = ...
    BUTTON = ...
    LINEEDIT_VALIDATOR_CHECKBOX = ...
