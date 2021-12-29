from flask import Flask, render_template, Blueprint
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

#순서대로 제목, 설명, 링크, 제공기관, 데이터 타입
data_Title = []
data_Explain = []
data_Link = []
data_Provider = []
data_Date = []
data_Area = []
#데이터 넘길때 총합본
data_total = []



def getData(pageNum, dataNum):
    html = urlopen("https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage="+str(pageNum)+"&perPage="+str(dataNum)+"&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=")
    soup = BeautifulSoup(html, "html.parser")

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

    i=1
    for k in data_Area:
        if str(k).isnumeric():
            temp = soup.select("#fileDataList > div.result-list > ul > li:nth-child("+str(i)+") > div.info-data > p:nth-child(6)")
            check = str(temp).split("</span>")[1]
            check = check.split("</p>")[0].strip()
            #print("재검사 결과 : "+check)
            data_Area[i-1] = check
        i=i+1




    print(str(pageNum)+" Page Data collect complete!!")



app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def main_page():
    getData(1,50)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5000)


