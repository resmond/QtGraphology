#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

import json
from collections import defaultdict
from re import S
#from tkinter import N
from typing import Any, Literal, Self

from QtGraphology.errors import NodePropertyError
from QtGraphology.base.node import NodeObject
from QtGraphology.constants import *
class PortModel(object):
    """
    Data dump for a port object.
    """

    def __init__(self: Self, node: NodeObject | None) -> None:
        self.node: NodeObject | None = node
        self.type: str = ''
        self.name: str = 'port'
        self.display_name: bool = True
        self.multi_connection: bool = False
        self.visible: bool = True
        self.locked: bool = False
        self.connected_ports: defaultdict[str, list] = defaultdict(list)

    def __repr__(self: Self) -> str:
        return '<{}(\'{}\') object at {}>'.format(
            self.__class__.__name__, self.name, hex(id(self)))

    @property
    def to_dict(self: Self) -> dict[str, Any]:
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
        props: dict[str, Any] = self.__dict__.copy()
        props.pop('node')
        props['connected_ports'] = dict(props.pop('connected_ports'))
        return props


class NodeModel(object):
    """
    Data dump for a node object.
    """

    def __init__(self: Self) -> None:
        self.type_: str = ''
        self.id: str = hex(id(self))
        self.icon: str = ''
        self.name: str = 'node'
        self.color: TCOLOR = (13, 18, 23, 255)
        self.border_color: TCOLOR = (74, 84, 85, 255)
        self.text_color: TCOLOR = (255, 255, 255, 180)
        self.disabled: bool = False
        self.selected: bool = False
        self.visible: bool = True
        self.width: float = 100.0
        self.height: float = 80.0
        self.pos: list[float] = [0.0, 0.0]
        self.layout_direction: LayoutDirectionEnum = LayoutDirectionEnum.HORIZONTAL

        # BaseNode attrs.
        self.inputs: dict[str, Any] = {}
        self.outputs: dict[str,Any] = {}
        self.port_deletion_allowed: bool = False

        # GroupNode attrs.
        self.subgraph_session: dict[str, Any] = {}

        # Custom
        self._custom_prop: dict[str,Any] = {}

        # node graph model set at node added time.
        self._graph_model: NodeGraphModel | None = None

        # store the property attributes.
        # (deleted when node is added to the graph)
        self._TEMP_property_attrs: dict[str,Any] = {}

        # temp store the property widget types.
        # (deleted when node is added to the graph)
        self._TEMP_property_widget_types: dict[str, Any] = {
            'type_': NodePropWidgetEnum.QLABEL.value,
            'id': NodePropWidgetEnum.QLABEL.value,
            'icon': NodePropWidgetEnum.HIDDEN.value,
            'name': NodePropWidgetEnum.QLINE_EDIT.value,
            'color': NodePropWidgetEnum.COLOR_PICKER.value,
            'border_color': NodePropWidgetEnum.HIDDEN.value,
            'text_color': NodePropWidgetEnum.COLOR_PICKER.value,
            'disabled': NodePropWidgetEnum.QCHECK_BOX.value,
            'selected': NodePropWidgetEnum.HIDDEN.value,
            'width': NodePropWidgetEnum.HIDDEN.value,
            'height': NodePropWidgetEnum.HIDDEN.value,
            'pos': NodePropWidgetEnum.HIDDEN.value,
            'layout_direction': NodePropWidgetEnum.HIDDEN.value,
            'inputs': NodePropWidgetEnum.HIDDEN.value,
            'outputs': NodePropWidgetEnum.HIDDEN.value,
        }

        # temp store connection constrains.
        # (deleted when node is added to the graph)
        # OGQ-1: refer to NodeGraph.add_node for the temp key pop
        self._TEMP_accept_connection_types: dict[str, Any] = {}
        self._TEMP_reject_connection_types: dict[str, Any] = {}

    def __repr__(self: Self) -> str:
        return f'<{self.__class__.__name__}(\'{self.name}\') object at {self.id}>'

    def add_property(
            self: Self,
            name: str,
            value: Any,
            items: list[Any] = [],
            range: Any = None,
            widget_type: NodePropWidgetEnum = NodePropWidgetEnum.HIDDEN,
            widget_tooltip: str='',
            tab: str | None=None,
            **kwargs: dict[str, Any]
    ) -> None:
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
        widget_type: NodePropWidgetEnum = widget_type
        tab: str | None = tab or 'Properties'

        if name in self.properties.keys():
            raise NodePropertyError(
                '"{}" reserved for default property.'.format(name))
        if name in self._custom_prop.keys():
            raise NodePropertyError(
                '"{}" property already exists.'.format(name))

        self._custom_prop[name] = value

        if self._graph_model is None:
            self._TEMP_property_widget_types[name] = widget_type
            self._TEMP_property_attrs[name] = {'tab': tab}
            if items:
                self._TEMP_property_attrs[name]['items'] = items
            if range:
                self._TEMP_property_attrs[name]['range'] = range
            if widget_tooltip:
                self._TEMP_property_attrs[name]['tooltip'] = widget_tooltip
            if kwargs:
                self._TEMP_property_attrs[name].update(kwargs)
        else:
            attrs: dict[str, dict[str, dict[str, NodePropWidgetEnum | str]]] = {
                self.type_: {
                    name: {
                        'widget_type': widget_type,
                        'tab': tab
                    }
                }
            }
            if items:
                attrs[self.type_][name]['items'] = items
            if range:
                attrs[self.type_][name]['range'] = range
            if widget_tooltip:
                attrs[self.type_][name]['tooltip'] = widget_tooltip
            if kwargs:
                attrs[self.type_][name].update(kwargs)

            self._graph_model.set_node_common_properties(attrs)

    def set_property(self, name, value):
        """
        Args:
            name (str): property name.
            value (object): property value.
        """
        if name in self.properties.keys():
            setattr(self, name, value)
        elif name in self._custom_prop.keys():
            self._custom_prop[name] = value
        else:
            raise NodePropertyError('No property "{}"'.format(name))

    def get_property(self, name):
        """
        Args:
            name (str): property name.

        Returns:
            object: property value.
        """
        if name in self.properties.keys():
            return self.properties[name]
        return self._custom_prop.get(name)

    def is_custom_property(self, name):
        """
        Args:
            name (str): property name.

        Returns:
            bool: true if custom property.
        """
        return name in self._custom_prop

    def get_widget_type(self: Self, name: str) -> Any:
        """
        Args:
            name (str): property name.

        Returns:
            int: node property widget type.
        """
        model: NodeGraphModel | None = self._graph_model
        if model is None:
            return self._TEMP_property_widget_types.get(name)
        return model.get_node_common_properties(self.type_)[name]['widget_type']

    def get_tab_name(self: Self, name: str) -> str | None:
        """
        Args:
            name (str): property name.

        Returns:
            str: name of the tab for the properties bin.
        """
        model = self._graph_model
        if model is None:
            attrs = self._TEMP_property_attrs.get(name)
            if attrs:
                return attrs.get('tab')
            return None
        return model.get_node_common_properties(self.type_)[name]['tab']

    def add_port_accept_connection_type(
            self: Self,
            port_name: str,
            port_type: str,
            node_type: str,
            accept_pname: str,
            accept_ptype: str,
            accept_ntype: str,
    ) -> None:
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
        model: NodeGraphModel | None = self._graph_model
        if model:
            model.add_port_accept_connection_type(
                port_name=port_name, port_type=port_type, node_type=node_type,
                accept_pname=accept_pname, accept_ptype=accept_ptype, accept_ntype=accept_ntype,
            )
            return

        connection_data: dict[str, Any] = self._TEMP_accept_connection_types
        keys: list[str] = [node_type, port_type, port_name, accept_ntype]
        # TODO: This is a very weird for loop condition aka for context, this
        #  always result in connection_data becoming empty dict since the original
        #  _TEMP_accept_connection_types is already empty dict on init
        for key in keys:
            if key not in connection_data.keys():
                connection_data[key] = {}
            connection_data = connection_data[key]

        if accept_ptype not in connection_data:
            connection_data[accept_ptype] = {accept_pname}
        else:
            connection_data[accept_ptype].add(accept_pname)

    # Todo: This function is not used anywhere in the codebase
    def add_port_reject_connection_type(
            self: Self,
            port_name: str,
            port_type: str,
            node_type: str,
            reject_pname: str,
            reject_ptype: str,
            reject_ntype: str,
    ) -> None:
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
        model: NodeGraphModel | None = self._graph_model
        if model:
            model.add_port_reject_connection_type(
                port_name=port_name, port_type=port_type, node_type=node_type,
                reject_pname=reject_pname, reject_ptype=reject_ptype, reject_ntype=reject_ntype,
            )

        connection_data = self._TEMP_reject_connection_types
        keys: list[str]= [node_type, port_type, port_name, reject_ntype]
        # TODO: This is a very weird for loop condition aka for context, this
        #  always result in connection_data becoming empty dict since the original
        #  _TEMP_reject_connection_types is already empty dict on init
        for key in keys:
            if key not in connection_data.keys():
                connection_data[key] = {}
            connection_data = connection_data[key]

        if reject_ptype not in connection_data:
            connection_data[reject_ptype] = {reject_pname}
        else:
            connection_data[reject_ptype].add(reject_pname)

    @property
    def properties(self: Self) -> dict[str, Any]:
        """
        return all default node properties.

        Returns:
            dict: default node properties.
        """
        props: dict[str, Any] = self.__dict__.copy()
        exclude: list[str] = [
            "_custom_prop",
            "_graph_model",
            "_TEMP_property_attrs",
            "_TEMP_property_widget_types"
        ]
        exclude_keys = [i for i in exclude if i in props.keys()]
        for key in exclude_keys:
            props.pop(key)

        return props

    @property
    def properties(self: Self) -> dict[str, Any]:
        """
        return all custom properties specified by the user.

        Returns:
            dict: user defined properties.
        """
        return self._custom_prop

    @property
    def to_dict(self)-> dict[str, dict[str, Any]]:
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
        node_dict: dict[str, Any] = self.__dict__.copy()
        node_id: str = node_dict.pop('id')

        inputs: dict[str, Any] = {}
        outputs: dict[str, Any] = {}
        input_ports: list[dict[str, Any]] = []
        output_ports: list[dict[str, Any]] = []
        for name, model in node_dict.pop('inputs').items():
            if self.port_deletion_allowed:
                output_ports.append({
                    'name': name,
                    'multi_connection': model.multi_connection,
                    'display_name': model.display_name,
                })
            connected_ports: dict[str, Any] = model.to_dict['connected_ports']
            if connected_ports:
                inputs[name] = connected_ports
        for name, model in node_dict.pop('outputs').items():
            if self.port_deletion_allowed:
                output_ports.append({
                    'name': name,
                    'multi_connection': model.multi_connection,
                    'display_name': model.display_name,
                })
            connected_ports: dict[str, Any] = model.to_dict['connected_ports']
            if connected_ports:
                outputs[name] = connected_ports
            if connected_ports:
                outputs[name] = connected_ports
        if inputs:
            node_dict['inputs'] = inputs
        if outputs:
            node_dict['outputs'] = outputs

        if self.port_deletion_allowed:
            node_dict['input_ports'] = input_ports
            node_dict['output_ports'] = output_ports

        if self.subgraph_session:
            node_dict['subgraph_session'] = self.subgraph_session

        custom_props = node_dict.pop('_custom_prop', {})
        if custom_props:
            node_dict['custom'] = custom_props

        exclude: list[str] = ['_graph_model',
                   '_TEMP_property_attrs',
                   '_TEMP_property_widget_types']
        [node_dict.pop(i) for i in exclude if i in node_dict.keys()]

        return {node_id: node_dict}

    @property
    def serial(self) -> str:
        """
        Serialize model information to a string.

        Returns:
            str: serialized JSON string.
        """
        model_dict: dict[str, Any] = self.to_dict
        return json.dumps(model_dict)


class NodeGraphModel(object):
    """
    Data dump for a node graph.
    """

    def __init__(self: Self) -> None:
        self.__common_node_props: dict[str, Any] = {}

        self.accept_connection_types: dict[str, Any] = {}
        self.reject_connection_types: dict[str, Any] = {}

        self.node: dict[str, Any] = {}
        self.session: str = ''
        self.acyclic: bool = True
        self.pipe_collision: bool = False
        self.pipe_slicing: bool = True
        self.pipe_style: PipeLayoutEnum = PipeLayoutEnum.CURVED.value
        self.layout_direction: LayoutDirectionEnum = LayoutDirectionEnum.HORIZONTAL.value

    def common_properties(self: Self) -> dict[str, Any]:
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
        return self.__common_node_props

    def set_node_common_properties(self: Self, attrs: dict[str, Any]) -> None:
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
        for node_type in attrs.keys():
            node_props: dict[str, Any] = attrs[node_type]

            if node_type not in self.__common_node_props.keys():
                self.__common_node_props[node_type] = node_props
                continue

            for prop_name, prop_attrs in node_props.items():
                common_props: dict[str, Any] = self.__common_node_props[node_type]
                if prop_name not in common_props.keys():
                    common_props[prop_name] = prop_attrs
                    continue
                common_props[prop_name].update(prop_attrs)

    def get_node_common_properties(self: Self, node_type: str) -> dict[str, Any] | None:
        """
        Return all the common properties for a registered node.

        Args:
            node_type (str): node type.

        Returns:
            dict: node common properties.
        """
        return self.__common_node_props.get(node_type)

    def add_port_accept_connection_type(
            self: Self,
            port_name: str,
            port_type: str,
            node_type: str,
            accept_pname: str,
            accept_ptype: str,
            accept_ntype: str
    ) -> None:
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
        connection_data: dict[str, Any] = self.accept_connection_types
        keys: list[str] = [node_type, port_type, port_name, accept_ntype]
        # TODO: This is a very weird for loop condition
        for key in keys:
            if key not in connection_data.keys():
                connection_data[key] = {}
            connection_data = connection_data[key]

        if accept_ptype not in connection_data:
            connection_data[accept_ptype] = [accept_pname]
        else:
            connection_data[accept_ptype].append(accept_pname)

    def port_accept_connection_types(self: Self, node_type: str, port_type: str, port_name: str) -> dict[str, Any]:
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
        data: dict[str, Any] = self.accept_connection_types.get(node_type) or {}
        accepted_types: dict[str, Any] = data.get(port_type) or {}
        return accepted_types.get(port_name) or {}

    def add_port_reject_connection_type(
            self: Self,
            port_name: str,
            port_type: str,
            node_type: str,
            reject_pname: str,
            reject_ptype: str,
            reject_ntype: str,
    ) -> None:
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
        connection_data: dict[str, Any] = self.reject_connection_types
        keys: list[str] = [node_type, port_type, port_name, reject_ntype]
        # TODO: The same very weird for loop condition
        for key in keys:
            if key not in connection_data.keys():
                connection_data[key] = {}
            connection_data = connection_data[key]

        if reject_ptype not in connection_data:
            connection_data[reject_ptype] = [reject_pname]
        else:
            connection_data[reject_ptype].append(reject_pname)

    def port_reject_connection_types(self: Self, node_type: str, port_type: str, port_name: str) -> dict[str, Any]:
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
        data: dict[str, Any] = self.reject_connection_types.get(node_type) or {}
        rejected_types: dict[str, Any] = data.get(port_type) or {}
        return rejected_types.get(port_name) or {}


if __name__ == '__main__':
    p = PortModel(None)
    # print(p.to_dict)

    n = NodeModel()
    n.inputs[p.name] = p
    n.add_property('foo', 'bar')

    print('-'*100)
    print('property keys\n')
    print(list(n.properties.keys()))
    print('-'*100)
    print('to_dict\n')
    for k, v in n.to_dict[n.id].items():
        print(k, v)
