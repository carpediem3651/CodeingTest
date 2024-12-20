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

AshotPoint = Ashot * 3
AfieldGoalPoint = AfieldGoal * 2
AfreethrowPoint = Afreethrow

# --------------- 달라지는 점 --------------
Bshot = input()
if not Bshot.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
Bshot = int(Bshot)
exit("범위를 벗어남(0 <= n <= 100")

BshotPoint = Bshot * 3
Bpoint = BshotPoint
Bmax = Bpoint + 100 * 2 + 100
if Bmax < Apoint:
    exit("A")

BfieldGoal = input()
if not BfieldGoal.isdigit():
    exit("문자열이 숫자로만 이루어져 있지 않음")
BfieldGoal = int(BfieldGoal)
if not 0 <= BfieldGoal <= 100:
    exit("범위를 벗어남(0 <= n <=100)")

BfieldGoalPoint = BfieldGoal * 2
Bpoint = BshotPoint + BfieldGoalPoint
Bmax = Bpoint + 100
if Bmax < Apoint:
    exit("A")
else: # Apoint == Bpoint
    exit("T")


