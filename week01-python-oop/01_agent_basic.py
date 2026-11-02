class Agent:
    version = "1.0"

    # name과 role 입력 받기
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.question_count = 0

    # 질문 받는 인스턴스 메서드 생성
    def ask(self, question):
        self.question_count += 1
        return f'{self.name}가 "{question}" 질문을 받았습니다'

    # 소개하는 인스턴스 메서드 생성
    def introduce(self):
        return f'안녕하세요. 저는 {self.name}이고 역할은 {self.role}입니다.'

# Agent 객체화
agent1 = Agent("Sakura", "일본 취업 도우미")
agent2 = Agent("CodeBot", "Python 도우미")

# Sakura에게 질문 2번, CodeBot에게 질문 1번
agent1.ask("JLPT는 몇 급이 필요해?")
agent1.ask("일본 취업은 어떻게 준비해?")
agent2.ask("클래스가 뭐야?")

# 각각의 질문 횟수 출력
print(agent1.question_count)
print(agent2.question_count)