
from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
from PIL import Image

load_dotenv()   # env 파일 메모리에 로드하기 

openai_api_key = os.getenv('OPEN_API_KEY')

client = OpenAI(api_key= openai_api_key)
MODEL = "dall-e-3"
response = client.images.generate(
  model=MODEL,
  prompt="각각 토끼모양, 곰돌이 모양 모자를 쓴 강아지 두 마리가 잔디밭에서 뒹굴고 있어",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

# 저장 파일 이름 설정
filename = 'image.jpg'
response = requests.get(image_url)
with open(filename, 'wb') as f:
  f.write(response.content)
  
Image.open(filename)
pass