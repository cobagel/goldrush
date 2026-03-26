import pyxel

from ..constants import (
    COLOR_TEXT,
    COLOR_TITLE,
    SCENE_CHARACTERS,
    SCENE_SETTINGS,
    SCENE_STAGE_MAP,
    SCENE_TITLE,
    WINDOW_WIDTH,
)
from ..ui.button import ButtonUI
from .base import BaseScene


class HomeScene(BaseScene):
    TITLE_TEXT = "HOME"
    PROMPT_TEXT = "SELECT MENU"

    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        button_width = 180
        button_height = 34
        gap = 12
        top_y = 68
        button_x = (WINDOW_WIDTH - button_width) // 2

        self.buttons = [
            ButtonUI(
                button_x,
                top_y,
                button_width,
                button_height,
                "Character",
                lambda: self.scene_manager.change(SCENE_CHARACTERS),
                bg_color=3,
                hover_bg_color=11,
            ),
            ButtonUI(
                button_x,
                top_y + button_height + gap,
                button_width,
                button_height,
                "Stage Map",
                lambda: self.scene_manager.change(SCENE_STAGE_MAP),
                bg_color=4,
                hover_bg_color=9,
            ),
            ButtonUI(
                button_x,
                top_y + (button_height + gap) * 2,
                button_width,
                button_height,
                "Settings",
                lambda: self.scene_manager.change(SCENE_SETTINGS),
                bg_color=2,
                hover_bg_color=10,
            ),
        ]

    def update(self) -> None:
        for button in self.buttons:
            button.update()

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.scene_manager.change(SCENE_TITLE)

    def draw(self) -> None:
        self.draw_centered_text(24, self.TITLE_TEXT, COLOR_TITLE)
        self.draw_centered_text(38, self.PROMPT_TEXT, COLOR_TEXT)

        for button in self.buttons:
            button.draw()

        self.draw_centered_text(232, "BACKSPACE: TITLE", COLOR_TEXT)

    def on_enter(self, **kwargs) -> None:
        pyxel.mouse(True)

    def on_exit(self) -> None:
        pass
