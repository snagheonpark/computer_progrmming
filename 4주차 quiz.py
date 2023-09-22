#학생들 점수
students= [90, 45, 64, 9, 17, 29]

# 비어있는 리스트 변수 만들기
results = []

# for 반복문
for score in students:
    if score >= 71:
        results.append("A")
    elif score >= 41:
        results.append("B")
    elif score >= 11:
        results.append("C")
    else:
        results.append("D")

# 결과 출력
print(results)
