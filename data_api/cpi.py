#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import collections as cl

APP_ID = 'bfa52112516f3710f695113038b92d0d8df2456d'
API_URL = 'http://api.e-stat.go.jp/rest/2.1/app/json/getStatsData?appId=bfa52112516f3710f695113038b92d0d8df2456d&lang=J&statsDataId=0003143513&surveyYears=200001-201612'

if __name__ == "__main__":
    # APIを呼び出してレスポンスオブジェクトを得る
    response = requests.get(API_URL)

    # response.bodyは jsonとみなしパース済み。パース前の内容が欲しければ raw_bodyを使う
    print (response)

    ys = cl.OrderedDict()
    fw = open('data2.json','w')
    json.dump(response.json(),fw,indent=2)



