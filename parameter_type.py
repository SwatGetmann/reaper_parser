from enum import Enum, unique, auto

@unique
class ParameterType(Enum):
    
    TEXT = auto()
    
    # Project
    RIPPLE = auto()
    GROUPOVERRIDE = auto()
    AUTOXFADE = auto()
    ENVATTACH = auto()
    POOLEDENVATTACH = auto()
    MIXERUIFLAGS = auto()
    PEAKGAIN = auto()
    FEEDBACK = auto()
    PANLAW = auto()
    PROJOFFS = auto()
    MAXPROJLEN = auto()
    GRID = auto()
    TIMEMODE = auto()
    VIDEO_CONFIG = auto()
    PANMODE = auto()
    CURSOR = auto()
    ZOOM = auto()
    VZOOMEX = auto()
    USE_REC_CFG = auto()
    RECMODE = auto()
    SMPTESYNC = auto()
    LOOP = auto()
    LOOPGRAN = auto()
    RECORD_PATH = auto()
    
    RENDER_FILE = auto()
    RENDER_FMT = auto()
    RENDER_1X = auto()
    RENDER_RANGE = auto()
    RENDER_RESAMPLE = auto()
    RENDER_ADDTOPROJ = auto()
    RENDER_STEMS = auto()
    RENDER_DITHER = auto()
    RENDER_PATTERN = auto()
    
    TIMELOCKMODE = auto()
    TEMPOENVLOCKMODE = auto()
    ITEMMIX = auto()
    DEFPITCHMODE = auto()
    TAKELANE = auto()
    SAMPLERATE = auto()
    LOCK = auto()
    
    GLOBAL_AUTO = auto()
    TEMPO = auto()
    PLAYRATE = auto()
    SELECTION = auto()
    SELECTION2 = auto()
    MASTERAUTOMODE = auto()
    MASTERTRACKHEIGHT = auto()
    MASTERPEAKCOL = auto()
    MASTERMUTESOLO = auto()
    MASTERTRACKVIEW = auto()
    MASTERHWOUT = auto()
    MASTER_NCH = auto()
    MASTER_VOLUME = auto()
    MASTER_FX = auto()
    MASTER_SEL = auto()
    MARKER = auto()
    
    # ScreenSet
    POS = auto()
    MASK = auto()
    CURSORPOS = auto()
    SCROLLX = auto()
    SCROLLY = auto()
    TRACKSCALE = auto()
    VZOOM = auto()
    
    # Metronome
    VOL = auto()
    FREQ = auto()
    BEATLEN = auto()
    SAMPLES = auto()
    PATTERN = auto()
    
    # Masterfxlist
    WNDRECT = auto()
    SHOW = auto()
    LASTSEL = auto()
    DOCKED = auto()
    
    # POOLEDENV
    ID = auto()
    NAME = auto()
    SRCLEN = auto()
    LFO = auto()
    PPT = auto()
    
    # MASTERPLAYSPEEDENV
    EGUID = auto()
    ACT = auto()
    VIS = auto()
    LANEHEIGHT = auto()
    ARM = auto()
    DEFSHAPE = auto()
    POOLEDENVINST = auto()
    PT = auto()
    
    # TRACK
    # NAME - 67
    PEAKCOL = auto()
    BEAT = auto()
    AUTOMODE = auto()
    VOLPAN = auto()
    MUTESOLO = auto()
    IPHASE = auto()
    PLAYOFFS = auto()
    ISBUS = auto()
    BUSCOMP = auto()
    SHOWINMIX = auto()
    FREEMODE = auto()
    SEL = auto()
    REC = auto()
    VU = auto()
    TRACKHEIGHT = auto()
    INQ = auto()
    NCHAN = auto()
    FX = auto()
    TRACKID = auto()
    PERF = auto()
    MIDIOUT = auto()
    MAINSEND = auto()
    FILE = auto()
    
    # FX Chain
    BYPASS = auto()
    PRESETNAME = auto()
    
    # VST
    FLOATPOS = auto()
    FXID = auto()
    WAK = auto()
    
    # ITEM
    POSITION = auto()
    SNAPOFFS = auto()
    LENGTH = auto()
    ALLTAKES = auto()
    FADEIN = auto()
    FADEOUT = auto()
    MUTE = auto()
    IGUID = auto()
    IID = auto()
    SOFFS = auto()
    CHANMODE = auto()
    GUID = auto()
    RECPASS = auto()
    
    # MIDI
    HASDATA = auto()
    CCINTERP = auto()
    POOLEDEVTS = auto()
    E = auto()
    e = auto()
    CHASE_CC_TAKEOFFS = auto()
    IGNTEMPO = auto()
    SRCCOLOR = auto()
    VELLANE = auto()
    CFGEDITVIEW = auto()
    KEYSNAP = auto()
    TRACKSEL = auto()
    EVTFILTER = auto()
    CFGEDIT = auto()
    
    # SWSCOLOR
    SWSCOLOR_ID = auto()
    
    # list is not full. more will be coming soon