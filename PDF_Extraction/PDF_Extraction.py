'''PDF에서 원하는 부분만 추출하여 Excel에 저장하는 기능'''


filename = 'C:\\Users\\Gurutech\\Documents\\Personal_Repository\\PDF_Extraction\\Sample_data\\[약식의결서(안)]_수정.pdf'


from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
for page_layout in extract_pages(filename):
    #text는 단순 데이터 받고, check는 유형 6가지 확인하기 위한것
    text = []
    check = []
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            #text값이 비어있으면 스킵
            if element.get_text() == []:
                continue
            else:
                text.append(element.get_text())

                print(text)

        #text초기화
        text = []