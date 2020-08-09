import sys
import urllib.parse

url = sys.argv[1]

content = url.split('?cookies=')[1]

content = urllib.parse.unquote(content)

cookiesAndStorage = content.split('&')

cookies = cookiesAndStorage[0]
storage = cookiesAndStorage[1]

print(cookies)
print(storage)