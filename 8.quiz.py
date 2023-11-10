import random

def 로또번호():
    results = []
    for i in range(6):
        number = random.randint(1, 45)
        if number not in results:
            results.append(number)

    results.sort()
    print(f"생성된 로또 번호는 {results} 입니다")
    return results

lotto_numbers = 로또번호()
