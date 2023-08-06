import enum

PICKLE_DATA_FILENAME='pinyin_jyutping.pkl'

class PinyinInitials(enum.Enum):
    b  =  1
    p  =  2
    m  =  3
    f  =  4
    d  =  5
    t  =  6
    n  =  7
    l  =  8
    g  =  9
    k  = 10
    h  = 11
    j  = 12
    q  = 13
    x  = 14
    zh = 15
    ch = 16
    sh = 17
    r  = 18
    z  = 19
    c  = 20
    s  = 21
    empty = 23

class PinyinFinalGroup(enum.Enum):
    group_a = 1
    group_i = 2
    group_u = 3
    group_v = 4

# https://en.wikipedia.org/wiki/Pinyin_table
class PinyinFinals(enum.Enum):
    # group a finals
    a   =  ( 2 , PinyinFinalGroup.group_a )
    o   =  ( 3 , PinyinFinalGroup.group_a )
    e   =  ( 4 , PinyinFinalGroup.group_a )
    ai  =  ( 5 , PinyinFinalGroup.group_a )
    ei  =  ( 6 , PinyinFinalGroup.group_a )
    ao  =  ( 7 , PinyinFinalGroup.group_a )
    ou  =  ( 8 , PinyinFinalGroup.group_a )
    an  =  ( 9 , PinyinFinalGroup.group_a )
    en  =  (10 , PinyinFinalGroup.group_a )
    ang =  (11 , PinyinFinalGroup.group_a )
    eng =  (12 , PinyinFinalGroup.group_a )
    ong =  (13 , PinyinFinalGroup.group_a )
    er  =  (14 , PinyinFinalGroup.group_a, None, ['r'])
    # group i finals
    i   =  ( 1 , PinyinFinalGroup.group_i )    
    ia  =  (15 , PinyinFinalGroup.group_i )
    io  =  (16 , PinyinFinalGroup.group_i )
    ie  =  (17 , PinyinFinalGroup.group_i )
    iai =  (18 , PinyinFinalGroup.group_i )
    iao =  (19 , PinyinFinalGroup.group_i )
    iu  =  (20 , PinyinFinalGroup.group_i )
    ian =  (21 , PinyinFinalGroup.group_i )
    in_ =  (22 , PinyinFinalGroup.group_i, 'in')
    iang = (23 , PinyinFinalGroup.group_i )
    ing =  (24 , PinyinFinalGroup.group_i )
    iong = (25 , PinyinFinalGroup.group_i )
    # group u finals
    u   =  (26 , PinyinFinalGroup.group_u )
    ua  =  (27 , PinyinFinalGroup.group_u )
    uo  =  (28 , PinyinFinalGroup.group_u )
    uai =  (29 , PinyinFinalGroup.group_u )
    ui  =  (30 , PinyinFinalGroup.group_u )
    uan  = (31 , PinyinFinalGroup.group_u )
    un   = (32 , PinyinFinalGroup.group_u )
    uang = (33 , PinyinFinalGroup.group_u )
    ueng = (34 , PinyinFinalGroup.group_u )
    # group ü finals
    v   =  (35, PinyinFinalGroup.group_v, 'ü', ['u:']) # ü
    ve  =  (36, PinyinFinalGroup.group_v, 'üe', ['u:e'])
    van =  (37, PinyinFinalGroup.group_v, 'üan', ['u:an'])
    vn  =  (38, PinyinFinalGroup.group_v, 'ün')

    def __init__(self, value, final_group, override_final=None, variants=[]):
        self.val = value
        self.final_group = final_group
        self.override_final = override_final
        self.variants = variants

    def final_text(self):
        if self.override_final != None:
            return self.override_final
        return self.name

class PinyinTones(enum.Enum):
    tone_1 = (1)
    tone_2 = (2)
    tone_3 = (3)
    tone_4 = (4)
    tone_neutral = (5)

    def __init__(self, tone_number):
        self.tone_number = tone_number

VowelToneMap = {
    'a': {
        PinyinTones.tone_1: 'ā', 
        PinyinTones.tone_2: 'á', 
        PinyinTones.tone_3: 'ǎ', 
        PinyinTones.tone_4: 'à',
        PinyinTones.tone_neutral: 'a'
    },
    'o': {
        PinyinTones.tone_1: 'ō',
        PinyinTones.tone_2: 'ó',
        PinyinTones.tone_3: 'ǒ',
        PinyinTones.tone_4: 'ò',
        PinyinTones.tone_neutral: 'o'
    },
    'e': {
        PinyinTones.tone_1: 'ē',
        PinyinTones.tone_2: 'é',
        PinyinTones.tone_3: 'ě',
        PinyinTones.tone_4: 'è',
        PinyinTones.tone_neutral: 'e'
    },
    'i': {
        PinyinTones.tone_1: 'ī',
        PinyinTones.tone_2: 'í',
        PinyinTones.tone_3: 'ǐ',
        PinyinTones.tone_4: 'ì',
        PinyinTones.tone_neutral: 'i'
    },
    'u': {
        PinyinTones.tone_1: 'ū',
        PinyinTones.tone_2: 'ú',
        PinyinTones.tone_3: 'ǔ',
        PinyinTones.tone_4: 'ù',
        PinyinTones.tone_neutral: 'u'
    },
    'ü': {
        PinyinTones.tone_1: 'ǖ',
        PinyinTones.tone_2: 'ǘ',
        PinyinTones.tone_3: 'ǚ',
        PinyinTones.tone_4: 'ǜ',
        PinyinTones.tone_neutral: 'ü'
    },    

}


ALL_VOWELS = list(VowelToneMap.keys()) + ['y']

# when supplying user corrections, use this occurences value so that the result goes to the top
OCCURENCES_MAX = 10000