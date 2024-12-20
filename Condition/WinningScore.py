# --------------- Input------------------
# Apple Input
Ashot = input()
if not Ashot.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
Ashot = int(Ashot)
if not 0 <= Ashot <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

AfieldGoal = input()
if not AfieldGoal.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
AfieldGoal = int(AfieldGoal)
if not 0 <= AfieldGoal <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

Afreethrow = input()
if not Afreethrow.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
Afreethrow = int(Afreethrow)
if not 0 <= Afreethrow <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

# Banana Input
Bshot = input()
if not Bshot.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
Bshot = int(Bshot)
if not 0 <= Bshot <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

BfieldGoal = input()
if not BfieldGoal.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
BfieldGoal = int(BfieldGoal)
if not 0 <= BfieldGoal <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

Bfreethrow = input()
if not Bfreethrow.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
Bfreethrow = int(Bfreethrow)
if not 0 <= Bfreethrow <= 100:
    exit("범위를 벗어남 (0 <= n <= 100)")

# ---------- Activity to Point -----------------
# 불변식
AshotPoint = Ashot * 3
AfieldGoalPoint = AfieldGoal * 2
AfreethrowPoint = Afreethrow

BshotPoint = Bshot * 3
BfieldGoalPoint = BfieldGoal * 2
BfreethrowPoint = Bfreethrow

Apoint = AshotPoint + AfieldGoalPoint + AfreethrowPoint
Bpoint = BshotPoint + BfieldGoalPoint + BfreethrowPoint

# ------------ Result -------------
if Apoint > Bpoint:
    print("A")
elif Apoint < Bpoint:
    print("B")
else: # Apoint == Bpoint
    print("T")


