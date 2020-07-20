import requests
import sys
from fake_useragent import UserAgent
import random
import webbrowser

url = "https://www.baidu.com"

request = requests.get(url,UserAgent().chrome)

type = sys.getfilesystemencoding()

request.encoding = type

webbrowser.open(url)

print(request.text)