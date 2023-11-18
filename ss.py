class baverage:
    def __init__(self, kind, price, count):
        self.kind = kind
        self.price = price
        self.count = count
        self.total = 0

    # 주문한 메뉴와 갯수를 받아 가격을 계산하는 함수
    def calculate(self):
       self.total = self.price * self.count

# input을 통해 주문하고자 하는 메뉴와 갯수를 입력받아 함수를 실행하는 코드
while True:
    choice = input("어떤 메뉴를 주문하시나요? : ")
    b = int(input("몇개 고르실건가요? : "))

    # 커피 객체 생성
    coffe = baverage("커피", 3000, b)
    # 녹차 객체 생성
    GreenTea = baverage("녹차", 2500, b)
    # 아이스티 객체 생성
    IceTea = baverage("아이스티", 3000, b)

    #커피를 주문했을 시
    if choice == "커피":
        coffe.calculate()
        print("총 " + str(coffe.total) + "이 나왔습니다.")

    #녹차를 주문했을 시
    elif choice == "녹차":
        GreenTea.calculate()
        print("총 " + str(GreenTea.total) + "이 나왔습니다.")

    #아이스티를 주문했을 시
    elif choice == "아이스티":
        IceTea.calculate()
        print("총 " + str(IceTea.total) + "이 나왔습니다.")

    #잘못된 메뉴를 주문했을 시
    else:
        print("메뉴를 다시 선택해주세요")
