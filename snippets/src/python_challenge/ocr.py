# http://www.pythonchallenge.com/pc/def/ocr.html

import urllib.request
from collections import Counter

response = urllib.request.urlopen(
    'http://www.pythonchallenge.com/pc/def/ocr.html')

html = response.read()

b = Counter(html)
print(b)
