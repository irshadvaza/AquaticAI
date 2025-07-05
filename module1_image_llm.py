


# ==============================================
# 🔹 STEP 1: SECURE API KEY SETUP (Environment)
# ==============================================

import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")






# ==============================================
# 🔹 STEP 2: IMAGE TO BASE64 CONVERTER
# ==============================================
import base64

def covert_image_to_base64(img_path):
    with open(img_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    






















# ==============================================
# 🔹 STEP 3: MULTIMODAL AI ANALYSIS ENGINE
# ==============================================
#1. create object of Qroq Model - retrun result.
# from groq import Groq

# query="Is there something wrong with fish body?"
# model = "meta-llama/llama-4-scout-17b-16e-instruct"

# def get_ai_response_from_image_and_text(query, model, encoded_image):
#     client=Groq(api_key=GROQ_API_KEY)  
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text", 
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}",
#                     },
#                 },
#             ],
#         }]
#     chat_completion=client.chat.completions.create(
#             messages=messages,
#             model=model
#         )
#     return chat_completion.choices[0].message.content
    
# econded_image=convert_image_to_base64(image_path)
# print(get_ai_response_from_image_and_text(query,model,econded_image))
  
      