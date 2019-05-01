# %%
import unicodedata
import string
import re

# %%
from unicodedata import name
s = 'café'
print(s)
print(len(s))

# encode into bytes
b = s.encode('utf8')
print(b)
print(len(s))

c = b'caf\xc3\xa9'
t = c.decode('utf8')
print(t)

# The Euro sign
print(b'\xe2\x82\xac'.decode('utf8'))

# %%
cafe = bytes('café', encoding='utf_8')


# %%
symbols = '$¢£¥€¤'
codes = [ord(s) for s in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]


# %%

a = {chr(i): name(chr(i))
     for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(a)

# %%


def shave_marks(txt):
    """Remove all diacritic marks"""

    # Decompose all characters into base characters and combining marks
    norm_txt = unicodedata.normalize('NFD', txt)

    # Filter out all combining marks
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))

    # Recompose all characters
    return unicodedata.normalize('NFC', shaved)


def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin based characters"""

    norm_txt = unicodedata.normalize('NFD', txt)

    latin_base = False
    keepers = []

    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on latin base char

        keepers.append(c)

        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)

    return unicodedata.normalize('NFC', shaved)


txt = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

# only the letters ç í è were replaced
print(shave_marks(txt))

greek = 'Ζέφυρος, Zéfiro'
print(shave_marks(greek))

# Build mapping table for char-to-char replacement
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",
                           """'f"*^<''""---~>""")

# Build mapping table for char-to-string replacement
multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)


def dewinize(txt):
    """Replace Win1252 symbols with ASCII characters chars or sequences"""
    return txt.translate(multi_map)


def asciize(txt):

    no_marks = shave_marks_latin(dewinize(txt))

    no_marks = no_marks.replace('ß', 'ss')

    return unicodedata.normalize('NFKC', no_marks)


txt = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(asciize(txt))


# %%
re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char),
          sep='\t')

# %%

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))
print('  bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print('  str  :', re_words_str.findall(text_str))
print('  bytes:', re_words_bytes.findall(text_bytes))
