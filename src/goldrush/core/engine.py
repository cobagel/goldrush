from typing import TYPE_CHECKING

import pyxel

from ..constants import CLS_COLOR, FPS, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH

if TYPE_CHECKING:
    from .scene_mgr import SceneManager


class Engine:
    def __init__(self):
        pyxel.init(
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            title=WINDOW_TITLE,
            fps=FPS,
            quit_key=pyxel.KEY_ESCAPE,
        )

        self.scene_manager: SceneManager | None = None

    def run(self, scene_manager: SceneManager) -> None:
        self.scene_manager = scene_manager
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if self.scene_manager:
            self.scene_manager.update()

    def draw(self) -> None:
        pyxel.cls(CLS_COLOR)
        if self.scene_manager:
            self.scene_manager.draw()
