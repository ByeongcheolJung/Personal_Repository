#랜덤 데이터 만들기
import os
import random
import time

class random_data():
    def random_name(self):
        first_name = "김이박최정강조윤장임"
        middle_name = "민서예지도하주윤채현지"
        last_name = "준윤우원호후서연아은진"

        name = ""
        name += random.choice(first_name)
        name += random.choice(middle_name)
        name += random.choice(last_name)
        #print("name : "name)
        return name

    def random_age(self):
        age = random.randrange(1, 100)
        return str(age)

    def random_sung(self):
        man = "남", "여"
        sung = random.choice(man)
        return sung

    def random_phone(self):
        phone = "010-"
        for i in range(4):
            phone += str(random.randrange(0,10))
        phone +="-"
        for i in range(4):
            phone += str(random.randrange(0,10))
        return phone



def create_file(file_cnt):
    try: os.mkdir("personal_info")
    except FileExistsError:
        print("디렉토리가 이미 생성되어있습니다. : personal_info")

    for i in range(file_cnt):
        filename = "personal_info\INFO_" + str(i+1) + ".txt"
        file = open(filename,'w')
        file.write("개인 번호 : "+ str(i+1))
        file.write("\n이름 : " + random_data().random_name())
        file.write("\n나이 : " + random_data().random_age())
        file.write("\n성별 : " + random_data().random_sung())
        file.write("\n번호 : " + random_data().random_phone())
        file.close()


if __name__ == '__main__':
    start_time = time.time()
    #create_file(10)
    end_time = time.time()
    print("pricessing time : " + str(end_time-start_time))
    print(str(time.time())[-4:-2])

    print(str(time.time())[-6:-2])
