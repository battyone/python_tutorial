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
