# StudyAgent 클래스 생성
class StudyAgent:
    # 이름과 공부 횟수 인스턴스 변수로 초기화
    def __init__(self, name, study_count):
        self.name = name
        self.study_count = study_count
        
    # 공부 횟수를 객체 길이로 반환
    def __len__(self):
        return self.study_count
    # 공부 횟수 대소 비교
    def __gt__(self, other):
        return self.study_count > other.study_count
    # 공부 횟수 같은지 비교
    def __eq__(self, other):
        return self.study_count == other.study_count
    # 공부 횟수 더하여 반환
    def __add__(self, other):
        return self.study_count + other.study_count
    # 정보 문자열로 표현
    def __str__(self):
        return f"{self.name} (공부 횟수: {self.study_count}회)"


# StudyAgent 인스턴스 생성
agent1 = StudyAgent("Sakura", 10)
agent2 = StudyAgent("CodeBot", 5)
agent3 = StudyAgent("AnotherBot", 10)

print(agent1)
print(agent2)

print(len(agent1))
print(len(agent2))

print(agent1 > agent2)
print(agent1 == agent3)
print(agent1 + agent2)