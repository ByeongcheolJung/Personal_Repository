from urllib.request import urlopen
from bs4 import BeautifulSoup

#파일데이터 페이지수와, 데이터 표시갯수 설정 (디폴트 1/50
pageNum = 3
dataNum = 50
html = urlopen("https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage="+str(pageNum)+"&perPage="+str(dataNum)+"&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=")
soup = BeautifulSoup(html, "html.parser")

#순서대로 제목, 설명, 링크, 제공기관, 데이터 타입
data_Title = []
data_Explain = []
data_Link = []
data_Provider = []
data_Date = []
data_Area = []

for temps in soup.find_all('span', "title"):
    data_Title.append(temps.get_text().strip())

for temps in soup.find_all('dd', "ellipsis publicDataDesc"):
    data_Explain.append(temps.get_text().strip())

for temps in soup.find('div', "result-list").find_all("dt"):
    linkdata = temps.find("a")["href"]
    data_Link.append("https://www.data.go.kr/"+linkdata)

for temps in soup.select("#fileDataList > div.result-list > ul > li > div.info-data > p:nth-child(1) > span.data"):
    data_Provider.append(temps.get_text().strip())

for temps in soup.select("#fileDataList > div.result-list > ul > li > div.info-data > p:nth-child(2) > span.data"):
    data_Date.append(temps.get_text().strip())

i=1
for temps in soup.select("#fileDataList > div.result-list > ul > li > div.info-data > p:nth-child(5)"):
    check = temps.get_text()[10:].strip()
    data_Area.append(check)
    #print(i, str("번째 : "), str(check).isnumeric(), check)
    i=i+1

print("****************************")

i=1
for k in data_Area:
    print("@@@K : "+k)
    if str(k).isnumeric():
        temp = soup.select("#fileDataList > div.result-list > ul > li:nth-child("+str(i)+") > div.info-data > p:nth-child(6)")
        check = str(temp).split("</span>")[1]
        check = check.split("</p>")[0]

        print("재검사 결과 : "+check.strip()[:])
    i=i+1



'''
for i in range(dataNum):
    print("*******"+str(i+1)+"번재 데이터++++++")
    print("Data: ", data_Title[i])
    print("Explain : ", data_Explain[i])
    print("Link : ", data_Link[i])
    print("Provider : "+ str(data_Provider[i]))
    print("Modify Date : " + data_Date[i])
    print("Data Area : " + data_Area[i] + "\n")

print("Data len : ", len(data_Title))
'''
