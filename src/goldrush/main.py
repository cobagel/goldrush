from .constants import (
    SCENE_CHARACTERS,
    SCENE_HOME,
    SCENE_SETTINGS,
    SCENE_STAGE_MAP,
    SCENE_TITLE,
)
from .core.engine import Engine
from .core.scene_mgr import SceneManager
from .scenes.characters import CharactersScene
from .scenes.home import HomeScene
from .scenes.settings import SettingsScene
from .scenes.stage_map import StageMapScene
from .scenes.title import TitleScene


def main():
    engine = Engine()

    scene_manager = SceneManager()

    scene_manager.register(SCENE_TITLE, TitleScene)
    scene_manager.register(SCENE_HOME, HomeScene)
    scene_manager.register(SCENE_CHARACTERS, CharactersScene)
    scene_manager.register(SCENE_STAGE_MAP, StageMapScene)
    scene_manager.register(SCENE_SETTINGS, SettingsScene)
    scene_manager.change(SCENE_TITLE)

    engine.run(scene_manager)
