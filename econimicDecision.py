from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry("640x480")
root.title("경제적 의사결정 프로그램")


# TODO: 위젯 위로 올려야 함
class Business:
    def __init__(self, name, deposit, interest, period):
        self.name = name
        self.deposit = deposit
        self.interest = interest
        self.period = period

        self.npv = None
    
    def npvCal(self):
        self.npv = self.deposit + (self.interest * self.period)


# 빈 레이블 생성 (공백 역할)
def space(co, ro):
    space_label = Label(root, text=" " * 10)  # 텍스트로 공백을 추가
    space_label.grid(column=co, row=ro)


# ===================== 새로운 사업, 기존 사업 =======================
# new
newLabel = Label(root, text = "새로운 사업", font = ("맑은고딕", 16, "bold"))
newLabel.grid(column=1, row=0)

space(2, 0)

# old
aLabel = Label(root, text = "기존 사업", font = ("맑은고딕", 16, "bold"))
aLabel.grid(column=3, row=0)


# ===================== 이름 =======================
# 사업 이름 레이블
nameLabel = Label(root, text = "사업 이름", font = ("맑은고딕", 16, "bold"))
nameLabel.grid(column=0, row=1, sticky="w", padx=10)

# 이름 입력창
newNameEntry = Entry(root, width = 15)
newNameEntry.focus()
newNameEntry.grid(column=1, row=1)

space(2, 1)

oldNameEntry = Entry(root, width = 15)
oldNameEntry.focus()
oldNameEntry.grid(column=3, row=1)


# ===================== 투자금 =======================
# 사업 투자금 레이블
depositLabel = Label(root, text = "사업 투자금", font = ("맑은고딕", 16, "bold"))
depositLabel.grid(column=0, row=2, sticky="w", padx=10)

# 투자금 입력창
newDepositEntry = Entry(root, width = 15)
newDepositEntry.grid(column=1, row=2)

space(2, 2)

oldDepositEntry = Entry(root, width = 15)
oldDepositEntry.grid(column=3, row=2)


# ===================== 이자 =======================
# 사업 투자금 레이블
interestLabel = Label(root, text = "사업 이자", font = ("맑은고딕", 16, "bold"))
interestLabel.grid(column=0, row=3, sticky="w", padx=10)

# 투자금 입력창
newInterestEntry = Entry(root, width = 15)
newInterestEntry.grid(column=1, row=3)

space(2, 3)

oldInterestEntry = Entry(root, width = 15)
oldInterestEntry.grid(column=3, row=3)

# ===================== 기간 =======================
# 사업 기간 레이블
periodLabel = Label(root, text = "계약 기간", font = ("맑은고딕", 16, "bold"))
periodLabel.grid(column=0, row=4, sticky="w", padx=10)

# 기간 입력창
newPeriodEntry = Entry(root, width = 15)
newPeriodEntry.grid(column=1, row=4)

space(2, 4)

oldPeriodEntry = Entry(root, width = 15)
oldPeriodEntry.grid(column=3, row=4)

# ================== 가로 구분선 =====================
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=5, column=0, columnspan=5, sticky='ew', padx=(10, 0), pady=2)

# NPV
npv_label = Label(root, text = "NPV", font = ("맑은고딕", 16, "bold"))
npv_label.grid(column=0, row=6, sticky="w", padx=10)

# IRR
irr_label = Label(root, text = "IRR", font = ("맑은고딕", 16, "bold"))
irr_label.grid(column=0, row=7, sticky="w", padx=10)

# 계산 버튼
cal_button = Button(root, text="비교하기", height=3, bg="#63aff6", fg="navy") # TODO: command 추가해야함
cal_button.grid(row=1, column=4, rowspan=4, padx=10, sticky="ns")

# 사업 이름 추출 실험(완) ==============================
'''
newBusiness = Business(None, None, None, None)

result_Label = Label(root, text="사업의 이름")
result_Label.grid(column=0, row=5)

def whatName():
    newBusiness.name = newNameEntry.get()
    newBusiness.deposit = int(newDepositEntry.get())
    newBusiness.interest = float(newInterestEntry.get())
    newBusiness.period = int(newPeriodEntry.get())
    newBusiness.npvCal()
    result_Label.config(text=newBusiness.npv)


# 비교하기 버튼
button = Button(root, text="비교하기", command=whatName)
button.grid(column=1, row=5)
'''

gameCorporation = Business(None, None, None, None)


# 사용자로부터 입력받기
# FIXME: 삭제
'''
gameCorporation.name = input("사업의 이름을 입력하세요: ")
gameCorporation.deposit = int(input("사업의 계약금을 입력하세요: "))
gameCorporation.interest = float(input("사업의 이자를 입력하세요: "))
gameCorporation.period = int(input("사업의 계약 기간을 입력하세요: "))
'''

# NPV 계산
# gameCorporation.npvCal()


# print(f"{gameCorporation.name}의 NPV는 {gameCorporation.npv}입니다.")


root.mainloop()