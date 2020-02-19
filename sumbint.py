from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#applyJobBtn
def inster_ID(username,passWord):
    driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").click()
    
    
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)

    driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
    return    
driver = webdriver.Chrome() 
url = 'https://www.104.com.tw/job/6iayo?jobsource=hotjob_chr'

driver.get(url)
username = str('J122795936')
passWord = str('s2380215')
inster_ID(username,passWord)
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
                print('找不到歐')
                driver.quit()
            
                break
            end=time.clock()
            break
print ('定位耗费时间：'+str(end-start))

# driver.find_element_by_xpath('//input[@id="resumeList0"]').click()
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
                print('找不到歐')
                driver.quit()
            end=time.clock()    
            break
print ('定位耗费时间：'+str(end-start))

# driver.find_element_by_xpath('//input[@id="resumeList0"]').click()

while 1:
    start = time.clock()
    try:
        driver.find_element_by_xpath('//input[@id="btSend"]').click()
        print ('已定位到元素')
        end=time.clock()
        break
    except:
                
        for i in range(100):
            print ("还未定位到元素!")
            i+=1
            if i ==100:
                print('找不到歐')
                driver.quit()
                pass
        end=time.clock()    
    break



print ('定位耗费时间：'+str(end-start))
                
                        

