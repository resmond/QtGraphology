#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING

from .pkg_info import __version__ as VERSION
from .pkg_info import __license__ as LICENSE

from .base.graph import NodeGraph, SubGraph
from .base.menu  import NodesMenu, NodeGraphMenu, NodeGraphCommand
from .base.port  import Port
from .base.node  import NodeObject

from .nodes.base_node        import BaseNode
from .nodes.base_node_circle import BaseNodeCircle
from .nodes.backdrop_node    import BackdropNode
from .nodes.group_node       import GroupNode

# widgets
from .widgets.node_widgets import NodeBaseWidget

from .custom_widgets.nodes_tree import NodesTreeWidget
from .custom_widgets.nodes_palette import NodesPaletteWidget
from .custom_widgets.properties_bin.node_property_widgets import (
    NodePropEditorWidget,
    PropertiesBinWidget,
)

__version__ = VERSION

__all__ = [
    'BackdropNode',
    'BaseNode',
    'BaseNodeCircle',
    'GroupNode',
    'LICENSE',
    'NodeBaseWidget',
    'NodeGraph',
    'NodeGraphCommand',
    'NodeGraphMenu',
    'NodeObject',
    'NodesPaletteWidget',
    'NodesTreeWidget',
    'NodesMenu',
    'Port',
    'PropertiesBinWidget',
    'SubGraph',
    'VERSION',
    'NodesTreeWidget',
    'NodesPaletteWidget'
]
