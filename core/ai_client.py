# from wsgiref import types
from google import genai
from google.genai import types
import time
from tools import get_tools
# client = genai.Client(api_key="AIzaSyCvmXguGsTvl2CqsSImrrmKP9qMxpp9PxQ")
client = genai.Client(api_key="AIzaSyBRgsYMh-dZknRbE04Xo6gHZA6nesc4ubo")

date = time.strftime("%Y-%m-%d")
date_name = time.strftime("%A")
while True:
    input_text = input("Enter your request: ")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Yout are ai agent class representative in university, for It Studente and your name is RepIt and you build to make and the user asks you this {input_text} answer frendly from the tool if ot say today date is this context {date} and today is {date_name} and tools is also {get_tools}",
        
            
        config=types.GenerateContentConfig(tools=tools)
    )
    fa = response.candidates[0].content.parts
    part = response.candidates[0].content.parts

    for fn in part:
        if hasattr(fn, "function_call") and fn.function_call is not None:
            fc = fn.function_call
            print("Function name:", fc.name)
            print(fc.args)
        else:
            print(fn.text)