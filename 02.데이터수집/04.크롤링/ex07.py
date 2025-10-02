from selenium import webdriver
from bs4 import BeautifulSoup
import re, time

date = time.strftime('%Y-%m-%d %H:%M:%S')


options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.weather.go.kr/w/index.do'
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div', {'id':'weather2'})


els = local.find_all('dl', {'class':re.compile('^po_')})
print(f'[{date}]')
for el in els:
    name = el.dt.getText()
    temp = el.span.getText()
    weather = el.i.getText()
    print(name, temp, weather)
    print('-'*30)

