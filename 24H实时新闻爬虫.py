
import pandas as pd
import openpyxl 
import requests
from bs4 import BeautifulSoup

url='https://kuaixun.eastmoney.com/'
html=requests.get(url)
html.encoding='utf-8'
soup=BeautifulSoup(html.text,'lxml')

wb=openpyxl.Workbook()
ws=wb.active
ws.append(['标题'])

for time_and_title in soup.find_all(class_='livenews-media'):
    #time=time_and_title.find(class_='time').get_text()
    title=time_and_title.get_text()
    ws.append([title])
    #print(title)
wb.save(r'C:\Users\lenovo\Desktop\python练习文件\爬虫东方财富全球资讯\24H实时新闻爬虫.xlsx')  #这边的地址改成自己的保存位置即可
