# from dotenv import load_dotenv
# import os
# from openai import OpenAI

# load_dotenv()   # env 파일 메모리에 로드하기 

# openai_api_key = os.getenv('OPEN_API_KEY')

# client = OpenAI(api_key= openai_api_key)

# MODEL = "gpt-3.5-turbo-1106"

# want_to = """아래 내용을 기반으로 질의응답 하는 로봇이다
# content
# {}"""

# content = """비빔밥: 다양한 채소와 고기가 들어간 건강하고 맛있는 한 그릇의 음식입니다.
# 라면: 간편하게 끓여먹을 수 있는 라면은 시간이 부족할 때나 급한 식사로 좋습니다.
# 샐러드: 가벼우면서 영양가가 높은 샐러드는 다이어트 중이거나 건강을 고려하는 분들에게 좋은 선택입니다.
# 찜닭: 부드러운 닭고기와 고추장의 매콤한 맛이 일품인 찜닭은 한끼 식사로도 훌륭합니다.
# 김밥: 간편하고 맛있는 김밥은 언제나 좋은 선택이죠. 다양한 종류의 김밥을 골고루 챙겨보세요."""

# def ask_to_gpt(messages):
#     response = client.chat.completions.create(
#         model=MODEL,
#         top_p=0.1,
#         temperature=0.1,
#         messages=messages
#     )
    
#     return response.choices[0].message.content

# messages = [
#     {'role':'system', 'content':want_to.format(content)},
# ]

# while True:
#     user_input = input("질문 : ")
    
#     if user_input.lower() == 'quit':
#         break
#     messages.append({
#         'role':'user', 'content':user_input
#     },)
#     response = ask_to_gpt(messages)
#     messages.append(
#         {'role':'assitant', 'content':response}
#     )
#     print(response)