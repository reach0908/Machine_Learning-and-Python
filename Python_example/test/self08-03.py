string = input("문자열 입력 : ")

if string.isdigit():
    print("숫자입니다.")
elif string.isalpha():
    print("문자입니다.")
elif string.isalnum():
    print("글자 + 숫자입니다.")
else:
    print("모르겠습니다.")