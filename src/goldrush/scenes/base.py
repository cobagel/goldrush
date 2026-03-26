from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import pyxel

from ..constants import FONT_CHAR_WIDTH, WINDOW_WIDTH

if TYPE_CHECKING:
    from ..core.scene_mgr import SceneManager


class BaseScene(ABC):
    def __init__(self, scene_manager: SceneManager):
        self.scene_manager = scene_manager

    @abstractmethod
    def update(self) -> None: ...

    @abstractmethod
    def draw(self) -> None: ...

    @abstractmethod
    def on_enter(self, **kwargs) -> None: ...

    @abstractmethod
    def on_exit(self) -> None: ...

    def center_text_x(self, text: str) -> int:
        return (WINDOW_WIDTH - len(text) * FONT_CHAR_WIDTH) // 2

    def draw_centered_text(self, y: int, text: str, color: int) -> None:
        pyxel.text(self.center_text_x(text), y, text, color)
