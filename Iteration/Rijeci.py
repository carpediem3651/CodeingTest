pressed = input()
if not pressed.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
preesed = int(pressed)
if not 1 <= pressed <= 45:
    exit("범위를 벗어남(1 <= n <= 45)")

countA = 1
countB = 0

for i in range(pressed) :
    prevA = countA
    prevB = countB
    countA = prevB
    countB = prevA + prevB

print(str(countA) + " " + str(countB))