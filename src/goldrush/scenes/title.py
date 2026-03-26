import pyxel

from ..constants import (
    COLOR_TEXT,
    COLOR_TITLE,
    PROMPT_BLINK_INTERVAL,
    SCENE_HOME,
    WINDOW_HEIGHT,
)
from .base import BaseScene


class TitleScene(BaseScene):
    TITLE_TEXT = "G O L D R U S H"
    PROMPT_TEXT = "- PRESS ENTER TO START -"

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene_manager.change(SCENE_HOME)

    def draw(self) -> None:
        title_y = WINDOW_HEIGHT // 3
        self.draw_centered_text(title_y, self.TITLE_TEXT, COLOR_TITLE)
        if pyxel.frame_count % PROMPT_BLINK_INTERVAL < PROMPT_BLINK_INTERVAL // 2:
            prompt_y = WINDOW_HEIGHT // 2 + 20
            self.draw_centered_text(prompt_y, self.PROMPT_TEXT, COLOR_TEXT)

    def on_enter(self, **kwargs) -> None:
        pass

    def on_exit(self) -> None:
        pass
