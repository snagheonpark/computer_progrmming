class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

while True:
    choose_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티 - 종료하려면 'exit' 입력): ")

    if choose_beverage.lower() == 'exit':
        print("주문을 종료합니다.")
        break

    number = int(input("수량을 입력하세요: "))
    if choose_beverage == "커피":
        total = Coffee.calculate(number)
        print(f"{Coffee.name} {number}잔의 총 가격은 {total}원 입니다.")
    elif choose_beverage == "녹차":
        total = GreenTea.calculate(number)
        print(f"{GreenTea.name} {number}잔의 총 가격은 {total}원 입니다.")
    elif choose_beverage == "아이스티":
        total = IceTea.calculate(number)
        print(f"{IceTea.name} {number}잔의 총 가격은 {total}원 입니다.")
    else:
        print("올바른 음료를 선택하세요.")
