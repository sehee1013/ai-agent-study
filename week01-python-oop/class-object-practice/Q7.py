# 첫 줄: "예금주 초기잔액" (예: "kim 1000" -> owner="kim", balance=1000)
# 둘째 줄: 입금액들 (예: "500 300" -> [500, 300])
owner, balance = input().split()
balance = int(balance)
deposits = [int(x) for x in input().split()]

# Account 클래스 정의
class Account:
    """
    입금 업무를 처리
    """
    # 예금주와 초기잔액 정보를 인스턴스 변수로 초기화
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    # 잔액 증가 메소드 선언
    def deposit(self, amount):
        self.balance += amount

    # 현재 잔액 반환하는 메소드 선언
    def get_balance(self):
        return self.balance

# ---- 호출부 (수정 금지) ----
acc = Account(owner, balance)
print(f"{acc.owner} 초기 잔액 {acc.get_balance()}")
for amount in deposits:
    acc.deposit(amount)
    print(f"입금 {amount} -> 잔액 {acc.get_balance()}")