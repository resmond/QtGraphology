"""
This type stub file was generated by pyright.
"""

from QtGraphology.nodes.base_node import BaseNode

"""
This type stub file was generated by pyright.
"""
class GroupNode(BaseNode):
    """
    `Implemented in` ``v0.2.0``

    The ``QtGraphology.GroupNode`` class extends from the :class:`QtGraphology.BaseNode`
    class with the ability to nest other nodes inside of it.

    .. inheritance-diagram:: QtGraphology.GroupNode

    .. image:: ../_images/group_node.png
        :width: 250px

    -
    """
    NODE_NAME = ...
    def __init__(self, qgraphics_item=...) -> None:
        ...

    @property
    def is_expanded(self):
        """
        Returns if the group node is expanded or collapsed.

        Returns:
            bool: true if the node is expanded.
        """
        ...

    def get_sub_graph(self):
        """
        Returns the sub graph controller to the group node if initialized
        or returns None.

        Returns:
            SubGraph: sub graph controller.
        """
        ...

    def get_sub_graph_session(self):
        """
        Returns the serialized sub graph session.

        Returns:
            dict: serialized sub graph session.
        """
        ...

    def set_sub_graph_session(self, serialized_session):
        """
        Sets the sub graph session data to the group node.

        Args:
            serialized_session (dict): serialized session.
        """
        ...

    def expand(self):
        """
        Expand the group node session.

        See Also:
            :meth:`NodeGraph.expand_group_node`,
            :meth:`SubGraph.expand_group_node`.

        Returns:
            SubGraph: node graph used to manage the nodes expaneded session.
        """
        ...

    def collapse(self):
        """
        Collapse the group node session it's expanded child sub graphs.

        See Also:
            :meth:`NodeGraph.collapse_group_node`,
            :meth:`SubGraph.collapse_group_node`.
        """
        ...

    def set_name(self, name=...):
        ...

    def add_input(self, name=..., multi_input=..., display_name=..., color=..., locked=..., painter_func=...):
        ...

    def add_output(self, name=..., multi_output=..., display_name=..., color=..., locked=..., painter_func=...):
        ...

    def delete_input(self, port):
        ...

    def delete_output(self, port):
        ...
