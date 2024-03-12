
from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
from PIL import Image

load_dotenv()   # env 파일 메모리에 로드하기 

openai_api_key = os.getenv('OPEN_API_KEY')

client = OpenAI(api_key= openai_api_key)
MODEL = "gpt-4-vision-preview"

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 사진에 대해서 설명해주라"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000088/88003/88003_320.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=100,
)

print(response.choices[0])