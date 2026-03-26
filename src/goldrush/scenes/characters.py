import pyxel

from ..constants import COLOR_TEXT, COLOR_TITLE, SCENE_HOME, WINDOW_WIDTH
from ..ui.button import ButtonUI
from ..ui.dialog import DialogUI
from .base import BaseScene


class CharactersScene(BaseScene):
    TITLE_TEXT = "CHARACTERS"

    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.character_names = ["RED", "BLUE", "YELLOW"]

        button_width = 160
        button_height = 22
        gap = 8
        top_y = 72
        button_x = (WINDOW_WIDTH - button_width) // 2

        self.buttons = []
        for index, name in enumerate(self.character_names):
            self.buttons.append(
                ButtonUI(
                    button_x,
                    top_y + (button_height + gap) * index,
                    button_width,
                    button_height,
                    name,
                    lambda n=name: self.open_character_dialog(n),
                    bg_color=5,
                    hover_bg_color=11,
                )
            )

        self.dialog = DialogUI(
            width=184,
            height=98,
            title="CHARACTER",
            message_lines=["NOTHING HERE YET"],
        )

    def open_character_dialog(self, name: str) -> None:
        self.dialog.title = name
        self.dialog.message_lines = ["NO ENHANCEMENT YET"]
        self.dialog.show()

    def update(self) -> None:
        if self.dialog.visible:
            self.dialog.update()
            return

        for button in self.buttons:
            button.update()

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.scene_manager.change(SCENE_HOME)

    def draw(self) -> None:
        self.draw_centered_text(22, self.TITLE_TEXT, COLOR_TITLE)
        self.draw_centered_text(38, "SELECT A CHARACTER", COLOR_TEXT)

        for button in self.buttons:
            button.draw()

        self.draw_centered_text(232, "BACKSPACE: HOME", COLOR_TEXT)
        self.dialog.draw()

    def on_enter(self, **kwargs) -> None:
        pyxel.mouse(True)
        self.dialog.hide()

    def on_exit(self) -> None:
        pass
