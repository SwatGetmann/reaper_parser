from enum import Enum

class ParameterType(Enum):
    TEXT = 1
    
    # Project
    RIPPLE = 2
    GROUPOVERRIDE = 3
    AUTOXFADE = 4
    ENVATTACH = 5
    POOLEDENVATTACH = 6
    MIXERUIFLAGS = 7
    PEAKGAIN = 8
    FEEDBACK = 9
    PANLAW = 10
    PROJOFFS = 11
    MAXPROJLEN = 12
    GRID = 13
    TIMEMODE = 14
    VIDEO_CONFIG = 15
    PANMODE = 16
    CURSOR = 17
    ZOOM = 18
    VZOOMEX = 19
    USE_REC_CFG = 20
    RECMODE = 21
    SMPTESYNC = 22
    LOOP = 23
    LOOPGRAN = 24
    RECORD_PATH = 25
    RENDER_FILE = 26
    RENDER_FMT = 27
    RENDER_1X = 28
    RENDER_RANGE = 29
    RENDER_RESAMPLE = 30
    RENDER_ADDTOPROJ = 31
    RENDER_STEMS = 32
    RENDER_DITHER = 33
    TIMELOCKMODE = 34
    TEMPOENVLOCKMODE = 35
    ITEMMIX = 36
    DEFPITCHMODE = 37
    TAKELANE = 38
    SAMPLERATE = 39
    LOCK = 40
    
    GLOBAL_AUTO = 41
    TEMPO = 42
    PLAYRATE = 43
    SELECTION = 44
    SELECTION2 = 45
    MASTERAUTOMODE = 46
    MASTERTRACKHEIGHT = 47
    MASTERPEAKCOL = 48
    MASTERMUTESOLO = 49
    MASTERTRACKVIEW = 50
    MASTERHWOUT = 51
    MASTER_NCH = 52
    MASTER_VOLUME = 53
    MASTER_FX = 54
    MASTER_SEL = 55
    MARKER = 56
    
    # Metronome
    VOL = 57
    FREQ = 58
    BEATLEN = 59
    SAMPLES = 60
    PATTERN = 61
    
    # Masterfxlist
    WNDRECT = 62
    SHOW = 63
    LASTSEL = 64
    DOCKED = 65
    
    # POOLEDENV
    ID = 66
    NAME = 67
    SRCLEN = 68
    LFO = 69
    PPT = 70
    
    # MASTERPLAYSPEEDENV
    EGUID = 71
    ACT = 72
    VIS = 73
    LANEHEIGHT = 74
    ARM = 75
    DEFSHAPE = 76
    
    # TRACK
    # NAME - 67
    PEAKCOL = 77
    BEAT = 78
    AUTOMODE = 79
    VOLPAN = 80
    MUTESOLO = 81
    IPHASE = 82
    PLAYOFFS = 83
    ISBUS = 84
    BUSCOMP = 85
    SHOWINMIX = 86
    FREEMODE = 87
    SEL = 88
    REC = 89
    VU = 90
    TRACKHEIGHT = 91
    INQ = 92
    NCHAN = 93
    FX = 94
    TRACKID = 95
    PERF = 96
    MIDIOUT = 97
    MAINSEND = 98
    
    # list is not full. more will be coming soon