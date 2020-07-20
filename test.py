# 无反爬
import urllib.parse
import urllib.request
import json


content = input('请输入需要翻译的词语：')

# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
    'i': content,
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


# 转换格式
data = urllib.parse.urlencode(data).encode('utf-8')
# 发送请求，带data就是post，不带data是get
response = urllib.request.urlopen(url,data)
# 转码
html = response.read().decode('utf-8')

ta = json.loads(html)  # json.loads()用于将str类型的数据转成dict。#参考 Json模块dumps、loads、dump、load函数介绍
print(ta['translateResult'][0][0]['tgt'])