from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests as re

# driver = webdriver.Chrome()     # 打开 Chrome 浏览器

a  = str(input('請搜尋想要找尋工作'))
page = 1
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
    # driver.refresh()
    #applyJobBtn
    driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").send_keys(Keys.ENTER)
    window_1=driver.current_window_handle
    windows=driver.window_handles
    print(windows)  #輸入控制代碼集合
    for current_window in windows:   #切換視窗
        if current_window != window_1:
            driver.switch_to.window(current_window)
    
    
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)
    time.sleep(1)#網頁仔入中

    driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
    time.sleep(4)#網頁仔入中
    print('網頁載入中')
    i=0
    while 1:
        start = time.clock()
 
        try:
            
            driver.find_element_by_xpath('//input[@id="resumeList0"]').click()
            
            end=time.clock()
            break
        except:
            
            print ("还未定位到元素!")
            i+=1
            if i ==50:
                print('已經有了歐')
                # driver.find_element_by_xpath('//input[@value="取消關閉"]').submit()
                driver.quit()
                break
            end=time.clock()
    print ('定位耗费时间：'+str(end-start))

    # driver.find_element_by_xpath('//input[@id="resumeList0"]').click()

    while 1:
        start = time.clock()
        try:
            
            driver.find_element_by_xpath('//input[@id="btSend"]').click()
            print ('已定位到元素')
            end=time.clock()
            driver.quit()
            break
        except:
            print ("还未定位到元素!")
            
            i+=1
            if i ==5:
                    print('找不到歐')
                    
                    end=time.clock()
                    break
        break
    
    print ('定位耗费时间：'+str(end-start))
    
    

    