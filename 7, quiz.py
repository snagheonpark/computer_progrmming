n = int(input("크리스마스 트리의 높이를 설정하세요: "))

def number(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()

number(n)
