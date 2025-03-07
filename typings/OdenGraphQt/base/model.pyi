"""
This type stub file was generated by pyright.
"""

class PortModel:
    """
    Data dump for a port object.
    """
    def __init__(self, node) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    @property
    def to_dict(self): # -> dict[str, Any]:
        """
        serialize model information to a dictionary.

        Returns:
            dict: node port dictionary eg.
                {
                    'type': 'in',
                    'name': 'port',
                    'display_name': True,
                    'multi_connection': False,
                    'visible': True,
                    'locked': False,
                    'connected_ports': {<node_id>: [<port_name>, <port_name>]}
                }
        """
        ...



class NodeModel:
    """
    Data dump for a node object.
    """
    def __init__(self) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    def add_property(self, name, value, items=..., range=..., widget_type=..., widget_tooltip=..., tab=..., **kwargs): # -> None:
        """
        add custom property or raises an error if the property name is already
        taken.

        Args:
            name (str): name of the property.
            value (object): data.
            items (list[str]): items used by widget type NODE_PROP_QCOMBO.
            range (tuple): min, max values used by NODE_PROP_SLIDER.
            widget_type (int): widget type flag.
            widget_tooltip (str): custom tooltip for the property widget.
            tab (str): widget tab name.
        """
        ...

    def set_property(self, name, value): # -> None:
        """
        Args:
            name (str): property name.
            value (object): property value.
        """
        ...

    def get_property(self, name): # -> Any | None:
        """
        Args:
            name (str): property name.

        Returns:
            object: property value.
        """
        ...

    def is_custom_property(self, name): # -> bool:
        """
        Args:
            name (str): property name.

        Returns:
            bool: true if custom property.
        """
        ...

    def get_widget_type(self, name): # -> int | None:
        """
        Args:
            name (str): property name.

        Returns:
            int: node property widget type.
        """
        ...

    def get_tab_name(self, name): # -> None:
        """
        Args:
            name (str): property name.

        Returns:
            str: name of the tab for the properties bin.
        """
        ...

    def add_port_accept_connection_type(self, port_name, port_type, node_type, accept_pname, accept_ptype, accept_ntype): # -> None:
        """
        Convenience function for adding to the "accept_connection_types" dict.
        If the node graph model is unavailable yet then we store it to a
        temp var that gets deleted.

        Args:
            port_name (str): current port name.
            port_type (str): current port type.
            node_type (str): current port node type.
            accept_pname (str): port name to accept.
            accept_ptype (str): port type accept.
            accept_ntype (str): port node type to accept.
        """
        ...

    def add_port_reject_connection_type(self, port_name, port_type, node_type, reject_pname, reject_ptype, reject_ntype): # -> None:
        """
        Convenience function for adding to the "reject_connection_types" dict.
        If the node graph model is unavailable yet then we store it to a
        temp var that gets deleted.

        Args:
            port_name (str): current port name.
            port_type (str): current port type.
            node_type (str): current port node type.
            reject_pname (str): port name to reject.
            reject_ptype (str): port type reject.
            reject_ntype (str): port node type to reject.
        """
        ...

    @property
    def properties(self): # -> dict[str, Any]:
        """
        return all default node properties.

        Returns:
            dict: default node properties.
        """
        ...

    @property
    def custom_properties(self): # -> dict[Any, Any]:
        """
        return all custom properties specified by the user.

        Returns:
            dict: user defined properties.
        """
        ...

    @property
    def to_dict(self): # -> dict[Any, dict[str, Any]]:
        """
        serialize model information to a dictionary.

        Returns:
            dict: node id as the key and properties as the values eg.
                {'0x106cf75a8': {
                    'name': 'foo node',
                    'color': (48, 58, 69, 255),
                    'border_color': (85, 100, 100, 255),
                    'text_color': (255, 255, 255, 180),
                    'type_': 'io.github.resmond.FooNode',
                    'selected': False,
                    'disabled': False,
                    'visible': True,
                    'width': 0.0,
                    'height: 0.0,
                    'pos': (0.0, 0.0),
                    'layout_direction': 0,
                    'custom': {},
                    'inputs': {
                        <port_name>: {<node_id>: [<port_name>, <port_name>]}
                    },
                    'outputs': {
                        <port_name>: {<node_id>: [<port_name>, <port_name>]}
                    },
                    'input_ports': [<port_name>, <port_name>],
                    'output_ports': [<port_name>, <port_name>],
                    },
                    subgraph_session: <sub graph session data>
                }
        """
        ...

    @property
    def serial(self): # -> str:
        """
        Serialize model information to a string.

        Returns:
            str: serialized JSON string.
        """
        ...



class NodeGraphModel:
    """
    Data dump for a node graph.
    """
    def __init__(self) -> None:
        ...

    def common_properties(self): # -> dict[Any, Any]:
        """
        Return all common node properties.

        Returns:
            dict: common node properties.
                eg.
                    {'QtGraphology.nodes.FooNode': {
                        'my_property': {
                            'widget_type': 0,
                            'tab': 'Properties',
                            'items': ['foo', 'bar', 'test'],
                            'range': (0, 100)
                            }
                        }
                    }
        """
        ...

    def set_node_common_properties(self, attrs): # -> None:
        """
        Store common node properties.

        Args:
            attrs (dict): common node properties.
                eg.
                    {'QtGraphology.nodes.FooNode': {
                        'my_property': {
                            'widget_type': 0,
                            'tab': 'Properties',
                            'items': ['foo', 'bar', 'test'],
                            'range': (0, 100)
                            }
                        }
                    }
        """
        ...

    def get_node_common_properties(self, node_type): # -> None:
        """
        Return all the common properties for a registered node.

        Args:
            node_type (str): node type.

        Returns:
            dict: node common properties.
        """
        ...

    def add_port_accept_connection_type(self, port_name, port_type, node_type, accept_pname, accept_ptype, accept_ntype): # -> None:
        """
        Convenience function for adding to the "accept_connection_types" dict.

        Args:
            port_name (str): current port name.
            port_type (str): current port type.
            node_type (str): current port node type.
            accept_pname (str):port name to accept.
            accept_ptype (str): port type accept.
            accept_ntype (str): port node type to accept.
        """
        ...

    def port_accept_connection_types(self, node_type, port_type, port_name): # -> dict[Any, Any]:
        """
        Convenience function for getting the accepted port types from the
        "accept_connection_types" dict.

        Args:
            node_type (str):
            port_type (str):
            port_name (str):

        Returns:
            dict: {<node_type>: {<port_type>: [<port_name>]}}
        """
        ...

    def add_port_reject_connection_type(self, port_name, port_type, node_type, reject_pname, reject_ptype, reject_ntype): # -> None:
        """
        Convenience function for adding to the "reject_connection_types" dict.

        Args:
            port_name (str): current port name.
            port_type (str): current port type.
            node_type (str): current port node type.
            reject_pname (str): port name to reject.
            reject_ptype (str): port type to reject.
            reject_ntype (str): port node type to reject.
        """
        ...

    def port_reject_connection_types(self, node_type, port_type, port_name): # -> dict[Any, Any]:
        """
        Convenience function for getting the accepted port types from the
        "reject_connection_types" dict.

        Args:
            node_type (str):
            port_type (str):
            port_name (str):

        Returns:
            dict: {<node_type>: {<port_type>: [<port_name>]}}
        """
        ...



if __name__ == '__main__':
    p = ...
    n = ...
