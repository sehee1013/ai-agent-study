# SearchAgent 클래스 정의
class SearchAgent:
    # run() 메소드 정의
    def run(self):
        print("검색 기능 실행")
    
# ChatAgent 클래스 정의
class ChatAgent:
    # run() 메소드 정의
    def run(self):
        print("채팅 기능 실행")

# SearchAgent와 ChatAgent를 상속 받은 CareerAgent 클래스 정의
class CareerAgent(SearchAgent, ChatAgent):
    pass

agent = CareerAgent()

agent.run()
print(CareerAgent.mro())