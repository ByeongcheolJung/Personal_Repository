'''PDF에서 원하는 부분만 추출하여 Excel에 저장하는 기능'''


filename = 'C:\\Users\\Gurutech\\Documents\\Personal_Repository\\PDF_Extraction\\Sample_data\\[약식의결서(안)]_수정.pdf'


import PyPDF2


file = open(filename, 'rb')
fileReader = PyPDF2.PdfFileReader(file)

fileReader.pageMode

# 문서의 정보를 읽어드린다
fileReader.documentInfo

# 전체 페이지수를 출력한다
print("page : ",fileReader.numPages)

# 첫 번째 페이지 정보를 가져온다
pageObj = fileReader.getPage(0)

# 페이지 정보의 텍스트를 가져온다
text = pageObj.extractText()
name =""




print("text : ",text)

try:
    name = name.decode('utf-8')
except:
    pass

print("name : ", name)
