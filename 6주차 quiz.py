class 붕어빵:
    def __init__(self, type, price):
        self.type = type
        self.price = price
        self.total = 0

    def sell(self):
        print(self.type + f"붕어빵을 {self.price}에 팔았습니다.")
        self.total += self.price


    def eat(self):
        print(self.type + "붕어빵을 먹었습니다.")

슈크림 = 붕어빵("슈크림", 700)

팥 = 붕어빵("팥", 500)

슈크림.sell()
슈크림.sell()
슈크림.eat()
print(슈크림.total)

팥.sell()
팥.eat()
print(팥.total)

print(슈크림.total + 팥.total)
