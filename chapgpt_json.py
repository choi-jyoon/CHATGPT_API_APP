# 응답형태를 json 형태로 바꾸기 -> 이후에 더 유용 .
# 토큰 : 의미를 가지고 있는 최소 단위 

from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
from PIL import Image

load_dotenv()   # env 파일 메모리에 로드하기 

openai_api_key = os.getenv('OPEN_API_KEY')

client = OpenAI(api_key= openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)