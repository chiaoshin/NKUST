# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:57:21 2022

@author: User
"""
import json
with open("lightrail.json",encoding = 'utf8') as file:
    data = json.load(file)
    temp_list = []
    with open("final_output.json", "w", encoding='utf-8') as fout:
        for item in data:
            temp_dict = {'年':item['年'],'月':item['月'],'總運量':item['總運量']} #抓取需要的json資料
            temp_list.append(temp_dict)
        json_data = json.dumps(temp_list, ensure_ascii=False)
        fout.write(json_data)   #寫入抓取好的json資料

with open("final_output.json", encoding='utf-8') as f:
    datas = json.load(f) #讀取json檔
    for item in datas:
        print(item)     #將json格式輸出於Console上
        
# 將JSON檔轉換為csv，方便後續開啟檔案，繪製圖表展示
import csv

with open('final_output.csv','w' ,newline='') as fout:
    csvwriter = csv.writer(fout, delimiter=',')
    headers=['年','月','總運量']
    csvwriter.writerow(headers)
    with open("final_output.json", encoding='utf-8') as f:
        datas = json.load(f)
        for item in datas:
            csvwriter.writerow((item['年'],item['月'],item['總運量']))