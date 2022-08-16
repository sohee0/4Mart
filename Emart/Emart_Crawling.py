from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def getEmartInfo(result):
    #USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
    #오류 해결 방법
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    wd = webdriver.Chrome('C:/MartRepository/4Mart/Emart/chromedriver.exe', options=options)


    for i in range(1, 138+1):
        wd.get('https://store.emart.com/branch/list.do?trcknCode=header_store')
        time.sleep(0.5)
        wd.find_element(By.XPATH,'//*[@id="branchType"]/option[2]').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH,f'//*[@id="branchList"]/li[{i}]/a').click()
        time.sleep(0.5)
        


        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        store_name = soup.select('div.store-cont > div.store-intro > div.store-header > h2')[0].string
        print(store_name)

        store_address = soup.select('dl.paper-data > dd.data ')[0].string
        print(store_address)

        store_contact = soup.select('div.cont > div.intro-wrap > ul > li > p')[2].string
        print(store_contact)
        
        # wd.find_element(By.XPATH,'//*[@id="branchType"]/option[2]').click()
        # time.sleep(0.3)


        result.append([store_name]+[store_address]+[store_contact])
        

def main():
    result = []
    print('이마트 매장 크롤링 >>>')
    getEmartInfo(result)

    # 판다스 데이터프레임 생성
    columns = ['store', 'address', 'contact']
    coffebean_df = pd.DataFrame(result, columns=columns)

    # csv 저장
    coffebean_df.to_csv('./Emart_info.csv', index=True, encoding='utf-8')
    print('저장완료!')


if __name__ == '__main__':
    main()
