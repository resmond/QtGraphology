"""
This type stub file was generated by pyright.
"""

from PySide6 import QtWidgets

class NodeScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=...) -> None:
        ...

    def __repr__(self): # -> str:
        ...

    def drawBackground(self, painter, rect): # -> None:
        ...

    def mousePressEvent(self, event): # -> None:
        ...

    def mouseMoveEvent(self, event): # -> None:
        ...

    def mouseReleaseEvent(self, event): # -> None:
        ...

    def viewer(self): # -> QGraphicsView | None:
        ...

    @property
    def grid_mode(self): # -> int:
        ...

    @grid_mode.setter
    def grid_mode(self, mode=...): # -> None:
        ...

    @property
    def grid_color(self): # -> tuple[Literal[45], Literal[45], Literal[45]]:
        ...

    @grid_color.setter
    def grid_color(self, color=...): # -> None:
        ...

    @property
    def background_color(self): # -> tuple[Literal[35], Literal[35], Literal[35]]:
        ...

    @background_color.setter
    def background_color(self, color=...): # -> None:
        ...
