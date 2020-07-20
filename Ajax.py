import sys
import random
import re
import requests
from fake_useragent import UserAgent

def getPage(url,headers,formdata):
    request = requests.post(url,formdata,headers = headers,verify = False)
    print(request.text)

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list?"
    headers = {
        "User-Agent":UserAgent().chrome
        }
    formdata = {
        "type":"24",
        "interval_id":"100:90",
        "action":"",
        "start":"0",
        "limit":"20"
    }
    getPage(url,headers,formdata)