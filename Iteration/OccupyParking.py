# 'C','.'와 같은 매직넘버를 쓰지 말 것.
PARKED = 'C'
EMPTY = '.'
spaces = input()
if not spaces.isdigit():exit(f"{spaces}이 숫자로만 이루어져 있지 않음")
spaces = int(spaces)
if not 1 <= spaces <= 100:exit(f"범위를 벗어남(1 <= {spaces} <= 100)")
continuousDay = input()
if not continuousDay.isdigit():exit(f"{continuousDay}이 숫자로만 이루어져 있지 않음")
continuousDay = int(spaces)
if not 1 <= continousDay <= 100: exit(f"범위를 벗어남(1 <= {continousDay} <= 100)")
history = ""
for i in range(continuousDay):
    data = input()
    if data.count(PARKED) + data.count(EMPTY) != spaces:
        exit(f"잘못된 입력값('C', '.'만 입력 가능, {spaces}만큼 입력 필요)")
    history += data
continuousParking = 0
for i in range(spaces):
    isContinuous = True
    for j in range(continuousDay):
        if history[i + j * spaces] == PARKED:
            isContinuous = False
            break
    if isContinuous:
        continuousParking += 1
print(continuousParking)