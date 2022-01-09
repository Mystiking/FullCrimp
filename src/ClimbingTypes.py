from enum import Enum


class ClimbingType(Enum):
    TOPROPE = 0
    LEAD = 1
    BOULDERING = 2
    HOME_WALL = 3


class ClimbingGym(Enum):
    BLOCKS_AND_WALLS = 0
    BETA_BOULDERS_WEST = 1
    BETA_BOULDERS_SOUTH = 2
    BOULDERS_SYDHAVNEN = 3
    OUTSIDE = 4
    HOME = 5


class BetaBouldersGrade(Enum):
    CYAN = 'cyan'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'
    ORANGE = 'orange'
    RED = 'red'
    BLACK = 'black'
