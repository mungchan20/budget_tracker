import json

class BudgetTracker:
    def __init__(self):
        self.expenses=[]

    # 지출 추가하기
    def add_expense(self,title,price,type):
        self.expenses.append({"제목":title,"가격":price,"유형":type})

    # 지출 목록보기
    def show_expenses(self):
        num = 1
        for expense in self.expenses:
            print(f"{num}.{expense['제목']}- {expense['가격']}원 ({expense['유형']})")
            num+=1

    # 지출 총액
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense["가격"]
        return total 

    # 지출 유형별 합계
    def total_by_type(self,type):
        total = 0
        for expense in self.expenses:
            if expense["유형"] == type:
                total += expense["가격"]
        return total       

    # 지출 삭제하기
    def delete_expense(self,num):
        del self.expenses[num-1]

    def save_to_file(self):
        with open("expenses.json","w",encoding="utf-8") as f:
            json.dump(self.expenses,f,ensure_ascii=False)

    def load_from_file(self):
        with open("expenses.json","r",encoding="utf-8") as f:
            self.expenses = json.load(f)

print("가계부에 오신 것을 환영합니다.")
tracker = BudgetTracker()
valid_type = ["카드","현금"]

try:
    tracker.load_from_file()
except FileNotFoundError:
    print("저장된 기록이 없습니다. 새로시작합니다.")

while True:
    print("1.지출 추가하기\n2.지출 목록보기\n3.총 지출 확인하기\n4.지출 삭제하기\n5.유형별 합계\n6.종료하기")
    num = int(input("원하시는 번호를 입력해주세요: "))
    if num == 1:    
        # 지출  추가하기
        title = input("지출 제목: ")
        price = int(input("가격 : "))
        type = input("지출 유형(카드/현금): ")
        if type in valid_type:
            tracker.add_expense(title,price,type)
        else:
            print("카드나 현금중에서만 입력해라")
    elif num == 2:    
        # 지출 목록보기
        tracker.show_expenses()
    elif num == 3:
        # 총 지출 확인하기
        print(f"총 지출 : {tracker.total_expense()}")
    elif num == 4:
        del_num = int(input("삭제하실 지출의 번호를 입력: "))
        if 1<=del_num<=len(tracker.expenses):
            tracker.delete_expense(del_num)
        else:
            print("똑바로 써라")
    elif num == 5:
        type = input("유형을 골라주세요:")
        if type in valid_type:
            print(f"{type} 합계 : {tracker.total_by_type(type)}")
        else:
            print("카드 또는 현금만 입력 가능")
    elif num == 6:
        tracker.save_to_file()
        break
    else:
        print("똑바로 써라")


    