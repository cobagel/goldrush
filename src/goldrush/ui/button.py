from collections.abc import Callable

import pyxel

from .base import BaseUI


class ButtonUI(BaseUI):
    STATE_NORMAL = "normal"
    STATE_HOVER = "hover"

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        on_click: Callable[[], None],
        bg_color: int = 5,
        text_color: int = 7,
        hover_bg_color: int = 6,
    ):
        super().__init__(x=x, y=y, width=width, height=height, visible=True)
        self.text = text
        self.on_click = on_click
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_bg_color = hover_bg_color
        self.state = self.STATE_NORMAL
        self._is_clicked = False

    def update(self) -> None:
        if not self.visible:
            return

        mouse_x = pyxel.mouse_x
        mouse_y = pyxel.mouse_y

        if self.is_point_inside(mouse_x, mouse_y):
            self.state = self.STATE_HOVER

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self._is_clicked = True
                self.on_click()
        else:
            self.state = self.STATE_NORMAL

        self._is_clicked = False

    def draw(self) -> None:
        if not self.visible:
            return

        current_bg_color = (
            self.hover_bg_color if self.state == self.STATE_HOVER else self.bg_color
        )

        pyxel.rect(self.x, self.y, self.width, self.height, current_bg_color)

        pyxel.rectb(self.x, self.y, self.width, self.height, 0)

        text_x = self.x + (self.width - len(self.text) * 4) // 2
        text_y = self.y + (self.height - 7) // 2
        pyxel.text(text_x, text_y, self.text, self.text_color)

    def handle_event(self, event: any) -> None: ...
