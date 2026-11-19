# 첫 줄: "모델명 연료" (예: "소나타 5" -> model="소나타", fuel=5)
# 둘째 줄: 주행 요청 거리들 (예: "20 15 30" -> [20, 15, 30])
model, fuel = input().split()
fuel = int(fuel)
trips = [int(x) for x in input().split()]

# Car 클래스 정의
class Car:
    # 모델명과 연료를 인스턴스 변수로 초기화
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel
    # 주행 거리를 받아 실제 주행 거리를 반환하고 연료를 소모하는 메서드    
    def drive(self, km):
        driven_distance = min(km, self.fuel * 10)
        self.fuel -= driven_distance // 10
        return driven_distance
        
    # 남은 연료 상태 나타내는 문자열 반환 메서드 
    def status(self):
        return f"{self.model} 남은 연료 {self.fuel}"

# ---- 호출부 (수정 금지) ----
car = Car(model, fuel)
print(car.status())
for km in trips:
    driven = car.drive(km)
    print(f"요청 {km}km -> 주행 {driven}km")
    print(car.status())