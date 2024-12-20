moves = input()
if moves.count("A") + moves.count("B") + moves.count("C") != len(moves) :
    exit("문자열에 A,B,C 이외의 문자가 있음")

cups = "123"
# 콘텍스트
for move in moves:
    if move == "A": # A : 123 -> 213
        cups = cups[1] + cups[0] + cups[2]
    elif move == "B": # B : 123 ->132
        cups = cups[0] + cups[2] + cups[1]
    else: # c : 123 -> 321
        cups = cups[2] + cups[1] + cups[0]

# 목적 cups위치
print(cups.find("1") + 1)