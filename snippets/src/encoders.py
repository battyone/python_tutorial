# %%
from unicodedata import normalize


# %%

# ascii cannot be used here since it cannot encode 'ñ'
for codec in ['latin-1', 'utf-8', 'utf-16', 'cp1252']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# %%
# ways to deal with UnicodeEncodeError
print('El Niño'.encode('ascii', errors='ignore'), sep='\t')
print('El Niño'.encode('ascii', errors='replace'), sep='\t')
print('El Niño'.encode('ascii', errors='xmlcharrefreplace'), sep='\t')


# %%
# ways to deal with UnicodeEncodeError
octets = b'Montr\xe9al'  # latin1 encoding
print(octets.decode('utf8', errors='ignore'))
print(octets.decode('utf8', errors='replace'))
print()

# correct decoding
print('correct: ', octets.decode('latin-1'), sep='\t')

# %%
# import chardet
# use this lib to identify what the encoding is for a file


# %%

s1 = 'café'
s2 = 'cafe\u0301'  # decomposed 'e' and acute accent

# looks the same
print(s1, s2)

# but len is different
print(len(s1), len(s2))

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
