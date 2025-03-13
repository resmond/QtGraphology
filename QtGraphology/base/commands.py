#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Self, Any
from PySide6 import QtWidgets, QtGui

from QtGraphology.constants import PortTypeEnum
from QtGraphology.base.node import NodeObject

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
        self.setText('property "{}:{}"'.format(node.name(), name))
        self.node = node
        self.name = name
        self.old_val = node.get_property(name)
        self.new_val = value

    def set_node_property(self: Self, name: str, value: Any) -> None:
        """
        updates the node view and model.
        """
        # set model data.
        model = self.node.model
        model.set_property(name, value)

        # set view data.
        view = self.node.view

        # view widgets.
        if hasattr(view, 'widgets') and name in view.widgets.keys():
            # check if previous value is identical to current value,
            # prevent signals from causing a infinite loop.
            if view.widgets[name].get_value() != value:
                view.widgets[name].set_value(value)

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
