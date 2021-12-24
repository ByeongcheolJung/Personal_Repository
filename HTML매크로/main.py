import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys

#시작 페이지값 설정!!!
startNum = 1

driver=webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://202.30.68.36:8080/odms/adminLogin.do?MM=sansam&OC=AAAAAAA')

driver.find_element_by_name('id').send_keys("sansam")
driver.find_element_by_name('pwd').send_keys("gurutech!@#")
driver.find_element_by_class_name('loginBtn').click()
driver.implicitly_wait(10)
driver.get('http://202.30.68.36:8080/odms/checkOpenManagement.do')
select = Select(driver.find_element_by_id('openUrlCheckSelect'))
select.select_by_visible_text('승인')
Select(driver.find_element_by_id('dchkSelect')).select_by_visible_text('(미검토)')

#검색버튼
driver.find_element_by_id('searchBtn').click()

driver.implicitly_wait(10)
Select(driver.find_element_by_class_name('ui-pg-selbox')).select_by_visible_text("50")

time.sleep(5)
page = driver.find_element_by_xpath('//*[@id="chkOpenMngtGrid_toppager_center"]/table/tbody/tr/td[4]/input')
page.clear()
page.send_keys(startNum)
driver.implicitly_wait(10)
page.send_keys(Keys.RETURN)

print("5초간 대기중...")
time.sleep(5)


for k in range(startNum,314):
    print(str(k) + "번째 페이지 이동")

    for i in range(1,51):
        driver.find_element_by_xpath('//*[@id="1"]/td[11]')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id='+str(i)+']/td[13]/button').click()
        print("창 열림 완료")
        driver.implicitly_wait(10)
        try:
            #input[9]로 설정되어야함
            driver.find_element_by_xpath('//*[@id="table4"]/tbody/tr[1]/td[2]/input[9]').click()
            print("제외대상 버튼 클릭 완료")
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("이미 제외 처리")

        driver.implicitly_wait(10)
        try:
            driver.find_element_by_id('okBtn2').send_keys(Keys.ENTER)
            print("설정 완료.")
        except selenium.common.exceptions.ElementClickInterceptedException:
            driver.find_element_by_id('closeBtn2').send_keys(Keys.ENTER)
            print("이미 설정됨.")
            i=i+1
            continue

        print(str(i)+"번쨰 데이터 완료")
        i=i+1

    #다음 페이지 이동
    driver.find_element_by_id('next_t_chkOpenMngtGrid_toppager').click()
    print("페이지 이동중..")
    time.sleep(10)
