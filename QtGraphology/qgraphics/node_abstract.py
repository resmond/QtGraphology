#!/usr/bin/python
from PySide6 import QtCore, QtWidgets
from typing import Dict, Any, List, Tuple, Optional, Union, cast, TYPE_CHECKING, Self

from QtGraphology.constants import *
from QtGraphology.widgets.viewer import NodeViewer, NodeScene

class AbstractNodeItem(QtWidgets.QGraphicsItem):
    """
    A base class for node graphics items in Qt applications with support for node-based workflows.

    This class provides the foundation for creating interactive node items that can be used in
    node graph interfaces. It handles common node functionality such as selection, movement,
    appearance styling, and sizing. The class manages a properties dictionary that stores
    node attributes like color, name, and state.

    AbstractNodeItem is designed to be subclassed for specific node types, with common
    functionality already implemented. Subclasses should implement at minimum the `draw_node()`
    method to define the node's appearance.

    Inherits:
        QtWidgets.QGraphicsItem: Base Qt class for custom graphics items in a QGraphicsScene

    Attributes:
        _properties (dict): Dictionary containing node properties including:
            - id: Unique identifier for the node
            - type_: String identifier for the node type
            - name: Display name of the node
            - color: Main node color as RGBA tuple (r, g, b, a)
            - border_color: Border color as RGBA tuple
            - text_color: Text color as RGBA tuple
            - layout_direction: Direction of the node layout (horizontal/vertical)
            - selected: Boolean indicating if the node is selected
            - disabled: Boolean indicating if the node is disabled
            - visible: Boolean indicating if the node is visible

        _width (float): Width of the node
        _height (float): Height of the node

        The base class of all node qgraphics item.
    """

    def __init__(self: Self, name: str = 'node', parent: Optional[QtWidgets.QGraphicsItem] = None) -> None:
        super().__init__(parent=parent)
        self.setFlags(self.GraphicsItemFlag.ItemIsSelectable | self.GraphicsItemFlag.ItemIsMovable)
        self.setCacheMode(ITEM_CACHE_MODE)
        self.setZValue(Z_VAL_NODE)
        self._properties: TPROPERTIES = {
            'id': None,
            'type_': 'AbstractBaseNode',
            'name': name.strip(),
            'color': (13, 18, 23, 255),
            'border_color': (46, 57, 66, 255),
            'text_color': (255, 255, 255, 180),
            'selected': False,
            'disabled': False,
            'visible': False,
            'layout_direction': LayoutDirectionEnum.HORIZONTAL,
            'identifier': None,  # Adding missing property referenced in getter/setter
        }
        self._width: float = NodeEnum.WIDTH.value
        self._height: float = NodeEnum.HEIGHT.value

    def __repr__(self: Self) -> str:
        return f'{self.__module__}.{self.__class__.__name__}(\'{self.name}\')'

    def boundingRect(self: Self) -> QtCore.QRectF:
        return QtCore.QRectF(0.0, 0.0, self._width, self._height)

    def mousePressEvent(self: Self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        """
        Re-implemented to update "self._properties['selected']" attribute.

        Args:
            event (QtWidgets.QGraphicsSceneMouseEvent): mouse event.
        """
        self._properties['selected'] = True
        super().mousePressEvent(event)

    def setSelected(self: Self, selected: bool) -> None:
        self._properties['selected'] = selected
        super().setSelected(selected)

    def draw_node(self: Self) -> None:
        """
        Re-draw the node item in the scene with proper
        calculated size and widgets aligned.

        (this is called from the builtin custom widgets.)
        """
        return

    def pre_init(self: Self, viewer: NodeViewer, pos: Optional[TPOSITION] = None) -> None:
        """
        Called before node has been added into the scene.

        Args:
            viewer (QtGraphology.widgets.viewer.NodeViewer): main viewer.
            pos (tuple): the cursor pos if node is called with tab search.
        """
        return

    def post_init(self: Self, viewer: NodeViewer, pos: Optional[TPOSITION] = None) -> None:
        """
        Called after node has been added into the scene.

        Args:
            viewer (QtGraphology.widgets.viewer.NodeViewer): main viewer
            pos (tuple): the cursor pos if node is called with tab search.
        """
        return

    @property
    def id(self: Self) -> TPROPERTY:
        return self._properties['id']

    @id.setter
    def id(self: Self, unique_id: Any = '') -> None:
        self._properties['id'] = unique_id

    @property
    def type_(self: Self) -> TPROPERTY:
        return self._properties['type_']

    @type_.setter
    def type_(self: Self, node_type: str = 'NODE') -> None:
        self._properties['type_'] = node_type

    @property
    def layout_direction(self: Self) -> TPROPERTY:
        return self._properties['layout_direction']

    @layout_direction.setter
    def layout_direction(self: Self, value: LayoutDirectionEnum = LayoutDirectionEnum.HORIZONTAL) -> None:
        self._properties['layout_direction'] = value

    @property
    def size(self: Self) -> TSIZE:
        return (self._width, self._height)

    @property
    def width(self: Self) -> float:
        return self._width

    @width.setter
    def width(self: Self, width: float = 0.0) -> None:
        self._width = width

    @property
    def height(self: Self) -> float:
        return self._height

    @height.setter
    def height(self: Self, height: float = 0.0) -> None:
        self._height = height

    @property
    def color(self: Self) -> TCOLOR:
        return cast(Tuple[int, int, int, int], self._properties['color'])

    @color.setter
    def color(self: Self, color: TCOLOR = (0, 0, 0, 255)) -> None:
        self._properties['color'] = color

    @property
    def text_color(self: Self) -> TCOLOR:
        return cast(Tuple[int, int, int, int], self._properties['text_color'])

    @text_color.setter
    def text_color(self: Self, color: TCOLOR = (100, 100, 100, 255)) -> None:
        self._properties['text_color'] = color

    @property
    def border_color(self: Self) -> TCOLOR:
        return cast(Tuple[int, int, int, int], self._properties['border_color'])

    @border_color.setter
    def border_color(self: Self, color: TCOLOR = (0, 0, 0, 255)) -> None:
        self._properties['border_color'] = color

    @property
    def disabled(self: Self) -> bool:
        return cast(bool, self._properties['disabled'])

    @disabled.setter
    def disabled(self: Self, state: bool = False) -> None:
        self._properties['disabled'] = state

    @property
    def selected(self: Self) -> bool:
        if self._properties['selected'] != self.isSelected():
            self._properties['selected'] = self.isSelected()
        return cast(bool, self._properties['selected'])

    @selected.setter
    def selected(self: Self, selected: bool = False) -> None:
        self.setSelected(selected)

    @property
    def visible(self: Self) -> bool:
        return cast(bool, self._properties['visible'])

    @visible.setter
    def visible(self: Self, visible: bool = False) -> None:
        self._properties['visible'] = visible
        self.setVisible(visible)

    @property
    def xy_pos(self: Self) -> TPOSITION:
        """
        return the item scene postion.
        ("node.pos" conflicted with "QGraphicsItem.pos()"
        so it was refactored to "xy_pos".)

        Returns:
            list[float]: x, y scene position.
        """
        return [float(self.scenePos().x()), float(self.scenePos().y())]

    @xy_pos.setter
    def xy_pos(self: Self, pos: Optional[List[float]] = None) -> None:
        """
        set the item scene postion.
        ("node.pos" conflicted with "QGraphicsItem.pos()"
        so it was refactored to "xy_pos".)

        Args:
            pos (list[float]): x, y scene position.
        """
        pos = pos or [0.0, 0.0]
        self.setPos(pos[0], pos[1])

    @property
    def name(self: Self) -> str:
        return cast(str, self._properties['name'])

    @name.setter
    def name(self: Self, name: str = '') -> None:
        self._properties['name'] = name
        self.setToolTip('node: {}'.format(name))

    @property
    def identifier(self) -> Any:
        return self._properties['identifier']

    @identifier.setter
    def identifier(self: Self, ident: str = '') -> None:
        self._properties['identifier'] = ident

    @property
    def properties(self) -> TPROPERTIES:
        """
        return the node view attributes.

        Returns:
            dict: {property_name: property_value}
        """
        props: TPROPERTIES = {'width': self.width,'height': self.height, 'pos': self.xy_pos}
        props.update(self._properties)

        return props

    def viewer(self) -> Optional[NodeViewer]:
        """
        return the main viewer.

        Returns:
            QtGraphology.widgets.viewer.NodeViewer: viewer object.
        """
        if self.scene():
            return self.scene.viewer() # type: ignore

    def delete(self) -> None:
        """
        remove node view from the scene.
        """
        if self.scene():
            self.scene().removeItem(self)

    def from_dict(self, node_dict: Dict[str, Any]) -> None:
        """
        set the node view attributes from the dictionary.

        Args:
            node_dict (dict): serialized node dict.
        """
        node_attrs = list(self._properties.keys()) + ['width', 'height', 'pos']
        for name, value in node_dict.items():
            if name in node_attrs:
                # "node.pos" conflicted with "QGraphicsItem.pos()"
                # so it's refactored to "xy_pos".
                if name == 'pos':
                    name = 'xy_pos'
                setattr(self, name, value)
