# 환율표 딕셔너리 생성
환율 = {
    "달러": 1320,  # 1달러 당 원화 환율
    "엔": 950,     # 1엔화 당 원화 환율
    "위안": 182     # 1위안화 당 원화 환율
}

# 철수가 가진 돈을 리스트 요소로 하는 리스트 변수 생성
돈 = [13, 200, 13]  # 각각 달러, 엔화, 위안

# 딕셔너리의 Key 값을 호출하여 리스트로 가져오기
key = "달러"
a = 환율[key]
달러환산 = a*돈[0]

key = "엔"
b = 환율[key]
엔환산 = b*돈[1]

key = "위안"
c = 환율[key]
위안환산 = c*돈[2]

x = (달러환산+엔환산+위안환산)

print(f"철수가 가지고 있는 돈의 원화가치는 {x}원 입니다")


