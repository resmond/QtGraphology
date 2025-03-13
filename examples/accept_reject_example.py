from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Self, Any

import signal

from PySide6 import QtWidgets

from QtGraphology import BaseNode, NodeGraph
from QtGraphology.constants import PortTypeEnum
from QtGraphology.qgraphics.node_base import NodeItem


class PublishWriteNodeItem(NodeItem):
    def _align_widgets_horizontal(self, v_offset: int):
        if not self._widgets:
            return

        rect = self.boundingRect()
        y = rect.y() + v_offset
        for widget in self._widgets.values():
            if not widget.isVisible():
                continue

            widget_rect = widget.boundingRect()
            x = rect.center().x() - (widget_rect.width() / 2)
            widget.widget().setTitleAlign('center')
            widget.setPos(x, y)
            y += widget_rect.height()


class PrevNextNode(BaseNode):
    __identifier__ = "action"
    NODE_NAME = "Action Node"

    def __init__(self):
        super().__init__()

        # create an input port.
        input_port = self.add_input("_prev", color=(180, 80, 0), multi_input=False)
        # create an output port.
        output_port = self.add_output("_next", multi_output=False)

        input_port.port_item.set_allow_partial_match_constraint(True)
        input_port.port_item.set_accept_constraint(
            port_name=output_port.name(),
            port_type=PortTypeEnum.OUT.value,
            node_identifier=self.__identifier__,
        )

        output_port.port_item.set_allow_partial_match_constraint(True)
        output_port.port_item.set_accept_constraint(
            port_name=input_port.name(),
            port_type=PortTypeEnum.IN.value,
            node_identifier=self.__identifier__,
        )


class IngredientNode(BaseNode):
    __identifier__ = "ingredient"


class SpamNode(IngredientNode):
    __identifier__ = "spam"
    NODE_NAME = "Spam"

    def __init__(self):
        super().__init__()
        spam_port = self.add_output(
            "spam",
            color=(50, 150, 222),
        )


class EggNode(IngredientNode):
    __identifier__ = "egg"
    NODE_NAME = "Egg"

    def __init__(self):
        super().__init__()
        egg_port = self.add_output(
            "egg",
            color=(50, 150, 222),
        )


class MealNode(BaseNode):
    NODE_NAME = "Meal"

    def __init__(self):
        super().__init__()
        spam_port = self.add_input("spam", color=(222, 15, 0), multi_input=False)
        spam_port.port_item.set_reject_constraint(
            port_name="egg",
            port_type=PortTypeEnum.OUT.value,
            node_identifier="egg",
        )
        egg_port = self.add_input("egg", color=(222, 15, 0), multi_input=False)
        egg_port.port_item.set_reject_constraint(
            port_name="spam",
            port_type=PortTypeEnum.OUT.value,
            node_identifier="spam",
        )


class BasePublishNode(PrevNextNode):
    __identifier__ = "publish"
    allow_multiple_write = False

    def __init__(self):
        super().__init__()
        port = self.add_output(
            "write",
            color=(184, 150, 0),
            multi_output=self.allow_multiple_write,
        )
        port.port_item.set_accept_constraint(
            port_name="src",
            port_type=PortTypeEnum.IN.value,
            node_identifier="publish",
        )


class PubNode(PrevNextNode):
    __identifier__ = "pub"
    NODE_NAME = "Not Tavern"


class PublishFileActionNode(BasePublishNode):
    NODE_NAME = "Publish File"
    allow_multiple_write = False


class PublishFileToManyActionNode(BasePublishNode):
    NODE_NAME = "Publish File to Many"
    allow_multiple_write = True


class PublishWriteNode(BaseNode):
    __identifier__ = "publish"
    NODE_NAME = "Publish Write"

    def __init__(self):
        super().__init__(qgraphics_item=PublishWriteNodeItem)
        self.set_color(164, 130, 0)
        self.add_text_input("write", "Path:")

        port = self.add_input("src", multi_input=False)
        port.port_item.set_accept_constraint(
            port_name="write",
            port_type=PortTypeEnum.OUT.value,
            node_identifier="publish",
        )


if __name__ == '__main__':

    # handle SIGINT to make the app terminate on CTRL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QtWidgets.QApplication([])

    # create graph controller.
    graph = NodeGraph()

    # set up context menu for the node graph.
    graph.set_context_menu_from_file('./examples/hotkeys/hotkeys.json')

    # registered example nodes.
    graph.register_nodes([
        SpamNode,
        EggNode,
        MealNode,
        PubNode,
        PublishFileActionNode,
        PublishFileToManyActionNode,
        PublishWriteNode,
    ])

    # add nodes
    graph.add_node(SpamNode())
    graph.add_node(EggNode())
    graph.add_node(MealNode())
    graph.add_node(PubNode())
    graph.add_node(PublishFileToManyActionNode())
    graph.add_node(PublishFileActionNode())
    graph.add_node(PublishWriteNode())
    graph.auto_layout_nodes()
    graph.clear_selection()

    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()

    app.exec_()
