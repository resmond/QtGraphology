"""
This type stub file was generated by pyright.
"""

from PySide6 import QtWidgets

"""
This type stub file was generated by pyright.
"""
TYPE_NODE = ...
TYPE_CATEGORY = ...
class BaseNodeTreeItem(QtWidgets.QTreeWidgetItem):
    def __eq__(self, other) -> bool:
        """
        Workaround fix for QTreeWidgetItem "operator not implemented error".
        see link: https://bugreports.qt.io/browse/PYSIDE-74
        """
        ...



class NodesTreeWidget(QtWidgets.QTreeWidget):
    """
    The :class:`QtGraphology.NodesTreeWidget` is a widget for displaying all
    registered nodes from the node graph with this widget a user can create
    nodes by dragging and dropping.

    .. inheritance-diagram:: QtGraphology.NodesTreeWidget
        :parts: 1
        :top-classes: PySide6.QtWidgets.QWidget

    .. image:: _images/nodes_tree.png
        :width: 300px

    .. code-block:: python
        :linenos:

        from QtGraphology import NodeGraph, NodesTreeWidget

        # create node graph.
        graph = NodeGraph()

        # create node tree widget.
        nodes_tree = NodesTreeWidget(parent=None, node_graph=graph)
        nodes_tree.show()

    Args:
        parent (QtWidgets.QWidget): parent of the new widget.
        node_graph (QtGraphology.NodeGraph): node graph.
    """
    def __init__(self, parent=..., node_graph=...) -> None:
        ...

    def __repr__(self):
        ...

    def mimeData(self, items):
        ...

    def set_category_label(self, category, label):
        """
        Override the label for a node category root item.

        .. image:: _images/nodes_tree_category_label.png
            :width: 70%

        Args:
            category (str): node identifier category eg. ``"nodes.widgets"``
            label (str): custom display label. eg. ``"Node Widgets"``
        """
        ...

    def update(self):
        """
        Update and refresh the node tree widget.
        """
        ...
