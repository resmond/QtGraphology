#!/usr/bin/python

# ------------------------------------------------------------------------------
# menu command functions
# ------------------------------------------------------------------------------
#from tkinter import NO
from QtGraphology import NodeGraph


def zoom_in(graph: NodeGraph) -> None:
    """
    Set the node graph to zoom in by 0.1
    """
    zoom: float = graph.get_zoom() + 0.1
    graph.set_zoom(zoom=zoom)


def zoom_out(graph: NodeGraph) -> None:
    """
    Set the node graph to zoom in by 0.1
    """
    zoom: float = graph.get_zoom() - 0.2
    graph.set_zoom(zoom=zoom)


def reset_zoom(graph: NodeGraph) -> None:
    """
    Reset zoom level.
    """
    graph.reset_zoom()


def layout_h_mode(graph: NodeGraph) -> None:
    """
    Set node graph layout direction to horizontal.
    """
    graph.set_layout_direction(direction=0)


def layout_v_mode(graph: NodeGraph) -> None:
    """
    Set node graph layout direction to vertical.
    """
    graph.set_layout_direction(direction=1)


def open_session(graph: NodeGraph) -> None:
    """
    Prompts a file open dialog to load a session.
    """
    current: str = graph.current_session()
    file_path: str = graph.load_dialog(current_dir=current)
    if file_path:
        graph.load_session(file_path=file_path)


def import_session(graph: NodeGraph) -> None:
    """
    Prompts a file open dialog to load a session.
    """
    current: str = graph.current_session()
    file_path: str = graph.load_dialog(current_dir=current)
    if file_path:
        graph.import_session(file_path=file_path)


def save_session(graph: NodeGraph) -> None:
    """
    Prompts a file save dialog to serialize a session if required.
    """
    current: str = graph.current_session()
    if current:
        graph.save_session(file_path=current)
        msg: str = 'Session layout saved:\n{}'.format(current)
        viewer = graph.viewer()
        viewer.message_dialog(msg, title='Session Saved')
    else:
        save_session_as(graph)


def save_session_as(graph: NodeGraph):
    """
    Prompts a file save dialog to serialize a session.
    """
    current = graph.current_session()
    file_path = graph.save_dialog(current)
    if file_path:
        graph.save_session(file_path)


def clear_session(graph: NodeGraph):
    """
    Prompts a warning dialog to new a node graph session.
    """
    if graph.question_dialog('Clear Current Session?', 'Clear Session'):
        graph.clear_session()


def clear_undo(graph: NodeGraph):
    """
    Prompts a warning dialog to clear undo.
    """
    viewer = graph.viewer()
    msg = 'Clear all undo history, Are you sure?'
    if viewer.question_dialog('Clear Undo History', msg):
        graph.clear_undo_stack()


def copy_nodes(graph: NodeGraph):
    """
    Copy nodes to the clipboard.
    """
    graph.copy_nodes()


def cut_nodes(graph: NodeGraph):
    """
    Cut nodes to the clip board.
    """
    graph.cut_nodes()


def paste_nodes(graph: NodeGraph):
    """
    Pastes nodes copied from the clipboard.
    """
    graph.paste_nodes()


def delete_nodes(graph: NodeGraph):
    """
    Delete selected node.
    """
    graph.delete_nodes(graph.selected_nodes())


def extract_nodes(graph: NodeGraph):
    """
    Extract selected nodes.
    """
    graph.extract_nodes(graph.selected_nodes())


def clear_node_connections(graph: NodeGraph):
    """
    Clear port connection on selected nodes.
    """
    graph.undo_stack().beginMacro('clear selected node connections')
    for node in graph.selected_nodes():
        for port in node.input_ports() + node.output_ports():
            port.clear_connections()
    graph.undo_stack().endMacro()


def select_all_nodes(graph: NodeGraph):
    """
    Select all nodes.
    """
    graph.select_all()


def clear_node_selection(graph: NodeGraph):
    """
    Clear node selection.
    """
    graph.clear_selection()


def invert_node_selection(graph: NodeGraph):
    """
    Invert node selection.
    """
    graph.invert_selection()


def disable_nodes(graph: NodeGraph):
    """
    Toggle disable on selected nodes.
    """
    graph.disable_nodes(graph.selected_nodes())


def duplicate_nodes(graph: NodeGraph):
    """
    Duplicated selected nodes.
    """
    graph.duplicate_nodes(graph.selected_nodes())


def expand_group_node(graph: NodeGraph):
    """
    Expand selected group node.
    """
    selected_nodes = graph.selected_nodes()
    if not selected_nodes:
        graph.message_dialog('Please select a "GroupNode" to expand.')
        return
    graph.expand_group_node(selected_nodes[0])


def fit_to_selection(graph: NodeGraph):
    """
    Sets the zoom level to fit selected nodes.
    """
    graph.fit_to_selection()


def show_undo_view(graph: NodeGraph):
    """
    Show the undo list widget.
    """
    graph.undo_view.show()


def curved_pipe(graph: NodeGraph):
    """
    Set node graph pipes layout as curved.
    """
    from QtGraphology.constants import PipeLayoutEnum
    graph.set_pipe_style(PipeLayoutEnum.CURVED.value)


def straight_pipe(graph: NodeGraph):
    """
    Set node graph pipes layout as straight.
    """
    from QtGraphology.constants import PipeLayoutEnum
    graph.set_pipe_style(PipeLayoutEnum.STRAIGHT.value)


def angle_pipe(graph: NodeGraph):
    """
    Set node graph pipes layout as angled.
    """
    from QtGraphology.constants import PipeLayoutEnum
    graph.set_pipe_style(PipeLayoutEnum.ANGLE.value)


def bg_grid_none(graph: NodeGraph):
    """
    Turn off the background patterns.
    """
    from QtGraphology.constants import ViewerEnum
    graph.set_grid_mode(ViewerEnum.GRID_DISPLAY_NONE.value)


def bg_grid_dots(graph: NodeGraph):
    """
    Set background node graph background with grid dots.
    """
    from QtGraphology.constants import ViewerEnum
    graph.set_grid_mode(ViewerEnum.GRID_DISPLAY_DOTS.value)


def bg_grid_lines(graph: NodeGraph):
    """
    Set background node graph background with grid lines.
    """
    from QtGraphology.constants import ViewerEnum
    graph.set_grid_mode(ViewerEnum.GRID_DISPLAY_LINES.value)


def layout_graph_down(graph: NodeGraph):
    """
    Auto layout the nodes down stream.
    """
    nodes = graph.selected_nodes() or graph.all_nodes()
    graph.auto_layout_nodes(nodes=nodes, down_stream=True)


def layout_graph_up(graph: NodeGraph):
    """
    Auto layout the nodes up stream.
    """
    nodes = graph.selected_nodes() or graph.all_nodes()
    graph.auto_layout_nodes(nodes=nodes, down_stream=False)


def toggle_node_search(graph: NodeGraph):
    """
    show/hide the node search widget.
    """
    graph.toggle_node_search()
