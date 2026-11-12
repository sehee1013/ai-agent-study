# 첫 줄: 상자 수 n. 이어지는 n 줄: "가로 세로 높이" (예: "2 3 4" -> [2, 3, 4])
n = int(input())
rows = [list(map(int, input().split())) for _ in range(n)]

# Box 클래스 정의
class Box:
    # 가로, 세로, 높이 인스턴스 변수로 초기화
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d
            
    # 부피 계산하여 반환하는 메소드 정의
    def volume(self):
        return self.w * self.h * self.d
    # 겉넓이 계산하여 반환하는 메소드 정의
    def surface(self):
        return 2 * (self.w * self.h + self.h*self.d + self.w*self.d)
    # 계산한 부피와 겉넓이를 문자열 형식으로 반환하는 메소드 정의
    def describe(self):
        return f"{self.w}x{self.h}x{self.d}: 부피 {self.volume()}, 겉넓이 {self.surface()}"

# ---- 호출부 (수정 금지) ----
for w, h, d in rows:
    box = Box(w, h, d)
    print(box.volume())
    print(box.surface())
    print(box.describe())