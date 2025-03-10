"""
This type stub file was generated by pyright.
"""

from typing import Literal
from PySide6 import QtWidgets
from QtGraphology.qgraphics.port import PortItem

ZOOM_MIN = ...
ZOOM_MAX = ...
class NodeViewer(QtWidgets.QGraphicsView):
    """
    The widget interface used for displaying the scene and nodes.

    functions in this class should mainly be called by the
    class:`QtGraphology.NodeGraph` class.
    """
    moved_nodes = ...
    search_triggered = ...
    connection_sliced = ...
    connection_changed = ...
    insert_node = ...
    node_name_changed = ...
    node_backdrop_updated = ...
    node_selected = ...
    node_selection_changed = ...
    node_double_clicked = ...
    data_dropped = ...
    context_menu_prompt = ...
    def __init__(self, parent=..., undo_stack=...) -> None:
        """
        Args:
            parent:
            undo_stack (QtGui.QUndoStack): undo stack from the parent
                                               graph controller.
        """
        ...

    def __repr__(self): # -> str:
        ...

    def focusInEvent(self, event): # -> None:
        """
        Args:
            event (QtGui.QFocusEvent): focus event.
        """
        ...

    def focusOutEvent(self, event): # -> None:
        """
        Args:
            event (QtGui.QFocusEvent): focus event.
        """
        ...

    def scale(self, sx, sy, pos=...): # -> None:
        ...

    def drawForeground(self, painter, rect): # -> None:
        ...

    def resizeEvent(self, event): # -> None:
        ...

    def contextMenuEvent(self, event): # -> None:
        ...

    def mousePressEvent(self, event):
        ...

    def mouseReleaseEvent(self, event): # -> None:
        ...

    def mouseMoveEvent(self, event):
        ...

    def wheelEvent(self, event): # -> None:
        ...

    def dropEvent(self, event): # -> None:
        ...

    def dragEnterEvent(self, event): # -> None:
        ...

    def dragMoveEvent(self, event): # -> None:
        ...

    def dragLeaveEvent(self, event): # -> None:
        ...

    def keyPressEvent(self, event): # -> None:
        """
        Key press event re-implemented to update the states for attributes:
        - ALT_state
        - CTRL_state
        - SHIFT_state

        Args:
            event (QtGui.QKeyEvent): key event.
        """
        ...

    def keyReleaseEvent(self, event): # -> None:
        """
        Key release event re-implemented to update the states for attributes:
        - ALT_state
        - CTRL_state
        - SHIFT_state

        Args:
            event (QtGui.QKeyEvent): key event.
        """
        ...

    def sceneMouseMoveEvent(self, event): # -> None:
        """
        triggered mouse move event for the scene.
         - redraw the live connection pipe.

        Args:
            event (QtWidgets.QGraphicsSceneMouseEvent):
                The event handler from the QtWidgets.QGraphicsScene
        """
        ...

    def sceneMousePressEvent(self, event): # -> None:
        """
        triggered mouse press event for the scene (takes priority over viewer event).
         - detect selected pipe and start connection.
         - remap Shift and Ctrl modifier.

        Args:
            event (QtWidgets.QGraphicsScenePressEvent):
                The event handler from the QtWidgets.QGraphicsScene
        """
        ...

    def sceneMouseReleaseEvent(self, event): # -> None:
        """
        triggered mouse release event for the scene.

        Args:
            event (QtWidgets.QGraphicsSceneMouseEvent):
                The event handler from the QtWidgets.QGraphicsScene
        """
        ...

    def apply_live_connection(self, event): # -> None:
        """
        triggered mouse press/release event for the scene.
        - verifies the live connection pipe.
        - makes a connection pipe if valid.
        - emits the "connection changed" signal.

        Args:
            event (QtWidgets.QGraphicsSceneMouseEvent):
                The event handler from the QtWidgets.QGraphicsScene
        """
        ...

    def start_live_connection(self, selected_port: PortItem): # -> None:
        """
        create new pipe for the connection.
        (show the live pipe visibility from the port following the cursor position)
        """
        ...

    def end_live_connection(self): # -> None:
        """
        delete live connection pipe and reset start port.
        (hides the pipe item used for drawing the live connection)
        """
        ...

    def establish_connection(self, start_port: PortItem, end_port: PortItem): # -> None:
        """
        establish a new pipe connection.
        (adds a new pipe item to draw between 2 ports)
        """
        ...

    @staticmethod
    def acyclic_check(start_port: PortItem, end_port: PortItem): # -> bool:
        """
        Validate the node connections so it doesn't loop itself.

        Args:
            start_port (PortItem): port item.
            end_port (PortItem): port item.

        Returns:
            bool: True if port connection is valid.
        """
        ...

    def tab_search_set_nodes(self, nodes): # -> None:
        ...

    def tab_search_toggle(self): # -> None:
        ...

    def rebuild_tab_search(self): # -> None:
        ...

    def qaction_for_undo(self): # -> None:
        """
        Get the undo QAction from the parent undo stack.

        Returns:
            QtWidgets.QAction: undo action.
        """
        ...

    def qaction_for_redo(self): # -> None:
        """
        Get the redo QAction from the parent undo stack.

        Returns:
            QtWidgets.QAction: redo action.
        """
        ...

    def context_menus(self): # -> dict[str, BaseMenu]:
        """
        All the available context menus for the viewer.

        Returns:
            dict: viewer context menu.
        """
        ...

    def question_dialog(self, text, title=...): # -> bool:
        """
        Prompt node viewer question dialog widget with "yes", "no" buttons.

        Args:
            text (str): dialog text.
            title (str): dialog window title.

        Returns:
            bool: true if user click yes.
        """
        ...

    def message_dialog(self, text, title=...): # -> None:
        """
        Prompt node viewer message dialog widget with "ok" button.

        Args:
            text (str): dialog text.
            title (str): dialog window title.
        """
        ...

    def load_dialog(self, current_dir=..., ext=...): # -> str | None:
        """
        Prompt node viewer file load dialog widget.

        Args:
            current_dir (str): directory path starting point. (optional)
            ext (str): custom file extension filter type. (optional)

        Returns:
            str: selected file path.
        """
        ...

    def save_dialog(self, current_dir=..., ext=...): # -> str | None:
        """
        Prompt node viewer file save dialog widget.

        Args:
            current_dir (str): directory path starting point. (optional)
            ext (str): custom file extension filter type. (optional)

        Returns:
            str: selected file path.
        """
        ...

    def all_pipes(self): # -> list[PipeItem]:
        """
        Returns all pipe qgraphic items.

        Returns:
            list[PipeItem]: instances of pipe items.
        """
        ...

    def all_nodes(self): # -> list[AbstractNodeItem]:
        """
        Returns all node qgraphic items.

        Returns:
            list[AbstractNodeItem]: instances of node items.
        """
        ...

    def selected_nodes(self): # -> list[AbstractNodeItem]:
        """
        Returns selected node qgraphic items.

        Returns:
            list[AbstractNodeItem]: instances of node items.
        """
        ...

    def selected_pipes(self): # -> list[PipeItem]:
        """
        Returns selected pipe qgraphic items.

        Returns:
            list[Pipe]: pipe items.
        """
        ...

    def selected_items(self): # -> tuple[list[Any], list[Any]]:
        """
        Return selected graphic items in the scene.

        Returns:
            tuple(list[AbstractNodeItem], list[Pipe]):
                selected (node items, pipe items).
        """
        ...

    def add_node(self, node, pos=...): # -> None:
        """
        Add node item into the scene.

        Args:
            node (AbstractNodeItem): node item instance.
            pos (tuple or list): node scene position.
        """
        ...

    @staticmethod
    def remove_node(node): # -> None:
        """
        Remove node item from the scene.

        Args:
            node (AbstractNodeItem): node item instance.
        """
        ...

    def move_nodes(self, nodes, pos=..., offset=...): # -> None:
        """
        Globally move specified nodes.

        Args:
            nodes (list[AbstractNodeItem]): node items.
            pos (tuple or list): custom x, y position.
            offset (tuple or list): x, y position offset.
        """
        ...

    def get_pipes_from_nodes(self, nodes=...): # -> list[Any] | None:
        ...

    def center_selection(self, nodes=...): # -> None:
        """
        Center on the given nodes or all nodes by default.

        Args:
            nodes (list[AbstractNodeItem]): a list of node items.
        """
        ...

    def get_pipe_layout(self): # -> int:
        """
        Returns the pipe layout mode.

        Returns:
            int: pipe layout mode.
        """
        ...

    def set_pipe_layout(self, layout): # -> None:
        """
        Sets the pipe layout mode and redraw all pipe items in the scene.

        Args:
            layout (int): pipe layout mode. (see the constants module)
        """
        ...

    def get_layout_direction(self): # -> int:
        """
        Returns the layout direction set on the node graph viewer
        used by the pipe items for drawing.

        Returns:
            int: graph layout mode.
        """
        ...

    def set_layout_direction(self, direction): # -> None:
        """
        Sets the node graph viewer layout direction for re-drawing
        the pipe items.

        Args:
            direction (int): graph layout direction.
        """
        ...

    def reset_zoom(self, cent=...): # -> None:
        """
        Reset the viewer zoom level.

        Args:
            cent (QtCore.QPoint): specified center.
        """
        ...

    def get_zoom(self): # -> float:
        """
        Returns the viewer zoom level.

        Returns:
            float: zoom level.
        """
        ...

    def set_zoom(self, value=...): # -> None:
        """
        Set the viewer zoom level.

        Args:
            value (float): zoom level
        """
        ...

    def zoom_to_nodes(self, nodes): # -> None:
        ...

    def force_update(self): # -> None:
        """
        Redraw the current node graph scene.
        """
        ...

    def scene_rect(self): # -> list[float]:
        """
        Returns the scene rect size.

        Returns:
            list[float]: x, y, width, height
        """
        ...

    def set_scene_rect(self, rect): # -> None:
        """
        Sets the scene rect and redraws the scene.

        Args:
            rect (list[float]): x, y, width, height
        """
        ...

    def scene_center(self): # -> list[float]:
        """
        Get the center x,y pos from the scene.

        Returns:
            list[float]: x, y position.
        """
        ...

    def scene_cursor_pos(self): # -> QPointF:
        """
        Returns the cursor last position mapped to the scene.

        Returns:
            QtCore.QPoint: cursor position.
        """
        ...

    def nodes_rect_center(self, nodes): # -> list[float]:
        """
        Get the center x,y pos from the specified nodes.

        Args:
            nodes (list[AbstractNodeItem]): list of node qgrphics items.

        Returns:
            list[float]: x, y position.
        """
        ...

    def clear_key_state(self): # -> None:
        """
        Resets the Ctrl, Shift, Alt modifiers key states.
        """
        ...

    def get_text_overlay(self) -> str:
        ...

    def set_text_overlay(self, text: str, align: Literal["left", "center", "right"] = ..., size: int = ..., spacing: int = ...): # -> None:
        ...

    def use_OpenGL(self): # -> None:
        """
        Use QOpenGLWidget as the viewer.
        """
        ...
