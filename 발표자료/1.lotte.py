from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def getLotteStoreInfo(result):


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome('./발표자료/chromedriver.exe', options=options) 

    lotte_url = 'https://www.lotteon.com/p/lotteplus/offlinestore/offLineStoreInfo?mall_no=4'
    wd.get(lotte_url)
    time.sleep(0.3)


    for i in range(2,114):
        wd.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/div[1]/div/ul/li[1]/button').click()
        time.sleep(1)
        wd.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[2]/div[2]/div/table/tr[{i}]/td[1]/a').click()
        time.sleep(1)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        store_name = soup.select('div.branchTitle > div.storeName')[0].string.strip()
        print(store_name)
        store_address = soup.select('div.branchInfo > div.content')[0].string
        print(store_address)
        store_tell = soup.select('div.content > a')[0].string
        print(store_tell)
        wd.find_element(By.XPATH,'//*[@id="modals-container"]/div/div/div[2]/div/button').click()
        time.sleep(1)
        result.append([store_name]+[store_address]+[store_tell])


def main():
    result = []
    print('롯마 매장 크롤링 >>>')
    getLotteStoreInfo(result)

   

    columns = ['store','address','phone']
    lottemart_df= pd.DataFrame(result, columns=columns)
    lottemart_df.to_csv('./topmart_shop_info.csv',index=True, encoding='utf-8')
   
    print('저장완료')



if __name__ == '__main__':
    main()