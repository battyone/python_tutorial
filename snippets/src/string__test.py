# %%
from datetime import datetime

# %%

alphabet = ''.join([chr(c) for c in range(ord('a'), ord('z')+1)])
shifted = alphabet[2:] + alphabet[:2]
translation = str.maketrans(alphabet, shifted)

s1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr''q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
s2 = s1.translate(translation)

print(s2)

s1 = 'map'
s2 = s1.translate(translation)
print(s2)

# http://www.pythonchallenge.com/pc/def/ocr.html

# %%
# f string format
f = 13.45678983762
print(f'{f:.3f}')

# %%
a = 42
# print binary
print(f'{a:b}')

# print percent
print(f'{2/3:.1%}')

# %%
now = datetime.now()
print(f'{now:%H:%M:%S}')
print(f'It is now {now:%I:%M %p}')

# %%
# multiline
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)
            ''')

# %%
# Center the string around a bunch of 'o's
print(f'Hello World'.center(50, 'o', ))


# %%
