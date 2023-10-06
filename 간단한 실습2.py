pingpong_list = ["나영", "예진", "원빈", "현빈"]

def create_contents_of_mail(name):
    return f"한국교통대학교 천하제일 탁구대회, {name}님 탁구 대회에 참여해주셔서 감사합니다.\n행사 일시: 2023-10-06, 시간: 10:30 AM, 복장: 트레이닝 복\n행사 당일에 뵙겠습니다. {name}님 감사합니다."

results = []

for people in pingpong_list:
    i = create_contents_of_mail(people)
    results.append(i)

for mail in results:
    print(mail)
