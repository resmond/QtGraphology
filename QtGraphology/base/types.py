from __future__ import annotations
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict
from typing import Any

Kwargs = dict[str, Any]
class TSDGraph(TypedDict):
    acyclic: bool
    pipe_style: int
    pipe_slicing: bool
    pipe_collision: bool
    layout_direction: int
    accept_connection_types: dict
    reject_connection_types: dict

T_PORTS = dict[str, dict[str, list[str]]]

class TSDNode(TypedDict):
    pos: tuple[int, int]  # Actually tuple[int, int]
    icon: str | None
    name: str
    color: tuple[int]  # tuple[int, int, int, int]
    type_: str
    width: float
    height: float
    custom: dict
    visible: bool
    disabled: bool
    selected: bool
    text_color: tuple[int, int, int, int]  # tuple[int, int, int, int]
    border_color: tuple[int, int, int, int]  # tuple[int, int, int, int]
    layout_direction: int
    input_ports: NotRequired[T_PORTS]
    output_ports: NotRequired[T_PORTS]
    subgraph_session: dict
    port_deletion_allowed: bool

TSDConnections = TypedDict(
    "TSDConnections",
    {
        "in": tuple[str,str],  # Technically tuple[str, str] but JSON so pain peko
        "out": tuple[int,int],  # tuple[int, int]
    }
)

class TSerializedData(TypedDict):
    graph: TSDGraph
    nodes: dict[str, TSDNode]
    connections: NotRequired[list[TSDConnections]]
