from bs4 import BeautifulSoup
from time import sleep
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

slp=5
url='https://www.imovirtual.com/comprar/'
cookies='//*[@id="onetrust-accept-btn-handler"]'
wdriver=r'C:\Users\M\py_jupyter\os\GitHub-Repository\Bruno-H-Neves\DataMining\chromedriver.exe'
driver = webdriver.Chrome(executable_path=wdriver)
driver.get(url)
sleep(slp)
cook=driver.find_element_by_xpath(cookies)
cook.click()
sleep(slp)
content=driver.page_source
site= BeautifulSoup(content,'html.parser')
sleep(slp)
imo=[]

produtos=site.find_all('div',attrs={'class':'offer-item-details'})
for idx,produto in enumerate(produtos):
    tipologia=produto.find('span',attrs={'class':'offer-item-title'}).text
    link=produto.find('a')['href']
    area=produto.find('strong',attrs={'class':'visible-xs-block'}).text
    Tiponeg=produto.find('span',attrs={'class':'hidden-xs'}).text
    local=produto.find('p',attrs={'class':'text-nowrap'}).text
    preco=produto.find('li',attrs={'class':'offer-item-price'}).text
    preco=str(re.sub('[^0-9]', '',preco))+'€'
    imovel=[tipologia,area,Tiponeg,local,preco,link]
    imo.append(imovel)

print('nº de imoveis',len(imo))

Imodf=pd.DataFrame(imo,columns=['tipologia','area','Tiponeg','local','preco','link'])
print(Imodf)
Imodf.to_csv(r'C:\Users\M\py_jupyter\os\GitHub-Repository\Bruno-H-Neves\DataMining\imovirtual.csv', index=False)