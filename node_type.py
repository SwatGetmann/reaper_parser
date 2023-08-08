from enum import Enum, auto


class NodeType(Enum):
    """Class represents type of Node from Reaper Project tree.
    Basically, it's a Enum.
    """

    REAPER_PROJECT = auto()
    NOTES = auto()
    RECORD_CFG = auto()
    APPLYFX_CFG = auto()
    RENDER_CFG = auto()
    METRONOME = auto()
    MASTERFXLIST = auto()
    POOLEDENV = auto()
    MASTERPLAYSPEEDENV = auto()
    TEMPOENVEX = auto()
    SCREENSET = auto()
    SET = auto()
    PROJBAY = auto()
    TRACK = auto()
    FXCHAIN = auto()
    VST = auto()
    ITEM = auto()
    SOURCE = auto()
    EXTENSIONS = auto()
    SWSAUTOCOLOR = auto()
    SELTRACKITEMSELSTATE = auto()
    SLOT = auto()
    BR_CURSOR_POS = auto()
    PANENV = auto()
    PANENV2 = auto()
    JS = auto()
    VOLENV = auto()
    VOLENV2 = auto()

    # list is not full. more will be coming soon
