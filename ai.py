# from wsgiref import types
from google import genai
from google.genai import types
import time
date = time.strftime("%Y-%m-%d")
date_name = time.strftime("%A")
# from dotenc
import os
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client(api_key="AIzaSyCvmXguGsTvl2CqsSImrrmKP9qMxpp9PxQ")
client = genai.Client(api_key="AIzaSyBRgsYMh-dZknRbE04Xo6gHZA6nesc4ubo")

def SceduleClass(R_number: str, start: str, end: str, case: str = "None"):
    return f"Class scheduled in room {R_number} from {start} to {end}. Reason: {case}"

# SceduleClass = genai.Function(
#     "SceduleClass",
#     description="Schedule a class for students",
#     parameters={
#         "type": "object",
#         "properties": {
#             "Room_number": {"type": "string", "description": "Room number of the class"},
#             "start": {"type": "string", "description": "Time of the class in HH:MM format"},
#             "end": {"type": "string", "items": {"type": "string"}, "description":"end class in HH:MM format"},
#             "case": {"type": "string", "items": {"type": "string"}, "description": "Why u postpone of student"}
#         },
#         "required": ["Room_number", "start", "students"]
#     }
# )
# /
tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="CheckUser",
                description="to check the user role Student/Admin/Teacher",
                parameters={
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                },
            ),
            types.FunctionDeclaration(
                name="CancelClass",
                description="Cancel a scheduled class",
                parameters={
                    "type": "object",
                    "properties": {
                        "R_number": {"type": "string"},
                        "time": {"type": "string"},
                        "reason": {"type": "string"}
                    },
                    "required": ["R_number", "time"]
                }
            ),
            types.FunctionDeclaration(
                name="SceduleClass",
                description="Schedule a class for students postpon",
                parameters={
                    "type": "object",
                    "properties": {
                        "R_number": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
                        "case": {"type": "string"},
                        "course": {"type": "string"}
                    },
                    "required": ["R_number", "start", "end","course"]
                }
            ),
            types.FunctionDeclaration(
                name="ShowSchedule",
                description="Show the schedule of classes for the week",
                parameters={
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                    },
                    "required": ["date"]
                }
            ),types.FunctionDeclaration(
                name="SceduleClassforSpecificCourse",
                description="Schedule a class for This Course only specific course",
                parameters={
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "course": {"type": "string"},
                    },
                    "required": ["date", "course"]
                }
            ),types.FunctionDeclaration(
                name="ShowClassForToday",
                description="Show class for today",
                parameters={
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "today": {"type": "string"},
                    },
                    "required": ["date", "today"]
                }
            ),types.FunctionDeclaration(
                name="MakeQuiz",
                description="As teacher on what topic make quiz with mcq and u need to generate by questionnand 4 chice and correct index",
                parameters={
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "choice_": {"type": "string"},
                        "choice_2": {"type": "string"},
                        "choice_3": {"type": "string"},
                        "choice_4": {"type": "string"},
                        "correct_index": {"type": "integer"},
                    },
                    "required": ["question", "choice_", "choice_2", "choice_3", "choice_4", "correct_index"]
                }
            ),
            types.FunctionDeclaration(
                name="MakePoll",
                description="Create a poll for students and thisis to make some descision on specific area that is send to the department if it is more that 80 vote",
                parameters={
                    "type": "object",
                    "properties": {
                        "doing": {"type": "string"},
                    },
                    "required": ["doing"]
                }
            ),
        ]
    )
]
while True:
    input_text = input("Enter your request: ")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Yout are ai agent class representative in university, for It Studente and your name is RepIt and you build to make and the user asks you this {input_text} answer frendly from the tool if ot say today date is this context {date} and today is {date_name} and tools is also {tools}",
        
            
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
        # print("Arguments:", dict(fc.args))
        # if fc.name == "SceduleClass":
        # SceduleClass(**fc.args)
    # args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    # fc = part.function_call
    # print("Function name:", fn.name)
    # print("Arguments:", fn.args)

# print(response.text)