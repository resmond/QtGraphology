#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

from typing import NoReturn, Self, Any

from QtGraphology.errors import PortRegistrationError
from QtGraphology.nodes.base_node import BaseNode
from QtGraphology.qgraphics.node_port_in import PortInputNodeItem
from QtGraphology.qgraphics.node_port_out import PortOutputNodeItem

class PortInputNode(BaseNode):
    """
    The ``PortInputNode`` is the node that represents a input port from a
    :class:`QtGraphology.GroupNode` when expanded in a
    :class:`QtGraphology.SubGraph`.

    .. inheritance-diagram:: QtGraphology.nodes.port_node.PortInputNode
        :parts: 1

    .. image:: ../_images/port_in_node.png
        :width: 150px

    -
    """

    NODE_NAME = 'InputPort'

    def __init__(self: Self, qgraphics_item: PortInputNodeItem | None = None, parent_port: PortInputNodeItem | None=None) -> None:
        super(PortInputNode, self).__init__(qgraphics_item=qgraphics_item or PortInputNodeItem)
        self._parent_port: PortInputNodeItem | None = parent_port

    @property
    def parent_port(self: Self) -> PortInputNodeItem | None:
        """
        The parent group node port representing this node.

        Returns:
            QtGraphology.Port: port object.
        """
        return self._parent_port

    def add_input(self: Self, name: str='input', multi_input: bool=False, display_name: bool=True,
                  color: Any=None, locked: bool=False, painter_func: Any=None) -> NoReturn:
        """
        Warnings:
            This is not available for the ``PortInputNode`` class.
        """
        raise PortRegistrationError(f'"{self.__class__.__name__}.add_input()" is not available for {self}.')


    def add_output(self, name='output', multi_output=True, display_name=True,
                   color=None, locked=False, painter_func=None):
        """
        Warnings:
            This function is called by :meth:`QtGraphology.SubGraph.expand_group_node`
            and is not available for the ``PortInputNode`` class.
        """
        if self._outputs:
            raise PortRegistrationError(f'"{self.__class__.__name__}.add_output()" only ONE output is allowed for this node.')

        super(PortInputNode, self).add_output(
            name=name,
            multi_output=multi_output,
            display_name=False,
            color=color,
            locked=locked,
            painter_func=None
        )


class PortOutputNode(BaseNode):
    """
    The ``PortOutputNode`` is the node that represents a output port from a
    :class:`QtGraphology.GroupNode` when expanded in a
    :class:`QtGraphology.SubGraph`.

    .. inheritance-diagram:: QtGraphology.nodes.port_node.PortOutputNode
        :parts: 1

    .. image:: ../_images/port_out_node.png
        :width: 150px

    -
    """

    NODE_NAME = 'OutputPort'

    def __init__(self, qgraphics_item=None, parent_port=None):
        super(PortOutputNode, self).__init__(
            qgraphics_item or PortOutputNodeItem
        )
        self._parent_port = parent_port

    @property
    def parent_port(self):
        """
        The parent group node port representing this node.

        Returns:
            QtGraphology.Port: port object.
        """
        return self._parent_port

    def add_input(self, name='input', multi_input=False, display_name=True,
                  color=None, locked=False, painter_func=None):
        """
        Warnings:
            This function is called by :meth:`QtGraphology.SubGraph.expand_group_node`
            and is not available for the ``PortOutputNode`` class.
        """
        if self._inputs:
            raise PortRegistrationError(
                '"{}.add_input()" only ONE input is allowed for this node.'
                .format(self.__class__.__name__, self)
            )
        super(PortOutputNode, self).add_input(
            name=name,
            multi_input=multi_input,
            display_name=False,
            color=color,
            locked=locked,
            painter_func=None
        )

    def add_output(self, name='output', multi_output=True, display_name=True,
                   color=None, locked=False, painter_func=None):
        """
        Warnings:
            This is not available for the ``PortOutputNode`` class.
        """
        raise PortRegistrationError(
            '"{}.add_output()" is not available for {}.'
            .format(self.__class__.__name__, self)
        )
