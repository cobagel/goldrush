import pyxel

from ..constants import COLOR_TEXT, COLOR_TITLE, SCENE_HOME
from ..ui.dialog import DialogUI
from .base import BaseScene


class StageMapScene(BaseScene):
    TITLE_TEXT = "STAGE MAP"

    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.dialog = DialogUI(
            width=176,
            height=94,
            title="STAGE MAP",
            message_lines=["NOTHING HERE YET"],
        )

    def update(self) -> None:
        if self.dialog.visible:
            self.dialog.update()
            return

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.dialog.show()

        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.scene_manager.change(SCENE_HOME)

    def draw(self) -> None:
        self.draw_centered_text(40, self.TITLE_TEXT, COLOR_TITLE)
        self.draw_centered_text(60, "PRESS ENTER", COLOR_TEXT)
        self.draw_centered_text(232, "BACKSPACE: HOME", COLOR_TEXT)
        self.dialog.draw()

    def on_enter(self, **kwargs) -> None:
        pyxel.mouse(True)
        self.dialog.show()

    def on_exit(self) -> None:
        pass
