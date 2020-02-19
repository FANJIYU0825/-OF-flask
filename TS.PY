from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.webdriver.support.ui as ui

# driver = webdriver.Chrome() 
driver = webdriver.Chrome()     # 打开 Chrome 浏览器
driver.get('https://www.104.com.tw/job/5q22o?jobsource=hotjob_chr')


#applyJobBtn
def inster_ID(username,passWord):

    # driver.find_element_by_xpath(".//*[@class='b-btn js-apply b-btn--default gtm-applybtn-hotjob']").click()
    driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").click()
    
    window_1=driver.current_window_handle
    windows=driver.window_handles
    print(windows)  #輸入控制代碼集合
    for current_window in windows:   #切換視窗
        if current_window != window_1:
            driver.switch_to.window(current_window)
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)

    driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
    return    

username = str('J122795936')
passWord = str('s2380215')
inster_ID(username,passWord)
