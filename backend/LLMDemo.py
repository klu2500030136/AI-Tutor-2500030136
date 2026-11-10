import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("===== AI TUTOR USING GEMINI =====")

question = input("\nEnter your question: ")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )

    print("\n===== GEMINI RESPONSE =====")
    print(response.text)

except Exception as e:
    print("Error:", e)



# import os
# import sys
# import time

# from dotenv import load_dotenv
# from google import genai
# from google.genai import errors

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     print("Error: GEMINI_API_KEY is not set. Add it to backend\\.env or your environment.")
#     sys.exit(1)

# client = genai.Client(api_key=api_key)
# model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

# print("===== AI TUTOR USING GEMINI =====")

# question = input("\nEnter your question: ").strip()
# if not question:
#     print("Please enter a question.")
#     sys.exit(1)

# chat = client.chats.create(model=model)

# try:
#     for attempt in range(3):
#         try:
#             response = chat.send_message(question)
#             if response.text:
#                 print("\n===== GEMINI RESPONSE =====")
#                 print(response.text)
#             else:
#                 print("Gemini returned an empty response. Please try asking again.")
#             break
#         except errors.APIError as error:
#             if error.code in {408, 429, 500, 502, 503, 504} and attempt < 2:
#                 delay = 2 ** attempt
#                 print(f"Gemini is temporarily unavailable. Retrying in {delay} seconds...")
#                 time.sleep(delay)
#                 continue

#             print(f"Error communicating with Gemini (HTTP {error.code}): {error}")
#             if error.code in {408, 429, 500, 502, 503, 504}:
#                 print("Please wait a moment and run the command again.")
#             sys.exit(1)
# finally:
#     client.close()
