import requests
import time

def getHtmlText(url):
   try:
       r = requests.get(url, timeout=30)
       r.raise_for_status()
       r.encoding = r.apparent_encoding
       return r.text
   except:
       return '运行异常'
if  __name__ == "__main__":
    start = time.perf_counter()
    totaltime = 0
    url = "http://www.stat-nba.com/player/1717.html"
    for i in range(10):
        time.sleep(0.5)
        starttime = time.perf_counter()
        getHtmlText(url)
        endtime = time.perf_counter()
        print('第{0}次爬取，用时{1:.4f}秒'.format(i + 1, endtime - starttime))
        totaltime = totaltime + endtime - starttime
    print('总共用时{:.4f}秒'.format(totaltime))


