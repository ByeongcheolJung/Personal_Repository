def num_check(personal_num):
    if len(personal_num) != 6:
        return 0
    # 숫자 6자리 정확히 입력
    elif personal_num.isnumeric():
        return 1
    else:
        return 0


def num_input():
    while (1):
        print("숫자 6개 입력 : ")
        number = input()
        if 1 == num_check(number):
            return number
        else:
            continue


def Pnum_result(Pnum):
    year = Pnum[0:2]
    month = Pnum[2:4]
    day = Pnum[4:6]
    result = "출생년도 : "
    if int(year) > 50:
        result += "19"
    else:
        result += "20"
    print(result+year+"년", "생년 월일 : ", month+"월"+ day+"일")


a = ""
a = num_input()
Pnum_result(a)
