print("경제적 의사결정 프로그램입니다.")

class Business:
    def __init__(self, name, interest, period, deposit):
        self.name = name
        self.interest = interest
        self.period = period
        self.deposit = deposit
        self.npv = None
    
    def npvCal(self):
        self.npv = self.deposit + (self.interest * self.period)


gameCorporation = Business(None, None, None, None)

# 사용자로부터 입력받기
gameCorporation.name = input("사업의 이름을 입력하세요: ")
gameCorporation.interest = float(input("사업의 이자를 입력하세요: "))
gameCorporation.period = int(input("사업의 계약 기간을 입력하세요: "))
gameCorporation.deposit = int(input("사업의 계약금을 입력하세요: "))

# NPV 계산
gameCorporation.npvCal()

input(f"{gameCorporation.name}의 NPV는 {gameCorporation.npv}입니다.")