#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING, Self

import re
#from distutils.version import LooseVersion
from packaging.version import parse as version_parse

from PySide6 import QtGui, QtCore

from QtGraphology.errors import NodeMenuError
from QtGraphology.widgets.actions import BaseMenu, GraphAction, NodeAction, NodeGraph

class NodeGraphMenu(object):
    """
    The ``NodeGraphMenu`` is the main context menu triggered from the node graph.
    """

    def __init__(self: Self, graph: NodeGraph, qmenu: NodeGraphMenu):
        self._graph: NodeGraph = graph
        self._qmenu: NodeGraphMenu = qmenu
        self._name: str = qmenu.title()
        self._menus: dict[str, NodeGraphMenu] = {}
        self._commands: dict[str, NodeGraphCommand] = {}
        self._items: list[NodeGraphMenu] = []

    def __repr__(self):
        return f'<{self.__class__.__name__}("{self.name()}") object at {hex(id(self))}>'

    @property
    def qmenu(self: Self) -> NodeGraphMenu:
        """
        The underlying QMenu.

        Returns:
            BaseMenu: menu object.
        """
        return self._qmenu

    def name(self: Self) -> str:
        """
        Returns the name for the menu.

        Returns the name for the menu.

        Returns:
            str: label name.
        """
        return self._name

    def get_items(self: Self) -> list[NodeGraphMenu]:
        """
        Return the menu items in the order they were added.

        Returns:
            list: current menu items.
        """
        return self._items

    def get_menu(self: Self, name: str) -> NodeGraphMenu | None:
        """
        Returns the child menu by name.

        Args:
            name (str): name of the menu.

        Returns:
            QtGraphology.NodeGraphMenu: menu item.
        """
        return self._menus.get(name)

    def get_command(self: Self, name: str) -> NodeGraphCommand | None:
        """
        Returns the child menu command by name.

        Args:
            name (str): name of the command.

        Returns:
            QtGraphology.NodeGraphCommand: context menu command.
        """
        return self._commands.get(name) or None

    def add_menu(self: Self, name: str) -> NodeGraphMenu:
        """
        Adds a child menu to the current menu.

        Args:
            name (str): menu name.

        Returns:
            QtGraphology.NodeGraphMenu: the appended menu item.
        """
        if name in self._menus:
            raise NodeMenuError('menu object "{}" already exists!'.format(name))
        graph_menu: NodeGraphMenu = NodeGraphMenu(self._graph, self.qmenu)
        self.qmenu.addMenu(graph_menu)
        menu: NodeGraphMenu = NodeGraphMenu(self._graph, graph_menu)
        self._menus[name] = menu
        self._items.append(menu)
        return menu

    @staticmethod
    def _set_shortcut(action: NodeGraphAction, shortcut):
        if isinstance(shortcut, str):
            search = re.search(r"(?:\.|)QKeySequence\.(\w+)", shortcut)
            if search:
                shortcut = getattr(QtGui.QKeySequence, search.group(1))
            elif all([i in ["Alt", "Enter"] for i in shortcut.split("+")]):
                # For devs who still using PySide2, take note of this deprecation warning
                # PySideDeprecationWarningRemovedInQt6:
                # The "+" operator is deprecated in Qt For Python 6.0 . Please use "|" instead.
                #   QtCore.Qt.ALT + QtCore.Qt.Key_Return
                shortcut = QtGui.QKeySequence(
                    QtCore.Qt.ALT | QtCore.Qt.Key_Return
                )
            elif all([i in ["Return", "Enter"] for i in shortcut.split("+")]):
                shortcut = QtCore.Qt.Key_Return

        if shortcut:
            action.setShortcut(shortcut)

    def add_command(self, name, func=None, shortcut=None):
        """
        Adds a command to the menu.

        Args:
            name (str): command name.
            func (function): command function e.g. "func(``graph``)".
            shortcut (str): shortcut key.

        Returns:
            QtGraphology.NodeGraphCommand: the appended command.
        """
        action = GraphAction(name, self._graph.viewer())
        action.graph = self._graph
        if version_parse(QtCore.qVersion()) >= version_parse("5.10"):
            action.setShortcutVisibleInContextMenu(True)

        if shortcut:
            self._set_shortcut(action, shortcut)

        if func:
            action.executed.connect(func)

        self.qmenu.addAction(action)
        command = NodeGraphCommand(self._graph, action, func)
        self._commands[name] = command
        self._items.append(command)
        return command

    def add_separator(self):
        """
        Adds a separator to the menu.
        """
        self.qmenu.addSeparator()
        self._items.append(None)

class NodesMenu(NodeGraphMenu):

    def add_command(self: Self, name: str, func=None, node_type: str | None = None, node_class: type | None = None, shortcut: str | None = None) -> NodeGraphCommand:
        """
        Re-implemented to add a command to the specified node type menu.

        Args:
            name (str): command name.
            func (function): command function e.g. "func(``graph``, ``node``)".
            node_type (str): specified node type for the command.
            node_class (class): specified node class for the command.
            shortcut (str): shortcut key.

        Returns:
            QtGraphology.NodeGraphCommand: the appended command.
        """
        if not node_type and not node_class:
            raise NodeMenuError('Node type or Node class not specified!')

        if node_class:
            node_type = node_class.__name__

        node_menu = self.qmenu.get_menu(node_type)
        if not node_menu:
            node_menu = BaseMenu(node_type, self.qmenu)

            if node_class:
                node_menu.node_class = node_class
                node_menu.graph = self._graph

            self.qmenu.addMenu(node_menu)

        if not self.qmenu.isEnabled():
            self.qmenu.setDisabled(False)

        action = NodeAction(name, self._graph.viewer())
        action.graph = self._graph
        if version_parse(QtCore.qVersion()) >= version_parse("5.10"):
            action.setShortcutVisibleInContextMenu(True)

        if shortcut:
            self._set_shortcut(action, shortcut)

        if func:
            action.executed.connect(func)

        if node_class:
            node_menus = self.qmenu.get_menus(node_class)
            if node_menu in node_menus:
                node_menus.remove(node_menu)
            for menu in node_menus:
                menu.addAction(action)

        node_menu.addAction(action)
        command = NodeGraphCommand(self._graph, action, func)
        self._commands[name] = command
        self._items.append(command)
        return command

class NodeGraphCommand(object):
    """
    Node graph menu command.

    .. inheritance-diagram:: QtGraphology.NodeGraphCommand
        :parts: 1

    """

    def __init__(self: Self, graph: NodeGraph, qaction: GraphAction, func=None):
        self._graph = graph
        self._qaction = qaction
        self._name = qaction.text()
        self._func = func

    def __repr__(self):
        return '<{}("{}") object at {}>'.format(
            self.__class__.__name__, self.name(), hex(id(self)))

    @property
    def qaction(self: Self) -> GraphAction:
        """
        The underlying qaction.
        """
        return self._qaction

    @property
    def slot_function(self: Self) -> Any:
        return self._func

    def name(self: Self) -> str:
        """
        Returns the name for the menu command.

        Returns:
            str: label name.
        """
        return self._name

    def set_shortcut(self: Self, shortcut: QtGui.QKeySequence | QtCore.QKeyCombination | QtGui.QKeySequence.StandardKey | str | int) -> None:
        """
        Sets the shortcut key combination for the menu command.

        Args:
            shortcut (str): shortcut key.
        """
        self.qaction.setShortcut(shortcut)

    def run_command(self: Self) -> None:
        """
        Execute the menu command.
        """
        self.qaction.trigger()

    def set_enabled(self: Self, state: bool) -> None:
        """
        Sets the command to either be enabled or disabled.

        Args:
            state (bool): true to enable.
        """
        self.qaction.setEnabled(state)

    def set_hidden(self: Self, hidden: bool) -> None:
        """
        Sets then command item visibility in the context menu.

        Args:
            hidden (bool): true to hide the command item.
        """
        self.qaction.setVisible(not hidden)

    def show(self: Self) -> None:
        """
        Set the command to be visible in the context menu.
        """
        self.qaction.setVisible(True)

    def hide(self: Self) -> None:
        """
        Set the command to be hidden in the context menu.
        """
        self.qaction.setVisible(False)
