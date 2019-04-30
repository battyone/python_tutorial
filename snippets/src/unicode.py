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
