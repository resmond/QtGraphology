"""
This type stub file was generated by pyright.
"""

from typing import Literal, TYPE_CHECKING, TypedDict
from QtGraphology.qgraphics.node_base import NodeItem
from PySide6 import QtWidgets

"""
This type stub file was generated by pyright.
"""
if TYPE_CHECKING:
    ...
class TPortConstraint(TypedDict):
    port_name: str
    port_type: str
    ...


class PortItem(QtWidgets.QGraphicsItem):
    """
    Base Port Item.
    """
    def __init__(self, parent=...) -> None:
        ...

    def set_allow_partial_match_constraint(self, allow: bool):
        ...

    def get_allow_partial_match_constraint(self):
        ...

    def set_accept_constraint(self, port_name: str, port_type: Literal["in", "out"], node_identifier: str):
        ...

    def validate_accept_constraint(self, target_port: PortItem) -> bool | None:
        ...

    def set_reject_constraint(self, port_name: str, port_type: Literal["in", "out"], node_identifier: str):
        ...

    def validate_reject_constraint(self, target_port: PortItem) -> bool | None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self):
        ...

    def boundingRect(self):
        ...

    def paint(self, painter, option, widget):
        """
        Draws the circular port.

        Args:
            painter (QtGui.QPainter): painter used for drawing the item.
            option (QtGui.QStyleOptionGraphicsItem):
                used to describe the parameters needed to draw.
            widget (QtWidgets.QWidget): not used.
        """
        ...

    def itemChange(self, change, value):
        ...

    def mousePressEvent(self, event):
        ...

    def mouseReleaseEvent(self, event):
        ...

    def hoverEnterEvent(self, event):
        ...

    def hoverLeaveEvent(self, event):
        ...

    def viewer_start_connection(self):
        ...

    def redraw_connected_pipes(self):
        ...

    def add_pipe(self, pipe):
        ...

    def remove_pipe(self, pipe):
        ...

    @property
    def connected_pipes(self):
        ...

    @property
    def connected_ports(self):
        ...

    @property
    def hovered(self):
        ...

    @hovered.setter
    def hovered(self, value=...):
        ...

    @property
    def node(self) -> NodeItem:
        ...

    @property
    def name(self):
        ...

    @name.setter
    def name(self, name=...):
        ...

    @property
    def display_name(self):
        ...

    @display_name.setter
    def display_name(self, display=...):
        ...

    @property
    def color(self):
        ...

    @color.setter
    def color(self, color=...):
        ...

    @property
    def border_color(self):
        ...

    @border_color.setter
    def border_color(self, color=...):
        ...

    @property
    def border_size(self):
        ...

    @border_size.setter
    def border_size(self, size=...):
        ...

    @property
    def locked(self):
        ...

    @locked.setter
    def locked(self, value=...):
        ...

    @property
    def multi_connection(self):
        ...

    @multi_connection.setter
    def multi_connection(self, mode=...):
        ...

    @property
    def port_type(self):
        ...

    @port_type.setter
    def port_type(self, port_type):
        ...

    def connect_to(self, port):
        ...

    def disconnect_from(self, port):
        ...



class CustomPortItem(PortItem):
    """
    Custom port item for drawing custom shape port.
    """
    def __init__(self, parent=..., paint_func=...) -> None:
        ...

    def set_painter(self, func=...):
        """
        Set custom paint function for drawing.

        Args:
            func (function): paint function.
        """
        ...

    def paint(self, painter, option, widget):
        """
        Draws the port item.

        Args:
            painter (QtGui.QPainter): painter used for drawing the item.
            option (QtGui.QStyleOptionGraphicsItem):
                used to describe the parameters needed to draw.
            widget (QtWidgets.QWidget): not used.
        """
        ...
