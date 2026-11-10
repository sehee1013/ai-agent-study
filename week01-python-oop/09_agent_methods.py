# Agent 클래스 정의
class Agent:
    version = "1.0"
    # 이름을 인스턴스 변수로 초기화
    def __init__(self, name):
        self.name = name

    # 자기 소개 출력하는 메소드 정의
    def introduce(self):
        print(f"저는 {self.name}입니다.")

    # 클래스 메소드 change_version 정의하여 version 정보 변경
    @classmethod
    def change_version(cls, new_version):
        cls.version = new_version

    # 정적 메소드 정의하여 이름이 문자열인지 판별
    @staticmethod
    def is_valid_name(name):
        return name != ""

    @property
    def greeting(self):
        return f"안녕하세요, {self.name}!"
    
# RobotAgent 클래스 정의
class RobotAgent:
    # introduce() 메소드 작성
    def introduce(self):
        print("저는 로봇 에이전트입니다.")
# execute(agent) 함수 정의
def execute(agent):
    agent.introduce()

agent = Agent("Sakura")
agent.introduce()
Agent.change_version("2.0")
print(agent.version)
print(Agent.is_valid_name(""))
print(Agent.is_valid_name("Sakura"))
print(agent.greeting)

robot = RobotAgent()
execute(agent)
execute(robot)