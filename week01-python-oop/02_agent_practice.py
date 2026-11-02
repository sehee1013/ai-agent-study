class StudyAgent:
    # 공통 소속
    organization = "OpenAI Academy"

    # 이름, 전문 분야 정보 입력
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.study_count = 0

    # 공부할 내용 입력 받고, 호출될 때마다 공부 횟수 1 증가
    def study(self, content): 
        self.study_count += 1
        return f'{self.name}이 "{content}"를 공부했습니다.'

    # 전문 분야 변경
    def change_field(self, new_field):
        self.field = new_field

    # 정보 출력
    def data_print(self):
        print(self.name)
        print(f"전문 분야: {self.field}")
        print(f"공부 횟수: {self.study_count}")
        print()

# Agent 두 개 생성
agent1 = StudyAgent("PythonBot", "Python")
agent2 = StudyAgent("AIBot", "AI")

# PythonBot 공부 시키기
agent1.study("클래스")
agent1.study("인스턴스")
agent1.study("self")

# AIBot 공부 시키기
agent2.study("LLM")

# PythonBot 전문 분야 바꾸기
agent1.change_field("Python + AI")

# 결과 출력
agent1.data_print()
agent2.data_print()

print(f"소속: {StudyAgent.organization}")