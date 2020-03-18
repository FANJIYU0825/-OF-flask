from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests as re

# driver = webdriver.Chrome()     # 打开 Chrome 浏览器

'''
先使用 requests 跟 Bs4 來 找尋 網址LIST 
然後再放入 Selenium 內爬蟲
並且自動投遞履歷
未來方向 偵錯以及存入資料庫/比較工作總類
'''
a  = str(input('請搜尋想要找尋工作'))
page = 1
headers = {'user-agent': 'Mozilla/1.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

'''
解析                                        
order=?
order=2 : 依據日期                          
order=1 : 符合程度
order=4 : 接案(104外包網)equal to order=7
order=5 : 常駐國外
order=6 : 外商公司(在台灣工作) 
order=7 : equal to order=4
order=8 : 必須有查詢關鍵字 ===完全符合
order=9 : equal to order=8
asc=13: 依據薪資高低
____________________________________________________
asc=?  還在解析中
asc=1 : 預設值|
asc=2 : 論件計酬|
asc=3 : |
asc=4 : |
asc=5 : |
asc=6 : |
asc=7 : |
asc=8 : |

'''
search=re.get(f"https://www.104.com.tw/jobs/search/?keyword={a}&order=2&jobsource=2019indexpoc&ro=0",headers)
# search=re.get("https://www.104.com.tw/job/6fjk7?jobsource=n_my104_search_h",headers)

search.encoding = 'utf-8'
soup = BeautifulSoup(search.text,'lxml')

jobap_links = soup.select('h2 > a')
jlink_count = 0
for jobap_link in jobap_links:
    print(jobap_link.text)
    apply_page = jobap_link.get('href')
    
    apply_pages = 'https:'+apply_page
    print(apply_pages)
    driver = webdriver.Chrome()
    driver.get(apply_pages)
    # driver.refresh()
    #applyJobBtn
    

    # driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon btn-secondary']").send_keys(Keys.ENTER)
    #運用104的data base 幫我確認
    driver.find_element_by_xpath("//*[text()='登入']").click()
    window_1=driver.current_window_handle
    windows=driver.window_handles
    print(windows)  #輸入控制代碼集合
    for current_window in windows:   #切換視窗
        if current_window != window_1:
            driver.switch_to.window(current_window)
    
    username = 'J122795936'
    passWord = 's2380215'
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passWord)
    time.sleep(1)#網頁仔入中
    

    driver.find_element_by_xpath(".//*[@id='submitBtn']").send_keys(Keys.ENTER)
    time.sleep(3)#網頁仔入中
    #wait ajax loading
    print('Wed loading')
    
    try:
        no_re_apply = driver.find_element_by_xpath(".//*[@class='d-inline-block border-right pr-2 align-middle']")
        print('aready sumit')
        driver.quit()
        continue
    except:
        driver.find_element_by_xpath(".//*[@class='btn btn-sm btn-has-icon apply-button__button btn-secondary']").send_keys(Keys.ENTER)
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
jlink_count +=1    
    

    