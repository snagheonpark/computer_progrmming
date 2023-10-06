# 사용자로부터 단수를 입력 받음
a = int(input("몇 단까지 출력할까요? "))

def number(n):
    for x in range(2, n + 1):
        print("------- [" + str(x) + "단] -------")
        for y in range(1, n + 1):
            print(x, "X", y, "=", x * y)

number(a)

