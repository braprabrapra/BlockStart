import requests
import sys
import urllib
import random
import webbrowser
from fake_useragent import UserAgent

def loadPage(url,filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename：处理的文件名
    """
    print("正在下载" + filename)
    request = requests.get(url,UserAgent().chrome)
    type = sys.getfilesystemencoding()
    request.encoding = type
    writePage(request.text,filename)

def writePage(html,filename):
    """
        作用：将html内容写入到本地
        html：服务器响应文件内容
    """
    print("正在保存" + filename)    
    with open(filename,"w",encoding='utf-8') as f:
        f.write(html)
    print("-" * 30)

def tiebaSpider(url,beginPage,endPage):
    """
        作用：贴吧爬虫调度器
        url:贴吧url前部分
        beginPage:起始页
        endPage:结束页
    """
    for page in range(beginPage,endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        filename = "第" + str(page) + "页.html"
        loadPage(fullurl,filename)

if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名：")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页码："))
    url = "http://tieba.baidu.com/f?kw=" 
    key = urllib.parse.quote(kw)
    url = url + str(key)
    tiebaSpider(url,beginPage,endPage)