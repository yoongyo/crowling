import openpyxl
from selenium import webdriver as wd
import time


blog_list = []

wb = openpyxl.load_workbook('list.xlsm')

ws = wb.active
for i in ws.rows:
    blog_list.append(i[1].value)

# driver = wd.Chrome('./chromedriver')
dirver = wd.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.naver.com')
time.sleep(60)

for i in blog_list:
    driver.get(i)
