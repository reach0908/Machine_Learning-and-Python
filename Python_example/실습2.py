player_count = int(input("\n 달리기 선수가 몇 명인가요? "))

players = list()

while player_count > 0:
    players.append(input("지금 들어온 선수 이름을 입력하세요 : "))
    player_count -= 1

print("\n 달리기 시합 결과!!\n")

for rank, player in enumerate(players):
    print(rank+1, "등", player)

print("\n 수고 많았습니다. 여러분!!")