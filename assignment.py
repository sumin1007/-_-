class User:
    def __init__(self, name, phone, sex):
        self.name = name
        self.phone = phone
        self.sex = sex

person = []
while(True):
    name = input("이름을 입력하세요 : ")
    if(name == "그만"):
        for i in person:
            print("이름은 " + i.name + ", 전화번호는 " + i.phone + ", 성별은 " + i.sex + "입니다.")
        break
    
    phone = input("전화번호를 입력하세요 : ")
    
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if(sex != "male" and sex != "female"):
        sex = "unknown"
        
    info = User(name, phone, sex)
    person.append(info)

    for i in person:
        print("이름은 " + i.name + ", 전화번호는 " + i.phone + ", 성별은 " + i.sex + "입니다.")
