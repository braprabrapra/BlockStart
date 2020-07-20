import sys
import requests
import urllib
import time
import hashlib
import json
import random
import webbrowser
from fake_useragent import UserAgent

def postPage(url,formdata,headers):
    """
        postPage：模拟post请求，采用有道翻译的接口
        url：需要爬取的url
        formdata：查询请求
        headers：请求头模拟chrome
    """
    request = requests.post(url=url,data = formdata,headers = headers)
    trans_json = request.text
    trans_dic = json.loads(trans_json)
    result = trans_dic["translateResult"][0][0]["tgt"]
    print(result)

if __name__ == "__main__":
    """
        有道翻译抓包到的post请求，其中_o是反爬虫编码，需要删除
            http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
        上传到接口的json，其中i的值为需要翻译的单词
            i=python%0A&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15952332897953&sign=e422bb6a7973a875c82f1cac4530f606&ts=1595233289795&bv=7e3150ecbdf9de52dc355751b074cf60&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTlME
        有道回传过来的json，其中entries为译文
            {"translateResult":[[{"tgt":"python","src":"python"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 巨蟒；大蟒\r\n","n. （法）皮东（人名）\r\n"],"type":1}}
    """
    key = input("请输入要查询的字符串：")
    
    formdata = {
        'i': key,
        'doctype':'json',
        'keyfrom':'fanyi.web',
        'typoResult':'true',
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1520416292076',
        'sign':'41fe7ea28425a0a4ceb88ab4c8609d13',
        'version':'2.1',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'false'
    }

    url =  'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
        "User-Agent" : UserAgent().chrome
    }
    postPage(url,formdata,headers)    