from collections.abc import Callable

import pyxel

from .base import BaseUI


class DialogUI(BaseUI):
    def __init__(
        self,
        width: int,
        height: int,
        title: str,
        message_lines: list[str],
        on_close: Callable[[], None] | None = None,
    ):
        x = (pyxel.width - width) // 2
        y = (pyxel.height - height) // 2
        super().__init__(x=x, y=y, width=width, height=height, visible=False)
        self.title = title
        self.message_lines = message_lines
        self.on_close = on_close

        self.button_width = 56
        self.button_height = 16
        self.button_x = self.x + (self.width - self.button_width) // 2
        self.button_y = self.y + self.height - self.button_height - 10

    def show(self) -> None:
        self.visible = True

    def hide(self) -> None:
        self.visible = False

    def update(self) -> None:
        if not self.visible:
            return

        close_requested = pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_KP_ENTER)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            close_requested = close_requested or self._is_on_close_button(
                pyxel.mouse_x, pyxel.mouse_y
            )

        if close_requested:
            self.hide()
            if self.on_close is not None:
                self.on_close()

    def draw(self) -> None:
        if not self.visible:
            return

        pyxel.rect(0, 0, pyxel.width, pyxel.height, 1)

        pyxel.rect(self.x, self.y, self.width, self.height, 0)
        pyxel.rectb(self.x, self.y, self.width, self.height, 7)

        title_x = self.x + (self.width - len(self.title) * 4) // 2
        pyxel.text(title_x, self.y + 10, self.title, 10)

        text_y = self.y + 28
        for line in self.message_lines:
            line_x = self.x + (self.width - len(line) * 4) // 2
            pyxel.text(line_x, text_y, line, 7)
            text_y += 10

        pyxel.rect(
            self.button_x, self.button_y, self.button_width, self.button_height, 5
        )
        pyxel.rectb(
            self.button_x, self.button_y, self.button_width, self.button_height, 7
        )
        label = "OK"
        label_x = self.button_x + (self.button_width - len(label) * 4) // 2
        label_y = self.button_y + (self.button_height - 7) // 2
        pyxel.text(label_x, label_y, label, 7)

    def handle_event(self, event: any) -> None: ...

    def _is_on_close_button(self, x: int, y: int) -> bool:
        return (
            self.button_x <= x < self.button_x + self.button_width
            and self.button_y <= y < self.button_y + self.button_height
        )
