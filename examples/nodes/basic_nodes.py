from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Self, Any

from QtGraphology import BaseNode, BaseNodeCircle


class BasicNodeA(BaseNode):
    """
    A node class with 2 inputs and 2 outputs.
    """

    # unique node identifier.
    __identifier__: str = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'node A'

    def __init__(self: Self) -> None:
        super(BasicNodeA, self).__init__()

        # create node inputs.
        self.add_input(name='in A')
        self.add_input(name='in B')

        # create node outputs.
        self.add_output(name='out A')
        self.add_output(name='out B')


class BasicNodeB(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__: str = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'node B'

    def __init__(self) -> None:
        super(BasicNodeB, self).__init__()

        # create node inputs
        self.add_input(name='single 1')
        self.add_input(name='single 2')
        self.add_input(name='multi in', multi_input=True)

        # create node outputs
        self.add_output(name='single 1', multi_output=False)
        self.add_output(name='single 2', multi_output=False)
        self.add_output(name='multi out')


class CircleNode(BaseNodeCircle):
    """
    A node class with 3 inputs and 3 outputs.
    This node is a circular design.
    """

    # unique node identifier.
    __identifier__: str = 'nodes.basic'

    # initial default node name.
    NODE_NAME = 'Circle Node'

    def __init__(self: Self) -> None:
        super(CircleNode, self).__init__()
        self.set_color(r=10, g=24, b=38)

        # create node inputs
        p = self.add_input(name='in 1')
        p.add_accept_port_type(
            port_name='single 1',
            port_type='out',
            node_type='nodes.basic.BasicNodeB'
        )

        self.add_input(name='in 2')
        self.add_input(name='in 3', multi_input=True)
        self.add_input(name='in 4', display_name=False)
        self.add_input(name='in 5', display_name=False)

        # create node outputs
        self.add_output(name='out 1')
        self.add_output(name='out 2', multi_output=False)
        self.add_output(name='out 3', multi_output=True, display_name=False)
        self.add_output(name='out 4', multi_output=True, display_name=False)
