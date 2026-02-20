class RepItAgent:

    def __init__(self, ai_client, tools):
        self.ai = ai_client
        self.tools = tools

    def run(self, user_input, context):
        prompt = f"""
        You are RepIt AI class representative for IT students.
        Today is {context['date']} ({context['day']}).
        User request:
        {user_input}
        Use tools only when action is required."""
        response = self.ai.generate(prompt, self.tools)
        parts = response.candidates[0].content.parts
        results = []

        for part in parts:
            if hasattr(part, "function_call") and part.function_call:
                results.append(("function", part.function_call))
            else:
                results.append(("text", part.text))

        return results
 