#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/10 0010 17:55
# @Author  : liya
# @Site    : 
# @File    : dataSource.py
import sys
import json
import requests


def getData(index):
    reload(sys)
    sys.setdefaultencoding('utf8')

    payload = {'page': str(index), 'submit': '1', 'nav': 'tm', 'cate': '0', 'sort': 'zh', 'starttime': '0', 'inajax': '1'}
    url = 'http://fmgrgg.agent.yqjuejin.com'
    cookies = dict(sid='3iu0c8gq0lk52dph0ne6rfu2h2')
    headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
               'Cookie': 'sid=3iu0c8gq0lk52dph0ne6rfu2h2', 'Host': 'fmgrgg.agent.yqjuejin.com',
               'Pragma': 'no-cache',
               'Referer': 'http://fmgrgg.agent.yqjuejin.com/?page=1&submit=1&nav=tm&cate=0&sort=zh&starttime=0&end=pc',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest'}
    html = requests.get(url, params=payload, cookies=cookies, headers=headers)
    jsons = json.loads(html.text)
    jsonss = jsons['list']

    param = []
    for jsonhh in jsonss:
        itemId = str(jsonhh['itemId']).encode("utf-8")
        link = str(jsonhh['link']).encode("utf-8")
        title = str(jsonhh['title']).encode("utf-8")
        subtitle = str(jsonhh['subtitle']).encode("utf-8")
        intro = str(jsonhh['intro']).encode("utf-8")
        imagePath = str(jsonhh['imagePath']).encode("utf-8")
        staticImgPath = str(jsonhh['staticImgPath']).encode("utf-8")
        imagePaths = str(jsonhh['imagePaths']).encode("utf-8")
        sellPrice = str(jsonhh['sellPrice']).encode("utf-8")
        price = str(jsonhh['price']).encode("utf-8")
        itemUrl = str(jsonhh['itemUrl']).encode("utf-8")
        descUrl = str(jsonhh['descUrl']).encode("utf-8")
        planUrl = str(jsonhh['planUrl']).encode("utf-8")
        ulandUrl = str(jsonhh['ulandUrl']).encode("utf-8")
        historySales = str(jsonhh['historySales']).encode("utf-8")
        viewCount = str(jsonhh['viewCount']).encode("utf-8")
        sellerId = str(jsonhh['sellerId']).encode("utf-8")
        sellerType = str(jsonhh['sellerType']).encode("utf-8")
        sellerName = str(jsonhh['sellerName']).encode("utf-8")
        flagShip = str(jsonhh['flagShip']).encode("utf-8")
        certIcon = str(jsonhh['certIcon']).encode("utf-8")
        cpId = str(jsonhh['cpId']).encode("utf-8")
        cpPrice = str(jsonhh['cpPrice']).encode("utf-8")
        cpSpare = str(jsonhh['cpSpare']).encode("utf-8")
        cpCount = str(jsonhh['cpCount']).encode("utf-8")
        cpTotal = str(jsonhh['cpTotal']).encode("utf-8")
        cpCondition = str(jsonhh['cpCondition']).encode("utf-8")
        cpLimit = str(jsonhh['cpLimit']).encode("utf-8")
        cpStarts = str(jsonhh['cpStarts']).encode("utf-8")
        cpExpired = str(jsonhh['cpExpired']).encode("utf-8")
        cpLevel = str(jsonhh['cpLevel']).encode("utf-8")
        cpUrl = str(jsonhh['cpUrl']).encode("utf-8")
        gold = str(jsonhh['gold']).encode("utf-8")
        ju = str(jsonhh['ju']).encode("utf-8")
        qiang = str(jsonhh['qiang']).encode("utf-8")
        freeExpress = str(jsonhh['freeExpress']).encode("utf-8")
        freeExpressBack = str(jsonhh['freeExpressBack']).encode("utf-8")
        commission = str(jsonhh['commission']).encode("utf-8")
        cgold = str(jsonhh['cgold']).encode("utf-8")
        goodRatePercentage = str(jsonhh['goodRatePercentage']).encode("utf-8")
        dx = str(jsonhh['dx']).encode("utf-8")
        is_brand = str(jsonhh['is_brand']).encode("utf-8")

        param.append([
            itemId, link, title, subtitle, intro, imagePath, staticImgPath, imagePaths, sellPrice, price, itemUrl,
            descUrl,
            planUrl,
            ulandUrl, historySales, viewCount, sellerId, sellerType, sellerName, flagShip, certIcon, cpId, cpPrice,
            cpSpare,
            cpCount, cpTotal, cpCondition, cpLimit, cpStarts, cpExpired, cpLevel, cpUrl, gold, ju, qiang,
            freeExpress,
            freeExpressBack, commission, cgold, goodRatePercentage, dx, is_brand])

    return param
