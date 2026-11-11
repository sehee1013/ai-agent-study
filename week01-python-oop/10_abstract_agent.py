# 추상 클래스 Agent 정의
from abc import ABC, abstractmethod

# 검색 실행하는 클래스 정의
class Agent(ABC):
    # 이름을 인스턴스 변수로 초기화
    def __init__(self, name):
        self.name = name
    # 추상 메소드 run(self) 선언
    @abstractmethod
    def run(self):
        pass

# 검색 실행하는 클래스 정의
class SearchAgent(Agent):
    # Agent 클래스에서 선언한 run 메소드 구현
    def run(self):
        print(f"{self.name}: 검색 실행")

# 코드 작성 실행하는 클래스 정의
class CodingAgent(Agent):
    # Agent 클래스에서 선언한 run 메소드 구현
    def run(self):
        print(f"{self.name}: 코드 작성 실행")

# 공통 실행 함수 생성
def execute(agent):
    agent.run()

# 실행
execute(SearchAgent("Sakura"))
execute(CodingAgent("PythonBot"))