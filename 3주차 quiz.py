# 환율표 딕셔너리 생성
exchange_rates = {
    "달러": 1320,  # 1달러 당 원화 환율
    "엔": 950,     # 1엔화 당 원화 환율
    "위안": 182     # 1위안화 당 원화 환율
}

# 철수가 가지고 있는 돈 리스트 생성
wallet = [
    {"currency": "달러", "amount": 13},
    {"currency": "엔", "amount": 200},
    {"currency": "위안", "amount": 13}
]

# 각 통화를 원화로 환산하여 합산
total_krw = sum(item["amount"] * exchange_rates[item["currency"]] for item in wallet)

# 결과 출력
print(f"철수가 가지고 있는 돈의 원화 가치는 {total_krw} 원 입니다.")
