from enum import Enum

class NodeType(Enum):
    REAPER_PROJECT = 1
    NOTES = 2
    RECORD_CFG = 3
    APPLYFX_CFG = 4
    RENDER_CFG = 5
    METRONOME = 6
    MASTERFXLIST = 7
    POOLEDENV = 8
    MASTERPLAYSPEEDENV = 9
    TEMPOENVEX = 10
    SCREENSET = 11
    SET = 12
    PROJBAY = 13
    TRACK = 14
    FXCHAIN = 15
    VST = 16
    ITEM = 17
    SOURCE = 18
    EXTENSIONS = 19
    SWSAUTOCOLOR = 20
    SELTRACKITEMSELSTATE = 21
    SLOT = 22
    BR_CURSOR_POS = 23
    PANENV = 24
    JS = 25
    # list os not full. more will be coming soon
