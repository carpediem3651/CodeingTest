# 변수에 'mb'를 표시한 걸 주의깊게 보자. 요구사항에 따라 gb,kb로 바뀔 수 있다.
mbPerMonth = input()
if not mbPerMonth.isdigit():exit(f"{mbPerMonth}이 숫자로만 이루어져 있지 않음")
mbPerMonth = int(mbPerMonth)
if not 1 <= mbPerMonth <= 1000:exit(f"범위를 벗어남(1 <= {mbPerMonth} <= 1000)")

spendMonths = input()
if not spendMonths.isdigit():exit(f"{spendMonths}이 숫자로만 이루어져 있지 않음")
spendMonths = int(spendMonths)
if not 1 <= {spendMonths} <= 1000:exit(f"범위를 벗어남(1 <= {spendMonths} <= 100)")

# spendPermonth는 사용한 데이터를 쌓는건 컨텍스트에서 변화가 생기더라도 바뀌지 않는 로직이다.
spendPerMonth = []
for i in range(spendMonths) :
    spendMb = input()
    if not spendMb.isdigit():exit(f"{spendMb}이 숫자로만 이루어져 있지 않음")
    spendMb = int(spendMb)
    if not 1 <= spendMb >= 10000 : exit(f"범위를 벗어남(1 <= {spendMb} <= 10000)")
    spendPerMonth.append(spendMb)

# availablemb 이통사의 조건에 따라 자주 바뀔 수 있는 로직
availablemb = mbPerMonth * (spendMonth + 1) - sum(spendPerMonth)
print(availablemb)