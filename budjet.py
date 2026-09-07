class BudgetTracker:
    def __init__(self):
        self.expenses=[]

    # 지출 추가하기
    def add_expense(self,title,price,type):
        self.expenses.append({"제목":title,"가격":price,"유형":type})

    # 지출 목록보기
    def show_expenses(self):
        for expense in self.expenses:
            print(f"{expense['제목']}- {expense['가격']}원 ({expense['유형']})")

    # 지출 총액
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense["가격"]
        return total 

print("가계부에 오신 것을 환영합니다.")
tracker = BudgetTracker()

while True:
    print("1.지출 추가하기\n2.지출 목록보기\n3.총 지출 확인하기\n4.종료하기")
    num = int(input("원하시는 번호를 입력해주세요: "))
    if num == 1:    
        # 지출  추가하기
        title = input("지출 제목: ")
        price = int(input("가격 : "))
        type = input("지출 유형(카드/현금): ")
        tracker.add_expense(title,price,type)
    elif num == 2:    
        # 지출 목록보기
        tracker.show_expenses()
    elif num == 3:
        # 총 지출 확인하기
        print(f"총 지출 : {tracker.total_expense()}")
    elif num == 4:
        break
    else:
        print("똑바로 써라")


    