import requests
import random
import time
import datetime
import string
import traceback
import multiprocessing


def id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def urls():
    randomdate = (datetime.datetime.now() - datetime.timedelta(minutes = random.choice(range(1680)))).strftime("%Y%m%d%H")
    houzui = id(random.choice(range(4,6)),'123456789')
    aaa='http://www.dianmi.net/cluni'+id(random.choice(range(2,5)),'qwertyuiopasdfghjklmnbvcxz')+'/'+randomdate+id(random.choice(range(2,6)),'123456789')+'/'
    return aaa


def push(a):
    while True:
        while True:
            try:
                url=urls()
                headers={'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                 'Connection':'keep-alive',
                 'DNT':'1',
                 'Host':'api.share.baidu.com',
                 'Referer':url,
                 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
                }
                r=requests.get('http://api.share.baidu.com/s.gif?l='+url,headers=headers,timeout=19)
                print(url)
                time.sleep(random.uniform(1, 2))
                print(a)
                print(r.status_code)
                break
            except:
                traceback.print_exc()
                print('超时，继续')
                continue


if __name__ == "__main__":
    p1 = multiprocessing.Process(target = push, args = ('1',))
    p2 = multiprocessing.Process(target = push, args = ('2',))
    p3 = multiprocessing.Process(target = push, args = ('3',))
    p4 = multiprocessing.Process(target = push, args = ('4',))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
