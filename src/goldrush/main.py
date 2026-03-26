from .constants import SCENE_HOME, SCENE_TITLE
from .core.engine import Engine
from .core.scene_mgr import SceneManager
from .scenes.home import HomeScene
from .scenes.title import TitleScene


def main():
    engine = Engine()

    scene_manager = SceneManager()

    scene_manager.register(SCENE_TITLE, TitleScene)
    scene_manager.register(SCENE_HOME, HomeScene)
    scene_manager.change(SCENE_TITLE)

    engine.run(scene_manager)
