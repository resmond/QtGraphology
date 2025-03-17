#!/usr/bin/python
from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Self, Any
from PySide6 import QtCore, QtWidgets, QtGui


from QtGraphology.constants import ViewerEnum
from QtGraphology.base import NodeGraph, AbstractNodeItem

class BaseMenu(QtWidgets.QMenu):

    def __init__(self: Self, *args, **kwargs: dict[str, Any]) -> None:
        super(BaseMenu, self).__init__(*args, **kwargs)
        # text_color = self.palette().text().color().getRgb()
        text_color  = tuple(map(lambda i, j: i - j, (255, 255, 255), ViewerEnum.BACKGROUND_COLOR.value))
        selected_color = self.palette().highlight().color().getRgb()
        style_dict = {
            'QMenu': {
                'color': 'rgb({0},{1},{2})'.format(*text_color),
                'background-color': 'rgb({0},{1},{2})'.format(
                    *ViewerEnum.BACKGROUND_COLOR.value
                ),
                'border': '1px solid rgba({0},{1},{2},30)'.format(*text_color),
                'border-radius': '3px',
            },
            'QMenu::item': {
                'padding': '5px 18px 2px',
                'background-color': 'transparent',
            },
            'QMenu::item:selected': {
                'color': 'rgb({0},{1},{2})'.format(*text_color),
                'background-color': 'rgba({0},{1},{2},200)'
                                    .format(*selected_color),
            },
            'QMenu::item:disabled': {
                'color': 'rgba({0},{1},{2},60)'.format(*text_color),
                'background-color': 'rgba({0},{1},{2},200)'
                .format(*ViewerEnum.BACKGROUND_COLOR.value),
            },
            'QMenu::separator': {
                'height': '1px',
                'background': 'rgba({0},{1},{2}, 50)'.format(*text_color),
                'margin': '4px 8px',
            }
        }
        stylesheet: str = ''
        for css_class, css in style_dict.items():
            style = f'{css_class} {{\n'
            for elm_name, elm_val in css.items():
                style += f'  {elm_name}:{elm_val};\n'
            style += f'}}\n'
            stylesheet += style
        self.setStyleSheet(stylesheet)
        self.node_class: type | None = None
        self.graph: NodeGraph | None = None

    # disable for issue #142
    # def hideEvent(self, event):
    #     super(BaseMenu, self).hideEvent(event)
    #     for a in self.actions():
    #         if hasattr(a, 'node_id'):
    #             a.node_id = None

    def get_menu(self: Self, name: str, node_id: str) -> BaseMenu | None:
        for action in self.actions():
            menu: BaseMenu = action.menu() # type: ignore
            if not menu:
                continue
            if menu.title() == name:
                return menu
            if node_id and menu.node_class:
                node: AbstractNodeItem = menu.graph.get_node_by_id(node_id) # type: ignore
                if isinstance(node, menu.node_class):
                    return menu

    def get_menus(self: Self, node_class: type) -> list[BaseMenu]:
        menus: list[BaseMenu] = []
        for action in self.actions():
            menu: BaseMenu = action.menu()  # type: ignore
            if menu.node_class:
                if issubclass(menu.node_class, node_class):
                    menus.append(menu)
        return menus


class GraphAction(QtGui.QAction):

    executed = QtCore.Signal(object)

    def __init__(self: Self, *args, **kwargs: dict[str, Any]) -> None:
        super(GraphAction, self).__init__(*args, **kwargs)
        self.graph: NodeGraph | None = None
        self.qmenu: QtWidgets.QMenu | None = None
        self.triggered.connect(self._on_triggered)

    def _on_triggered(self: Self):
        self.executed.emit(self.graph)

    def get_action(self: Self, name: str) -> QtGui.QAction | None:
        if not self.qmenu:
            return None

        for action in self.qmenu.actions():
            if not action.menu() and action.text() == name:
                return action
        return None


class NodeAction(GraphAction):

    executed = QtCore.Signal(object, object)

    def __init__(self: Self, *args, **kwargs: dict[str, Any]) -> None:
        super(NodeAction, self).__init__(*args, **kwargs)
        self.node_id = None

    def _on_triggered(self: Self) -> None:
        if not self.graph:
            return

        node = self.graph.get_node_by_id(self.node_id)
        self.executed.emit(self.graph, node)
