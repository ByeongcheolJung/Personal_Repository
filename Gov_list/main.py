import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re
from openpyxl import load_workbook


#shutil.copy('양식.xlsx', '기관목록 결과.xlsx')

workbook = load_workbook('양식.xlsx')
worksheet = workbook.active

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://gooddata.go.kr/dqe/account/login')
driver.implicitly_wait(30)
#아이디 비밀번호 입력후 로그인
#로그인 화면 이동
driver.find_element(By.ID, 'username').send_keys("sysMaster")
driver.find_element(By.ID, 'password').send_keys("sys!234%")
driver.find_element(By.CLASS_NAME, 'login-form-btn').click()
driver.implicitly_wait(10)

#DB확정상태 검색!!!
#driver.get('https://gooddata.go.kr/dqe/admin/databases?page=0&searchYear=2022&dbSelectionStatus=SELECTED&institutionCode=')

#대상여부 O만 뽑을떄!!!
#https://gooddata.go.kr/dqe/admin/databases?searchYear=2022&isTarget=true&isSelected=&dbSelectionStatus=&institutionType=&institutionCode=&insttName=

#전체 기관 뽑을떄!!!
driver.get('https://gooddata.go.kr/dqe/admin/databases?page=0&searchYear=2022&')


#결과값 갯수
search_result = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/span').text
print('결과값 : '+search_result)
print('정제값 : '+ re.sub(r'[^0-9]','',search_result))
search_res = int(re.sub(r'[^0-9]','',search_result))

#데이터 임시 저장할곳
data_array = [[0]*19 for i in range(search_res)]

#페이지 갯수
pageNum = int(search_res/10)
stoppoint = True
#데이터 저장

for page in range(0,pageNum+1):
        print(page+1)
        #확정상태 뽑을떄!!!
        #driver.get('https://gooddata.go.kr/dqe/admin/databases?page='+str(page)+'&searchYear=2022&dbSelectionStatus=SELECTED&institutionCode=')

        #대상여부가 O인 기관만 뽑을떄!!!
        #driver.get('https://gooddata.go.kr/dqe/admin/databases?page='+str(page)+'&searchYear=2022&isTarget=true&institutionCode=')

        #대상기괸 다 뽑을떄!!!
        driver.get('https://gooddata.go.kr/dqe/admin/databases?page='+str(page)+'&searchYear=2022&')


        driver.implicitly_wait(10)
        for i in range(0,10):

                lineNum = str(i+1)
                try:
                        data_array[i + page * 10][0] = i + page*10+1
                except:
                        print("페이지 크롤링 끝")
                        stoppoint = False
                        break

                data_array[i+page*10][1] = driver.find_element(By.XPATH, '// *[ @ id = "app"] / div[4] / div / div[1] / div[7] / table / tbody / tr['+lineNum+'] / td[3]').text
                data_array[i+page*10][2] = driver.find_element(By.XPATH, '// *[ @ id = "app"] / div[4] / div / div[1] / div[7] / table / tbody / tr['+lineNum+'] / td[4]').text
                data_array[i+page*10][3] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[5]/a').text
                data_array[i+page*10][4] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[6]').text
                data_array[i+page*10][5] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[7]').text
                data_array[i+page*10][6] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[8]').text
                data_array[i+page*10][7] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[9]').text
                data_array[i+page*10][8] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[10]').text
                data_array[i+page*10][9] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[11]').text
                data_array[i+page*10][10] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[12]').text
                data_array[i+page*10][11] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[13]').text
                data_array[i+page*10][12] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[14]').text
                data_array[i+page*10][13] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[15]').text
                data_array[i+page*10][14] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[16]').text
                data_array[i+page*10][15] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[17]').text
                data_array[i+page*10][16] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[18]').text
                data_array[i+page*10][17] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[19]').text
                data_array[i+page*10][18] = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[7]/table/tbody/tr['+lineNum+']/td[20]').text

        if stoppoint:
                continue
        else:
                break


for x in range(0,search_res):
        print(data_array[x])
        for y in range(0, 19):
                worksheet.cell(row = 3+x,column=y+1, value=data_array[x][y])

today_month = ""
if time.localtime().tm_mon<10:
        today_month = "0" + str(time.localtime().tm_mon)

today_day = ""
if time.localtime().tm_mday<10:
        today_day = "0" + str(time.localtime().tm_mday)

today_hour = ""
if time.localtime().tm_hour<10:
        today_hour = "0" + str(time.localtime().tm_hour)

today_min = ""
if time.localtime().tm_min<10:
        today_min = "0" + str(time.localtime().tm_min)


workbook.save('CRAWLING-RESULT_'+today_month+today_day+'_'+today_hour+today_min+'.xlsx')
workbook.close()