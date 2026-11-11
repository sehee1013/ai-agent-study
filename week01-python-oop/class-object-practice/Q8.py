# 첫 줄: 강아지 수 n. 이어지는 n 줄: "이름 나이" (예: "바둑이 3" -> ["바둑이", "3"])
n = int(input())
rows = [input().split() for _ in range(n)]

# Dog 클래스 정의
class Dog:
    # 이름과 나이를 인스턴스 변수로 초기화
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # "{name}: 멍멍" 형식의 문자열 반환
    def bark(self):
        return f"{self.name}: 멍멍"
    # 강아지 나이를 사람 나이로 환산한 결과 반환
    def human_age(self):
        return self.age * 7

# ---- 호출부 (수정 금지) ----
for dog_name, dog_age in rows:
    dog = Dog(dog_name, int(dog_age))
    print(dog.bark())
    print(f"{dog.name} {dog.age}살 = 사람 나이 {dog.human_age()}살")