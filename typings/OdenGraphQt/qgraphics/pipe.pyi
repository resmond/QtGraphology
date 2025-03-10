"""
This type stub file was generated by pyright.
"""

from PySide6 import QtWidgets

PIPE_STYLES = ...
class PipeItem(QtWidgets.QGraphicsPathItem):
    """
    Base Pipe item used for drawing node connections.
    """
    def __init__(self, input_port=..., output_port=...) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    def hoverEnterEvent(self, event): # -> None:
        ...

    def hoverLeaveEvent(self, event): # -> None:
        ...

    def itemChange(self, change, value): # -> Any:
        ...

    def paint(self, painter, option, widget): # -> None:
        """
        Draws the connection line between nodes.

        Args:
            painter (QtGui.QPainter): painter used for drawing the item.
            option (QtGui.QStyleOptionGraphicsItem):
                used to describe the parameters needed to draw.
            widget (QtWidgets.QWidget): not used.
        """
        ...

    def draw_path(self, start_port, end_port=..., cursor_pos=...): # -> None:
        """
        Draws the path between ports.

        Args:
            start_port (PortItem): port used to draw the starting point.
            end_port (PortItem): port used to draw the end point.
            cursor_pos (QtCore.QPointF): cursor position if specified this
                will be the draw end point.
        """
        ...

    def reset_path(self): # -> None:
        """
        reset the pipe initial path position.
        """
        ...

    def port_from_pos(self, pos, reverse=...): # -> PortItem | None:
        """
        Args:
            pos (QtCore.QPointF): current scene position.
            reverse (bool): false to return the nearest port.

        Returns:
            PortItem: port item.
        """
        ...

    def viewer(self): # -> None:
        """
        Returns:
            NodeViewer: node graph viewer.
        """
        ...

    def viewer_pipe_layout(self): # -> None:
        """
        Returns:
            int: pipe layout mode.
        """
        ...

    def viewer_layout_direction(self): # -> None:
        """
        Returns:
            int: graph layout mode.
        """
        ...

    def set_pipe_styling(self, color, width=..., style=...): # -> None:
        """
        Args:
            color (list or tuple): (r, g, b, a) values 0-255
            width (int): pipe width.
            style (int): pipe style.
        """
        ...

    def activate(self): # -> None:
        ...

    def active(self): # -> bool:
        ...

    def highlight(self): # -> None:
        ...

    def highlighted(self): # -> bool:
        ...

    def reset(self): # -> None:
        """
        reset the pipe state and styling.
        """
        ...

    def set_connections(self, port1, port2): # -> None:
        """
        Args:
            port1 (PortItem): port item object.
            port2 (PortItem): port item object.
        """
        ...

    def disabled(self): # -> bool:
        """
        Returns:
            bool: true if pipe is a disabled connection.
        """
        ...

    @property
    def input_port(self): # -> PortItem | None:
        ...

    @input_port.setter
    def input_port(self, port): # -> None:
        ...

    @property
    def output_port(self): # -> PortItem | None:
        ...

    @output_port.setter
    def output_port(self, port): # -> None:
        ...

    @property
    def color(self): # -> tuple[Literal[175], Literal[95], Literal[30], Literal[255]]:
        ...

    @color.setter
    def color(self, color): # -> None:
        ...

    @property
    def style(self): # -> int:
        ...

    @style.setter
    def style(self, style): # -> None:
        ...

    def delete(self): # -> None:
        ...



class LivePipeItem(PipeItem):
    """
    Live Pipe item used for drawing the live connection with the cursor.
    """
    def __init__(self) -> None:
        ...

    def hoverEnterEvent(self, event): # -> None:
        """
        re-implemented back to the base default behaviour or the pipe will
        lose it styling when another pipe is selected.
        """
        ...

    def draw_path(self, start_port, end_port=..., cursor_pos=..., color=...): # -> None:
        """
        re-implemented to also update the index pointer arrow position.

        Args:
            start_port (PortItem): port used to draw the starting point.
            end_port (PortItem): port used to draw the end point.
            cursor_pos (QtCore.QPointF): cursor position if specified this
                will be the draw end point.
            color (list[int]): override arrow index pointer color. (r, g, b)
        """
        ...

    def draw_index_pointer(self, start_port, cursor_pos, color=...): # -> None:
        """
        Update the index pointer arrow position and direction when the
        live pipe path is redrawn.

        Args:
            start_port (PortItem): start port item.
            cursor_pos (QtCore.QPoint): cursor scene position.
            color (list[int]): override arrow index pointer color. (r, g, b).
        """
        ...



class LivePipePolygonItem(QtWidgets.QGraphicsPolygonItem):
    """
    Custom live pipe polygon shape.
    """
    def __init__(self, parent) -> None:
        ...

    def paint(self, painter, option, widget): # -> None:
        """
        Args:
            painter (QtGui.QPainter): painter used for drawing the item.
            option (QtGui.QStyleOptionGraphicsItem):
                used to describe the parameters needed to draw.
            widget (QtWidgets.QWidget): not used.
        """
        ...
