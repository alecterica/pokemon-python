from enum import Enum

class GameState(Enum):
    NONE=0
    RUNNING=1
    ENDED=2

class GameContext(Enum):
    overworld=0
    battle=1
