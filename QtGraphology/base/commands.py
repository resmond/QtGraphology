#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Self, Any
from PySide6 import QtWidgets, QtGui

from QtGraphology.constants import PortTypeEnum
from QtGraphology.base.node import NodeObject, NodeModel
class PropertyChangedCmd(QtGui.QUndoCommand):
    """
    Node property changed command.

    Args:
        node (QtGraphology.NodeObject): node.
        name (str): node property name.
        value (object): node property value.
    """

    def __init__(self : Self, node: NodeObject, name: str, value: Any) -> None:
        QtGui.QUndoCommand.__init__(self)
        self.setText(f"property '{node.name()}':'{name}'")
        self.node: NodeObject = node
        self.name: str = name
        self.old_val: Any = node.get_property(name)
        self.new_val: Any = value

    def set_node_property(self: Self, name: str, value: Any) -> None:
        """
        updates the node view and model.
        """
        # set model data.
        model: NodeModel = self.node.model
        model.set_property(name, value)

        # set view data.
        view = self.node.view

        # view widgets.
        if hasattr(view, 'widgets'):
            widgets = view.__getattribute__('widgets')
            if name in widgets.keys():
                # check if previous value is identical to current value,
                # prevent signals from causing a infinite loop.
                if widgets[name].get_value() != value:
                    widgets[name].set_value(value)

        # view properties.
        if name in view.properties.keys():
            # remap "pos" to "xy_pos" node view has pre-existing pos method.
            if name == 'pos':
                name = 'xy_pos'
            setattr(view, name, value)

        # emit property changed signal.
        graph = self.node.graph
        graph.property_changed.emit(self.node, self.name, value)

    def undo(self) -> None:
        if self.old_val != self.new_val:
            self.set_node_property(self.name, self.old_val)

    def redo(self) -> None:
        if self.old_val != self.new_val:
            self.set_node_property(self.name, self.new_val)
