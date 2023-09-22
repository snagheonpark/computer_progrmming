a = input("나이를 입력하세요: ")
print(a, type(a))

age = int(a) #문자형을 숫자형으로 변환

if age > 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")
