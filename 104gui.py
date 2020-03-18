from selenium import webdriver
import time
import pandas as pd
import requests as re
import os
from bs4 import BeautifulSoup

class job_apply:
    
    def __init__(self,url):
        # headlessmode

        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.option.add_argument('hide_console')
        
        self.getDriver()

        self.driver = webdriver.Chrome(self.driverPath,
                                       options=self.option)

    def getDriver(self):
        path = os.getcwd()
        self.driverPath = path+"/chromedriver.exe"
        
    def links_104_txt(self):
        search = re.get(self)
        search.encoding = 'utf-8'
        soup = BeautifulSoup(search.text,'lxml')

        jobap_links = soup.select('h2 > a')

        
    
    
        jobap_links = links_104_txt
        for jobap_link in jobap_links:
            print(jobap_link.text)
            apply_page = jobap_link.get('href')
            apply_page = 'https:'+apply_page
            
            driver = webdriver.Chrome(self.driverPath,options=self.option)
            driver.get(apply_page)    

    #     #applyJobBtn
    #     # driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").send_keys(Keys.ENTER)
    #   運用104的data base 幫我確認
            driver.find_element_by_xpath("//*[text()='登入']").click()
            window_1=driver.current_window_handle
            windows=driver.window_handles
            print(windows)  #輸入控制代碼集合
            for current_window in windows:   #切換視窗
                if current_window != window_1:
                    driver.switch_to.window(current_window)
            

            driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)

            driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)
        #     time.sleep(1)#網頁仔入中
            driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
            time.sleep(3)#網頁仔入中
            #wait ajax loading
            print('Wed loading')
            
            try:
                no_re_apply = driver.find_element_by_xpath(".//*[@class='d-inline-block border-right pr-2 align-middle']")
                print('aready sumit')
                driver.quit()
                
            except:
                driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").send_keys(Keys.ENTER)
                time.sleep(3)
                pass
            
            
            i=0
            while 1:
                start = time.clock()
        
                try:
                    
                    driver.find_element_by_xpath('//input[@id="resumeList1"]').click()
                    
                    end=time.clock()
                    break
                except:
                    
                    print ("履歷元素找不到歐!")
                    i+=1
                    if i ==10:
                        print('aready sumit')
                        # driver.find_element_by_xpath('//input[@value="取消關閉"]').submit()
                        driver.quit()
                        break
                    end=time.clock()
            print ('waste_Time：'+str(end-start))

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
                    print ("投遞按鈕!")
                    
                    i+=1
                    if i ==5:
                            print('找不到歐')
                            
                            end=time.clock()
                            break
                break
            
            print ('定位耗费时间：'+str(end-start))
if __name__ == "__main__":
    a  = str(input('請搜尋想要找尋工作'))
    page = 1
    headers = {'user-agent': 'Mozilla/1.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    url=re.get(f"https://www.104.com.tw/jobs/search/?keyword={a}&order=2&jobsource=2019indexpoc&ro=0",headers)      
    
    job_apply.links_104_txt(url)

