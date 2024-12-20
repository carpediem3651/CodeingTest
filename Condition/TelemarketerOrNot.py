# --------------- Input------------------
# 유효성 검사
pnumLast4First = input()
if len(pnumLast4First) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4First.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4First = input()
if len(pnumLast4First) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4First.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4First = input()
if len(pnumLast4First) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4First.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4First = input()
if len(pnumLast4First) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4First.isdigit():
    exit("문자열이 숫자가 아님")


# 텔레마케더 구분 불변식
# 1. 첫 번째 숫자는 8 또는 9
# 2. 네 번째 숫자는 8 또는 9
# 3. 두 번째 숫자와 세 번째 숫자는 같아야 함
# ----------- 판정법--------------
# if pnumLast4First in "89" and pnumLast4First in "89" and pnumLast4Second == pnumLast4Third
#     print("ignore")
# else: 
#     print("answer")
# ----------- 부정법 --------------
if not pnumLast4First in "89":
    exit("asnwer")

if not pnumLast4Fourth in "89":
    exit("answer")

if not pnumLast4Second == pnumLast4Third:
    exit("answer")

print("ignore")