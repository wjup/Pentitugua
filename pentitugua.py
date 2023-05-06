#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import re
import random
from corpwechatbot.app import AppMsgSender
from bs4 import BeautifulSoup

serverchan_key = os.environ["SERVERCHAN_KEY"]
corp_id        = os.environ["CORP_ID"]
corp_secret    = os.environ["CORP_SECRET"]
agent_id       = os.environ["AGENT_ID"]

if __name__ == '__main__':
    # 获取文章列表
    # req = requests.get('https://www.dapenti.com/blog/blog.asp?subjectid=70&name=xilei')
    req = requests.get('https://www.dapenti.com/blog/index.asp')
    req.encoding = 'gbk'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    title_list = bf.find_all('div', class_='center_title_down')[0]
    bf2 = BeautifulSoup(str(title_list), 'html.parser')

    # 获取最新文章标题
    title = bf2.find_all(title=re.compile(u'喷嚏图卦'))[0]
    print(title.get('title'))

    # 文章链接
    url = 'https://www.dapenti.com/blog/' + title.get('href')
    print(url)

    # 正文
    req = requests.get(url)
    req.encoding = 'gbk'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    html = bf.find_all('table', style='table-layout:fixed;word-break:break-all;', class_='ke-zeroborder')[0]

    # 随机选择一张图片作为文章封面
    img_list = bf.find_all('img')
    img_list_len = len(img_list)
    random_index = random.randint(0, img_list_len - 1)
    cover_img_url = bf.find_all('img')[random_index].get('src')
    print(cover_img_url)

    # 下载封面
    r = requests.get(cover_img_url)
    with open('cover_img', 'wb') as f:
        f.write(r.content)

    # 推送到企业微信
    if corp_id != "" and corp_secret != "" and agent_id != "":
        # 配置企业微信推送密钥
        app = AppMsgSender(corpid=corp_id,          # 你的企业id
                           corpsecret=corp_secret,  # 你的应用凭证密钥
                           agentid=agent_id)

        # 推送到企业微信
        app.send_mpnews(title=title.get('title'),
                        image_path='cover_img',
                        content=str(html),
                        content_source_url=url,
                        author='铂程斋',
                        digest='每天一图卦，让我们更清楚地了解这个世界')

    # 推送到Server酱
    if serverchan_key != "":
        # TODO

    # 删除封面
    os.remove('cover_img')