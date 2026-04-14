timeout_ms = 50

fingers = [ 1,  2,  3,  4,  5,      6,  7,  8,  9, 10, 11,\
           13, 14, 15, 16, 17,     18, 19, 20, 21, 22, 23,\
           25, 26, 27, 28, 29,     30, 31, 32, 33, 34, 35\
           ]
left_thumb  = 37
right_thumb = 40

base_origins = [\
 'Q', 'W',   'E',   'R',   'T',         'Y',   'U',   'I',   'O', 'P',  '',\
 'A', 'S',   'D',   'F',   'G',         'H',   'J',   'K',   'L',  '',  '',\
 'Z', 'X',   'C',   'V',   'B',         'N',   'M',    '',    '',  '',  ''\
 ]
print(len(base_origins))

base_macros = [\
 'JPPERIOD', 'KA',   'TA',   'KO',   'SA',         'RA',   'TI',   'KU',   'TU',   'JPCOMMA2',  'JPCOMMA1',\
 'U',        'SI',   'TE',   'KE',   'SE',         'HA',   'TO',   'KI',   'I',    'NN',        'JPBACKSPACE',\
 'JPTEN',    'HI',   'SU',   'HU',   'HE',         'ME',   'SO',   'NE',   'HO',   'JPNAKATEN', 'JPEN'\
 ]
print(len(base_macros))

left_macros = [\
 'XA',       'E',        'RI',       'XYA',      'RE',            'PA',       'DI',       'GU',       'DU',       'PI',        'NONE',\
 'WO',       'A',        'NA',       'XYU',      'MO',            'BA',       'DO',       'GI',       'PO',       'NONE',      'NONE',\
 'XU',       'JPMINUS2', 'RO',       'YA',       'XI',            'PU',       'ZO',       'PE',       'BO',       'NONE',      'NONE'\
 ]
print(len(left_macros))

right_macros = [\
 'NONE',     'GA',       'DA',       'GO',       'ZA',            'YO',       'NI',       'RU',       'MA',       'XE',        'NONE',\
 'VU',       'JI',       'DE',       'GE',       'ZE',            'MI',       'O',        'NO',       'XYO',      'XTU',       'NONE',\
 'NONE',     'BI',       'ZU',       'BU',       'BE',            'NU',       'YU',       'MU',       'WA',       'XO',        'NONE'\
 ]
print(len(right_macros))

base_bindings =[\
('PERIOD',),     ('K','A'),  ('T','A'), ('K','O'), ('S','A'),     ('R','A'), ('T','I'), ('K','U'), ('T','U'), ('COMMA',), ('COMMA',),\
('U',),          ('S', 'I'), ('T','E'), ('K','E'), ('S','E'),     ('H','A'), ('T','O'), ('K','I'), ('I',),     ('N','N'),     ('BACKSPACE',),\
('PERIOD',), ('H','I'),  ('S','U'), ('H','U'), ('H','E'),     ('M','E'), ('S','O'), ('N','E'), ('H','O'), ('SLASH',),     ('LA(BACKSLASH)',)\
]
print(len(base_bindings))

left_bindings = [\
('X','A'),  ('E',),         ('R','I'),  ('X','Y','A'),  ('R','E'),        ('P','A'),     ('D','I'),     ('G','U'),   ('D','U'),   ('P','I'),     ('NONE'),\
('W','O'),  ('A',),         ('N','A'),  ('X','Y','U'),  ('M','O'),        ('B','A'),     ('D','O'),     ('G','I'),   ('P','O'),   ('NONE'),      ('NONE'),\
('X','U'),  ('MINUS',),     ('R','O'),  ('Y','A'),      ('X','I'),        ('P','U'),     ('Z','O'),     ('P','E'),   ('B','O'),   ('NONE'),      ('NONE')\
]
print(len(left_bindings))

right_bindings = [\
('NONE'),   ('G','A'),      ('D','A'),  ('G','O'), ('Z','A'),        ('Y','O'),     ('N','I'),     ('R','U'),   ('M','A'),     ('X','E'),     ('NONE'),\
('V','U'),  ('J','I'),      ('D','E'),  ('G','E'), ('Z','E'),        ('M','I'),     ('O',),        ('N','O'),   ('X','Y','O'), ('X','T','U'), ('NONE'),\
('NONE'),   ('B','I'),      ('Z','U'),  ('B','U'), ('B','E'),        ('N','U'),     ('Y','U'),     ('M','U'),   ('W','A'),     ('X','O'),     ('NONE')\
]
print(len(right_bindings))


def write_combo(fingers, thumb, macros):
    if len(fingers) == len(macros):
        for finger, macro in zip(fingers, macros):
            if macro != 'NONE':
                f.write('\tcombo_' + macro + ' {\n')
                f.write('\t\ttimeout-ms = <' + str(timeout_ms) + '>;\n')
                f.write('\t\tkey-positions = <' + str(finger) + ' ' + str(thumb) + '>;\n')
                f.write('\t\tlayers = <1>;\n')
                f.write('\t\tbindings = <&macro_' + macro + '>;\n')
                f.write('\t};\n\n')
            else:
                pass
    else:
        print('length is not equal at combo.')

path_w = 'combos.keymap'
with open(path_w, mode='w') as f:
    #f.write('combos {\n')
    #f.write('\tcompatible = "zmk,combos";\n\n')
    write_combo(fingers, left_thumb,  left_macros)
    write_combo(fingers, right_thumb, right_macros)
    #f.write('};')

def write_behavior(macros, bases):
    for macro, base in zip(macros, bases):
        if macro != 'NONE' and base != '':
            f.write('mm_' + macro + ': mm_' + macro + '{\n')
            f.write('compatible = "zmk,behavior-mod-morph";\n')
            f.write('label = "MOD_MORPH' + macro + '";\n')
            f.write('#binding-cells = <0>;\n')
            f.write('bindings = <&macro_' + macro + '>, <&kp ' + base + '>;\n')
            f.write('mods = <(MOD_LCTL|MOD_RCTL|MOD_LGUI|MOD_RGUI|MOD_LALT|MOD_RALT)>;\n')
            f.write('keep-mods = <(MOD_LCTL|MOD_RCTL|MOD_LGUI|MOD_RGUI|MOD_LALT|MOD_RALT)>;\n')
            f.write('};\n\n')

path_w = 'behaviors.keymap'
with open(path_w, mode='w') as f:
    #f.write('behaviors {\n')
    #f.write('\tcompatible = "zmk,behavior-mod-morph";\n\n')
    write_behavior(base_macros, base_origins)
    #f.write('};')

def write_ime_on_macro():
    f.write('macro_IMEON: macro_IMEON{\n')
    f.write('compatible = "zmk,behavior-macro";\n')
    f.write('label = "macro_IMEON";\n')
    f.write('#binding-cells = <0>;\n')
    f.write('bindings = <&kp INT2>, <&to 1>;\n')
    f.write('};\n\n')

def write_ime_off_macro():
    f.write('macro_IMEOFF: macro_IMEOFF{\n')
    f.write('compatible = "zmk,behavior-macro";\n')
    f.write('label = "macro_IMEOFF";\n')
    f.write('#binding-cells = <0>;\n')
    f.write('bindings = <&kp INT5>, <&to 0>;\n')
    f.write('};\n\n')

def write_macro(macros, bindings):
    if len(macros) == len(bindings):
        for macro, binding in zip(macros, bindings):
            if macro != 'NONE' and binding != 'NONE' and binding != 'YET':
                # print(bindcing)
                # print(macro)
                # print(binding)
                f.write('macro_' + macro + ': macro_' + macro + '{\n')
                f.write('compatible = "zmk,behavior-macro";\n')
                f.write('label = "macro_' + macro + '";\n')
                f.write('#binding-cells = <0>;\n')
                f.write('bindings = <&to 0>, ')
                for i,s in enumerate(binding):
                    if i == 0:
                        f.write('<&kp ' + s + '>')
                    else:
                        f.write(', <&kp ' + s + '>')
                f.write(', <&to 1>;\n')
                f.write('};\n\n')
            elif (macro != 'NONE' and binding == 'NONE') or (macro == 'NONE' and binding != 'NONE'):
                print('macro-binding pair error.')
            else:
                pass
    else:
        print('length is not equal at macro.')


path_w = 'macros.dtsi'
with open(path_w, mode='w') as f:
    write_ime_on_macro()
    write_ime_off_macro()
    write_macro(base_macros, base_bindings)
    write_macro(left_macros, left_bindings)
    write_macro(right_macros, right_bindings)
