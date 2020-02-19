from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests as re

driver = webdriver.Chrome()     # 打开 Chrome 浏览器
driver.get('https://www.104.com.tw/jobs/search/?keyword=%E8%A1%8C%E9%8A%B7%E4%BC%81%E5%8A%83&jobsource=n_my104_search_h')

#applyJobBtn
def inster_ID(username,passWord):
    driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").click()
    
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)

    driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
    return    


############ 主程式

a  = str(input('請搜尋想要找尋工作'))


headers = {'user-agent': 'Mozilla/1.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
search=re.get(f"https://www.104.com.tw/jobs/search/?keyword={a}&order=1&jobsource=2019indexpoc&ro=0",headers)
search.encoding = 'utf-8'
soup = BeautifulSoup(search.text,'lxml')

jobap_links = soup.select('h2 > a')

for jobap_link in jobap_links:
    
    apply_page = jobap_link.get('href')
    
    apply_pages = 'https:'+apply_page
    print(apply_pages)
    driver = webdriver.Chrome()
    driver.get(apply_pages)
    username = str('J122795936')
    passWord = str('s2380215')
    inster_ID(username,passWord)
    
    # while 1:
    #     start = time.clock()
    #     time.sleep(10)
    #     try:
    #         driver.find_element_by_xpath('//input[@value="取消關閉"]').submit
    #         print ('已定位到元素')
    #         print('已經投遞過了')
            
    #         end=time.clock()
    #         driver.quit()
    #         break
    #     except:
                
    #             print ("还未定位到元素!")
               
        # else:
    while 1:
        start = time.clock()
 
        try:
            
            driver.find_element_by_xpath('//input[@id="resumeList0"]').click()
            
            end=time.clock()
            break
        except:ㄋ
            
            print ("还未定位到元素!")
    while 1:
        start = time.clock()
 
        try:
            
            driver.find_element_by_xpath('//input[@id="btSend"]').click()
            
            end=time.clock()
            break
        except:
            
            print ("还未定位到元素!")
print ('定位耗费时间：'+str(end-start)) 
driver.quit()   