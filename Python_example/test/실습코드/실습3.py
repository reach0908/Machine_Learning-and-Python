phrase = input("문자열을 입력하세요 : ")

acronym = ""
for word in phrase.upper().split():
    print(word)
    acronym += word[0]
    print(word[0])

print(acronym)