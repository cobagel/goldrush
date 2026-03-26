import pyxel

from ..constants import COLOR_TEXT, SCENE_TITLE, WINDOW_HEIGHT
from .base import BaseScene


class HomeScene(BaseScene):
    TITLE_TEXT = "HOME"
    PROMPT_TEXT = "PRESS BACKSPACE TO RETURN"

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.scene_manager.change(SCENE_TITLE)

    def draw(self) -> None:
        y = WINDOW_HEIGHT // 2
        self.draw_centered_text(y, self.TITLE_TEXT, COLOR_TEXT)
        self.draw_centered_text(y + 16, self.PROMPT_TEXT, COLOR_TEXT)

    def on_enter(self, **kwargs) -> None:
        pass

    def on_exit(self) -> None:
        pass
