# 첫 줄: "상품명 정가" (예: "노트북 1200000" -> name="노트북", price=1200000)
# 둘째 줄: 할인율(%)들 (예: "10 20" -> [10, 20])
name, price = input().split()
price = int(price)
percents = [int(x) for x in input().split()]

# Product 클래스 정의
class Product:
    # 이름과 가격을 인스턴스 변수로 초기화
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # 할인된 가격을 반환하는 메소드 정의
    def discounted(self, percent):
        return self.price * (100 - percent) // 100
        
# ---- 호출부 (수정 금지) ----
p = Product(name, price)
for percent in percents:
    print(f"{p.name} {percent}% 할인가 {p.discounted(percent)}")
print(f"정가 {p.price}")