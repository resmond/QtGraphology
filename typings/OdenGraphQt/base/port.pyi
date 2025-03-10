"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from QtGraphology import NodeObject
from QtGraphology.qgraphics.port import PortItem

"""
This type stub file was generated by pyright.
"""
if TYPE_CHECKING:
    ...
class Port:
    """
    The ``Port`` class is used for connecting one node to another.

    .. inheritance-diagram:: QtGraphology.Port

    .. image:: _images/port.png
        :width: 50%

    See Also:
        For adding a ports into a node see:
        :meth:`BaseNode.add_input`, :meth:`BaseNode.add_output`

    Args:
        node (QtGraphology.NodeObject): parent node.
        port_item (PortItem): graphic item used for drawing.
    """
    def __init__(self, node, port_item) -> None:
        ...

    def __repr__(self):
        ...

    @property
    def port_item(self) -> PortItem:
        ...

    @property
    def port_node(self) -> NodeObject:
        ...

    @property
    def view(self):
        """
        Returns the :class:`QtWidgets.QGraphicsItem` used in the scene.

        Returns:
            QtGraphology.qgraphics.port.PortItem: port item.
        """
        ...

    @property
    def model(self):
        """
        Returns the port model.

        Returns:
            QtGraphology.base.model.PortModel: port model.
        """
        ...

    def type_(self):
        """
        Returns the port type.

        Port Types:
            - :attr:`QtGraphology.constants.IN_PORT` for input port
            - :attr:`QtGraphology.constants.OUT_PORT` for output port

        Returns:
            str: port connection type.
        """
        ...

    def multi_connection(self):
        """
        Returns if the ports is a single connection or not.

        Returns:
            bool: false if port is a single connection port
        """
        ...

    def node(self):
        """
        Return the parent node.

        Returns:
            QtGraphology.BaseNode: parent node object.
        """
        ...

    def name(self):
        """
        Returns the port name.

        Returns:
            str: port name.
        """
        ...

    def visible(self):
        """
        Port visible in the node graph.

        Returns:
            bool: true if visible.
        """
        ...

    def set_visible(self, visible=..., push_undo=...):
        """
        Sets weather the port should be visible or not.

        Args:
            visible (bool): true if visible.
            push_undo (bool): register the command to the undo stack. (default: True)
        """
        ...

    def locked(self):
        """
        Returns the locked state.

        If ports are locked then new pipe connections can't be connected
        and current connected pipes can't be disconnected.

        Returns:
            bool: true if locked.
        """
        ...

    def lock(self):
        """
        Lock the port so new pipe connections can't be connected and
        current connected pipes can't be disconnected.

        This is the same as calling :meth:`Port.set_locked` with the arg
        set to ``True``
        """
        ...

    def unlock(self):
        """
        Unlock the port so new pipe connections can be connected and
        existing connected pipes can be disconnected.

        This is the same as calling :meth:`Port.set_locked` with the arg
        set to ``False``
        """
        ...

    def set_locked(self, state=..., connected_ports=..., push_undo=...):
        """
        Sets the port locked state. When locked pipe connections can't be
        connected or disconnected from this port.

        Args:
            state (Bool): port lock state.
            connected_ports (Bool): apply to lock state to connected ports.
            push_undo (bool): register the command to the undo stack. (default: True)
        """
        ...

    def connected_ports(self):
        """
        Returns all connected ports.

        Returns:
            list[QtGraphology.Port]: list of connected ports.
        """
        ...

    def connect_to(self, target_port=..., push_undo=..., emit_signal=...):
        """
        Create connection to the specified port and emits the
        :attr:`NodeGraph.port_connected` signal from the parent node graph.

        Args:
            target_port (QtGraphology.Port): port object.
            push_undo (bool): register the command to the undo stack. (default: True)
            emit_signal (bool): emit the port connection signals. (default: True)
        """
        ...

    def disconnect_from(self, target_port=..., push_undo=..., emit_signal=...):
        """
        Disconnect from the specified port and emits the
        :attr:`NodeGraph.port_disconnected` signal from the parent node graph.

        Args:
            target_port (QtGraphology.Port): port object.
            push_undo (bool): register the command to the undo stack. (default: True)
            emit_signal (bool): emit the port connection signals. (default: True)
        """
        ...

    def clear_connections(self, push_undo=..., emit_signal=...):
        """
        Disconnect from all port connections and emit the
        :attr:`NodeGraph.port_disconnected` signals from the node graph.

        See Also:
            :meth:`Port.disconnect_from`,
            :meth:`Port.connect_to`,
            :meth:`Port.connected_ports`

        Args:
            push_undo (bool): register the command to the undo stack. (default: True)
            emit_signal (bool): emit the port connection signals. (default: True)
        """
        ...

    def add_accept_port_type(self, port_name, port_type, node_type):
        """
        Add a constraint to "accept" a pipe connection.

        Once a constraint has been added only ports of that type specified will
        be allowed a pipe connection.

        `Implemented in` ``v0.6.0``

        See Also:
            :meth:`QtGraphology.Port.add_reject_ports_type`,
            :meth:`QtGraphology.BaseNode.add_accept_port_type`

        Args:
            port_name (str): name of the port.
            port_type (str): port type.
            node_type (str): port node type.
        """
        ...

    def accepted_port_types(self):
        """
        Returns a dictionary of connection constrains of the port types
        that allow for a pipe connection to this node.

        See Also:
            :meth:`QtGraphology.BaseNode.accepted_port_types`

        Returns:
            dict: {<node_type>: {<port_type>: [<port_name>]}}
        """
        ...

    def add_reject_port_type(self, port_name, port_type, node_type):
        """
        Add a constraint to "reject" a pipe connection.

        Once a constraint has been added only ports of that type specified will
        be rejected a pipe connection.

        `Implemented in` ``v0.6.0``

        See Also:
            :meth:`QtGraphology.Port.add_accept_ports_type`,
            :meth:`QtGraphology.BaseNode.add_reject_port_type`

        Args:
            port_name (str): name of the port.
            port_type (str): port type.
            node_type (str): port node type.
        """
        ...

    def rejected_port_types(self):
        """
        Returns a dictionary of connection constrains of the port types
        that are NOT allowed for a pipe connection to this node.

        See Also:
            :meth:`QtGraphology.BaseNode.rejected_port_types`

        Returns:
            dict: {<node_type>: {<port_type>: [<port_name>]}}
        """
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
