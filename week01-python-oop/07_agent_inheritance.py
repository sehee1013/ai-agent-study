# 부모 클래스 Agent 정의
class Agent:
    # 이름을 인스턴스 변수로 초기화
    def __init__(self, name):
        self.name = name

    # 자기소개 문자열 반환 메서드 정의
    def introduce(self):
        return f"안녕하세요. 저는 {self.name}입니다."
    
# 자식 클래스 CareerAgent 정의
class CareerAgent(Agent):
    # 부모의 초기화 메서드를 호출하고 국가 정보를 추가
    def __init__(self, name, country):
        # 부모 클래스에서 이름 초기화
        super().__init__(name)
        self.country = country

    # 부모의 자기소개를 확장하도록 메서드 오버라이딩
    def introduce(self):
        return f"{super().introduce()} {self.country} 취업을 도와드립니다."

# 자식 클래스 CodingAgent 정의
class CodingAgent(Agent):
    # 부모의 초기화 메서드를 호출하고 언어 정보를 추가
    def __init__(self, name, language):
        # 부모 클래스로 이름 초기화
        super().__init__(name)
        self.language = language

    # 부모의 자기소개를 확장하도록 메서드 오버라이딩
    def introduce(self):
        return f"{super().introduce()} {self.language} 학습을 도와드립니다."


career_agent = CareerAgent("Sakura", "일본")
coding_agent = CodingAgent("CodeBot", "Python")

print(career_agent.introduce())
print(coding_agent.introduce())