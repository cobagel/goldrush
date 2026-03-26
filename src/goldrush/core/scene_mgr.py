from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..scenes.base import BaseScene


class SceneManager:
    def __init__(self):
        self._scene_classes: dict[str, type[BaseScene]] = {}
        self.current_scene: BaseScene | None = None

    def update(self) -> None:
        if self.current_scene is not None:
            self.current_scene.update()

    def draw(self) -> None:
        if self.current_scene is not None:
            self.current_scene.draw()

    def register(self, name: str, scene_class: type[BaseScene]) -> None:
        if name in self._scene_classes:
            raise ValueError(f"Scene '{name}' is already registered")
        self._scene_classes[name] = scene_class

    def change(self, name: str, **kwargs) -> None:
        if self.current_scene is not None:
            self.current_scene.on_exit()

        if name not in self._scene_classes:
            available = ", ".join(sorted(self._scene_classes))
            raise KeyError(f"Unknown scene '{name}'. Available: {available}")

        self.current_scene = self._scene_classes[name](self)
        self.current_scene.on_enter(**kwargs)
