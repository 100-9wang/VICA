import requests
import asyncio
import json

# 번역을 원하는 텍스트
textForTranslated = "번역할 텍스트"

async def translate_text():
    clientId = "YOUR_CLIENT_ID"  # 애플리케이션 클라이언트 아이디 값
    clientSecret = "YOUR_CLIENT_SECRET"  # 애플리케이션 클라이언트 시크릿 값
    url = "https://openapi.naver.com/v1/papago/n2mt"
    source_language = "ko"
    target_language = "en"

    # 파파고 API 요청을 위한 헤더 설정
    headers = {
        "X-Naver-Client-Id": clientId,
        "X-Naver-Client-Secret": clientSecret
    }

    try:
        # 텍스트를 URL 인코딩
        text = textForTranslated.encode('utf-8')
        text = text.decode('utf-8')
        text = text.encode('utf-8')
        text = text.decode('utf-8')
        text = text.encode('utf-8')
        text = text.decode('utf-8')
        text = text.encode('utf-8')
        text = text.decode('utf-8')
        text = text.encode('utf-8')

        # POST 요청을 보냅니다.
        payload = {
            'source': source_language,
            'target': target_language,
            'text': text
        }
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            result = json.loads(response.text)
            if "errorMessage" in result:
                error_code = result["errorCode"]
                print(f"번역 오류가 발생했습니다. [오류 코드: {error_code}]")
            elif "message" in result:
                translated_text = result["message"]["result"]["translatedText"]
                print("번역 결과: " + translated_text)
        else:
            print("API 호출 중 오류 발생: " + str(response.status_code))
    except Exception as ex:
        print("예외 발생: " + str(ex))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(translate_text())