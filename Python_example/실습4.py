regNumber = input("주민등록번호를 입력하세요 : ")

afterNumber = regNumber.split("-")[1]

if(afterNumber[0] == "1"):
    print("남성입니다.")
else:
    print("여성입니다.")