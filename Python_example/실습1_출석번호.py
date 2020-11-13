at=["이황","이이","원효"]
print("현재 학생은 %s" %at)

a = input("전학 온 학생은 누구입니까? ")
b = 0
at.append(a)
print(at)
print("번호 재정렬...")
at.sort()

for i in at:
    b = b+1
    print(b, i)