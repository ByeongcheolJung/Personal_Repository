import os

#헤더값 넣을 변수 headers
headers = []
#좀있다 한번만 돌릴거라 일회 사용용 변수
switch = False

#결과값 저장할 csv파일명
outfile_name = "merged_ID.csv"
#생성 하면서 오픈
out_file = open(outfile_name, 'w')
#personal_info안의 데이터 불러오기
input_files = os.listdir("personal_info")

for files in input_files:
    #txt파일을 포함하지 않은건 건너뜀
    if ".txt" not in files:
        continue

    #txt파일 순서대로 오픈
    files = open("personal_info/" + files)
    #값들을 임시로 넣어둘 배열
    contents = []

    for line in files:
        if ":" in line:
            splits = line.split(" : ")
            #strip이 없으면 엔터(\n)값 까지 넘어감.
            contents.append(splits[1].strip())
            print("splits-1 : " + splits[1].strip())
            #헤더값 설정하는부분, 첫번째 파일에 있는게 기준이 됨.
            if len(contents) > len(headers):
                headers.append(splits[0].strip())
                print("splits 0 : "+splits[0].strip())

    #헤더 입력 csv파일 최상단 입력이기에 한번만 입력
    if not switch:
        #join함수를 통해 하나로 합치기
        header = ",".join(headers)
        #헤더입력
        out_file.write(header)
        #반복실행 멈추기위해 변수 true
        switch = True

    #데이터 하나로 합치기 9,홍길동,15,남,010-1234-5678 이렇게 이어넣어서 CSV로 넣어버림
    new_line = ",".join(contents)
    out_file.write("\n" + new_line)

    files.close()
    print("파일 종료")

out_file.close()