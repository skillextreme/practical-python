import urllib.request
try:
    u = urllib.request.urlopen('httclearps://ctabustracker.com/home?stop=14791&route=22')
    data = u.read()
    print(data)
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)

