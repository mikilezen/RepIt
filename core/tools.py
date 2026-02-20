from google.genai import types

def get_tools():
    return [
        types.Tool(
            function_declarations=[

                types.FunctionDeclaration(
                    name="CheckUser",
                    description="Check user role",
                    parameters={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string"}
                        }
                    }
                ),

                types.FunctionDeclaration(
                    name="CancelClass",
                    description="Cancel scheduled class",
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
                    description="Schedule or postpone class",
                    parameters={
                        "type": "object",
                        "properties": {
                            "R_number": {"type": "string"},
                            "start": {"type": "string"},
                            "end": {"type": "string"},
                            "case": {"type": "string"},
                            "course": {"type": "string"}
                        },
                        "required": ["R_number", "start", "end", "course"]
                    }
                ),

                types.FunctionDeclaration(
                    name="ShowSchedule",
                    description="Show weekly schedule",
                    parameters={
                        "type": "object",
                        "properties": {
                            "date": {"type": "string"}
                        },
                        "required": ["date"]
                    }
                ),

                types.FunctionDeclaration(
                    name="ShowClassForToday",
                    description="Show today classes",
                    parameters={
                        "type": "object",
                        "properties": {
                            "date": {"type": "string"},
                            "today": {"type": "string"}
                        },
                        "required": ["date", "today"]
                    }
                ),

                types.FunctionDeclaration(
                    name="MakeQuiz",
                    description="Generate MCQ quiz",
                    parameters={
                        "type": "object",
                        "properties": {
                            "question": {"type": "string"},
                            "choice_1": {"type": "string"},
                            "choice_2": {"type": "string"},
                            "choice_3": {"type": "string"},
                            "choice_4": {"type": "string"},
                            "correct_index": {"type": "integer"},
                        },
                        "required": ["question", "choice_1", "choice_2", "choice_3", "choice_4", "correct_index"]
                    }
                ),

                types.FunctionDeclaration(
                    name="MakePoll",
                    description="Create poll for student decision",
                    parameters={
                        "type": "object",
                        "properties": {
                            "doing": {"type": "string"}
                        },
                        "required": ["doing"]
                    }
                ),
            ]
        )
    ]
