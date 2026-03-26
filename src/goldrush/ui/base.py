from abc import ABC, abstractmethod


class BaseUI(ABC):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        visible: bool = True,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible

    @abstractmethod
    def update(self) -> None: ...

    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def handle_event(self, event: any) -> None: ...

    def is_point_inside(self, x: int, y: int) -> bool:
        return self.x <= x < self.x + self.width and self.y <= y < self.y + self.height
