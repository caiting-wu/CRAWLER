#https://youtu.be/9Z9xKWfNo7k
#cookie(網站在使用者瀏覽器中存放的資料，連線時送出)https://youtu.be/BEA7F9ExiPY
import urllib.request as req
def getData(url):
    #附加 Headers(不被拒絕)
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析
    import bs4 
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    for title in titles:
        if title.a !=None:
            print(title.a.string)
    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
#抓取n頁
count=0
while count<3:
    pageURL="http://www.ptt.cc"+getData(pageURL)
    count+=1
