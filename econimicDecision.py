from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry("640x480")
root.title("경제적 의사결정 프로그램")


class Business:
    def __init__(self, name, deposit, proceed, interest, period):
        self.name = name
        self.deposit = deposit
        self.proceed = proceed
        self.interest = interest
        self.period = period

        self.npv = None
        self.i = None
        self.roi = None
    
    def npvCal(self):
        self.i = self.interest/100
        self.npv = (self.proceed)*(((self.i+1)**self.period)-1)/(self.i*((self.i+1)**self.period))
    
    def roiCal(self):
        self.roi = self.npv / self.deposit


# 빈 레이블 생성 (공백 역할)
def space(co, ro):
    space_label = Label(root, text=" " * 10)  # 텍스트로 공백을 추가
    space_label.grid(column=co, row=ro)


# ===================== 새로운 사업, 기존 사업 =======================
# new
new_Label = Label(root, text = "새로운 사업", font = ("맑은고딕", 16, "bold"))
new_Label.grid(column=1, row=0)

space(2, 0)

# old
old_Label = Label(root, text = "기존 사업", font = ("맑은고딕", 16, "bold"))
old_Label.grid(column=3, row=0)


# ===================== 이름 =======================
# 사업 이름 레이블
name_Label = Label(root, text = "사업 이름", font = ("맑은고딕", 16, "bold"))
name_Label.grid(column=0, row=1, sticky="w", padx=10)

# 이름 입력창
newName_Entry = Entry(root, width = 15)
newName_Entry.focus()
newName_Entry.grid(column=1, row=1)

space(2, 1)

oldName_Entry = Entry(root, width = 15)
oldName_Entry.grid(column=3, row=1)


# ===================== 투자금 =======================
# 사업 투자금 레이블
deposit_Label = Label(root, text = "초기 투자금", font = ("맑은고딕", 16, "bold"))
deposit_Label.grid(column=0, row=2, sticky="w", padx=10)

# 투자금 입력창
newDeposit_Entry = Entry(root, width = 15)
newDeposit_Entry.grid(column=1, row=2)

space(2, 2)

oldDeposit_Entry = Entry(root, width = 15)
oldDeposit_Entry.grid(column=3, row=2)

# ==================== 연간 수익금 ======================
# 수익금 레이블
proceed_Label = Label(root, text = "연간 수익금", font = ("맑은고딕", 16, "bold"))
proceed_Label.grid(column=0, row=3, sticky="w", padx=10)

# 투자금 입력창
newProceed_Entry = Entry(root, width = 15)
newProceed_Entry.grid(column=1, row=3)

space(2, 3)

oldProceed_Entry = Entry(root, width = 15)
oldProceed_Entry.grid(column=3, row=3)


# ===================== 이자 =======================
# 사업 투자금 레이블
interest_Label = Label(root, text = "이자율(%)", font = ("맑은고딕", 16, "bold"))
interest_Label.grid(column=0, row=4, sticky="w", padx=10)

# 투자금 입력창
newInterest_Entry = Entry(root, width = 15)
newInterest_Entry.grid(column=1, row=4)

space(2, 4)

oldInterest_Entry = Entry(root, width = 15)
oldInterest_Entry.grid(column=3, row=4)

# ===================== 기간 =======================
# 사업 기간 레이블
period_Label = Label(root, text = "계약 기간", font = ("맑은고딕", 16, "bold"))
period_Label.grid(column=0, row=5, sticky="w", padx=10)

# 기간 입력창
newPeriod_Entry = Entry(root, width = 15)
newPeriod_Entry.grid(column=1, row=5)

space(2, 5)

oldPeriod_Entry = Entry(root, width = 15)
oldPeriod_Entry.grid(column=3, row=5)

# ================== 가로 구분선 =====================
separator = ttk.Separator(root, orient='horizontal')
separator.grid(row=6, column=0, columnspan=5, sticky='ew', padx=(10, 0), pady=2)

# NPV
npv_label = Label(root, text = "NPV(수익의 현재가치)", font = ("맑은고딕", 12, "bold"))
npv_label.grid(column=0, row=7, sticky="w", padx=10)

newNpv_label = Label(root, text = "계산전", font = ("맑은고딕", 16))
newNpv_label.grid(column=1, row=7, padx=10)

space(2, 7)

oldNpv_label = Label(root, text = "계산전", font = ("맑은고딕", 16))
oldNpv_label.grid(column=3, row=7, padx=10)

    #TODO: old NPV Label 추가

# ROI
roi_label = Label(root, text = "ROI(투자대비 수익)", font = ("맑은고딕", 12, "bold"))
roi_label.grid(column=0, row=8, sticky="w", padx=10)

newRoi_label = Label(root, text = "계산전", font = ("맑은고딕", 16))
newRoi_label.grid(column=1, row=8, padx=10)

space(2, 8)

oldRoi_label = Label(root, text = "계산전", font = ("맑은고딕", 16))
oldRoi_label.grid(column=3, row=8, padx=10)


# 계산 버튼 함수

def resultCal():
    global newBusiness, oldBusiness

    newBusiness = Business(
        name=newName_Entry.get(),
        deposit=int(newDeposit_Entry.get()),
        proceed=int(newProceed_Entry.get()),
        interest=float(newInterest_Entry.get()),
        period=int(newPeriod_Entry.get())
    )
    newBusiness.npvCal()
    newBusiness.roiCal()
    newNpv_label.config(text="%.2f" % newBusiness.npv)
    newRoi_label.config(text="%.2f" % newBusiness.roi)

    oldBusiness = Business(
        name=oldName_Entry.get(),
        deposit=int(oldDeposit_Entry.get()),
        proceed=int(oldProceed_Entry.get()),
        interest=float(oldInterest_Entry.get()),
        period=int(oldPeriod_Entry.get())
    )
    oldBusiness.npvCal()
    oldBusiness.roiCal()
    oldNpv_label.config(text="%.2f" % oldBusiness.npv)
    oldRoi_label.config(text="%.2f" % oldBusiness.roi)

# 설명 버튼 함수

def explanation():

    def explan1(neyo):
        explan1_label = Label(root, text=neyo, font = ("맑은고딕", 11))
        explan1_label.grid(row=10, column=0, columnspan=5, padx=10, pady=(20, 0), sticky="ew")

    if newBusiness.npv > oldBusiness.npv:
        explan1(f"{newBusiness.name}의 NPV가 {oldBusiness.name}의 NPV보다 큽니다. {newBusiness.name}가 이득입니다.")
        newNpv_label.config(fg="blue")

    elif newBusiness.npv < oldBusiness.npv:
        explan1(f"{newBusiness.name}의 NPV가 {oldBusiness.name}의 NPV보다 작습니다. {oldBusiness.name}가 이득입니다.")
        oldNpv_label.config(fg="blue")
    
    else:
        explan1(f"{newBusiness.name}의 NPV와 {oldBusiness.name}의 NPV가 같습니다.")
        newNpv_label.config(fg="green")
        oldNpv_label.config(fg="green")

    def explan2(neyo):
        explan2_label = Label(root, text=neyo, font = ("맑은고딕", 11))
        explan2_label.grid(row=11, column=0, columnspan=5, padx=10, sticky="ew")

    if newBusiness.roi > oldBusiness.roi:
        explan2(f"{newBusiness.name}가 {oldBusiness.name}보다 투자금 대비 수익률이 좋습니다.")
        newRoi_label.config(fg="blue")

    elif newBusiness.roi < oldBusiness.roi:
        explan2(f"{oldBusiness.name}가 {newBusiness.name}보다 투자금 대비 수익률이 좋습니다.")
        oldRoi_label.config(fg="blue")
    
    else:
        explan2(f"{newBusiness.name}과 {oldBusiness.name}의 투자금 대비 수익률이 같습니다.")
        newRoi_label.config(fg="green")
        oldRoi_label.config(fg="green")


# 계산 버튼
cal_button = Button(root, text="계산하기", bg="#63aff6", fg="navy", command=resultCal)
cal_button.grid(row=1, column=4, rowspan=5, padx=10, sticky="ns")

# 결과 설명 버튼
commentary_button = Button(root, text="결과 설명", bg = "red", fg="white", command=explanation)
commentary_button.grid(row=7, column=4, rowspan=2, padx=10, sticky="ns")

root.mainloop()
