import openai
import gpt_keys 

# API 키 설정
openai.api_key = gpt_keys.OPEN_API_KEY
# 메세지 초기화
messages = []

# 동작
while True:
    #사용자 입력 받기
    content = input("User : ")
    #입력값을 메세지 리스트에 추가
    messages.append({"role":"user", "content": "다음 내용을 summary해줘: " + content})
    #OpenAI의 ChatCompletion API를 사용하여 응답을 생성하기
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )
    # API 응답을 추출하기
    chat_response = completion['choices'][0]['message']['content']
    # 응답 출력
    print(f'summary : {chat_response}')
    # 응답을 메세지 리스트에 추가
    messages.append({"role":"assistant", "content":chat_response})