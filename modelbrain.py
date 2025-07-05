#1. GROQ website - 
#2. store key - Environment
#3 VE

# ==============================================
# 🔹 STEP 1: SECURE API KEY SETUP (Environment)
# ==============================================

from dotenv import load_dotenv
load_dotenv() ## take environment variables from .env

import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY") #Security First! Never hardcode API keys



# ==============================================
# 🔹 STEP 2: IMAGE TO BASE64 CONVERTER
# ==============================================
import base64


image_path="fish2.jpeg"


def convert_image_to_base64(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')






# ==============================================
# 🔹 STEP 3: MULTIMODAL AI ANALYSIS ENGINE
# ==============================================
from groq import Groq

query = "Is there something wrong with my turle"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def get_ai_response_from_image_and_text(query, model, encoded_image):
    client=Groq(api_key=GROQ_API_KEY)  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
            messages=messages,
            model=model
        )
    return chat_completion.choices[0].message.content
    


encode_image=convert_image_to_base64(image_path)

print(get_ai_response_from_image_and_text(query,model,encode_image))
      