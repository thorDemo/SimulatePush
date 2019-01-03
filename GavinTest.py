# -*- coding: UTF-8 -*-
import requests
import time
from random import sample, choice, randint
from mylib.data import Data
from datetime import datetime, timedelta
from urllib import parse


def random_chars(num):
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(sample(chars, num))


def random_num(num):
    chars = '1234567890'
    return ''.join(sample(chars, num))


def random_path():
    chars = ['lsj', 'xxn', 'usb']
    return choice(chars)


def random_time():
    today = datetime.today()
    yesterday = today + timedelta(days=randint(-1, 0))
    return yesterday.strftime("%Y%m%d")


def get_url():
    domain = 'http://www.126gzw.com'
    url = '%s/%s%s%s.html' % (domain, random_path(), random_time(), random_chars(5))
    return url


data = Data()
# 将字典转为CookieJar：
cookiesJar = requests.utils.cookiejar_from_dict(data.cookie, cookiejar=None,overwrite=True)

success_count = 0
failure_count = 0
while 1:
    user_agent = choice(data.user_agent) # 获取随机UA
    referer = get_url()
    r = get_url()
    headers = {
        'User-Agent': user_agent,
        'Referer': referer,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'api.share.baidu.com',
    }

    conn = requests.Session()
    conn.headers = headers
    # 将cookiesJar赋值给会话
    conn.cookies = cookiesJar

    payload = {'r': r, 'l': referer}
    # url = 'http://api.share.baidu.com/s.gif?r=' + r + '&l=' +referer
    try:
        # res = conn.get(url,timeout=1)
        # res = conn.get('http://api.share.baidu.com/s.gif', params=payload, timeout=1, proxies=proxies)
        res = conn.get('http://api.share.baidu.com/s.gif', params=payload, timeout=1)
        success_count += 1
        url = parse.unquote(res.url)
        print('----------------------')
        print(res.status_code)
        print(url)
    except Exception as e:
        failure_count += 1
        print(e)
    print('success:%d  failure:%d'%(success_count,failure_count))
    time.sleep(0.1)
