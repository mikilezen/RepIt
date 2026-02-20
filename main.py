from core.ai_client import GeminiClient
from core.tools import get_tools
from core.agents import RepItAgent
import time

context = {
    "date": time.strftime("%Y-%m-%d"),
    "day": time.strftime("%A")
}

ai_client = GeminiClient()
tools = get_tools()
agent = RepItAgent(ai_client, tools)

while True:
    user_input = input("👨‍🎓 You: ")
    outputs = agent.run(user_input, context)

    for typ, data in outputs:
        if typ == "text":
            print("🤖 RepIt:", data)
        else:
            print("⚙ Function:", data.name)
            print("📦 Args:", data.args)



# import logging
# import google.generativeai as genai
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# # --- CONFIGURATION ---
# # Replace with your Gemini API Key from https://aistudio.google.com/
# GEMINI_API_KEY = "AIzaSyDHrFQxSA9zHLJxvnVTGKpuizNgfOwn2EM"
# TELEGRAM_TOKEN = "8315125873:AAGsCI_wd7KOn0IXfA1ZBrO82JWZIDSsYR4"

# # Configure Gemini
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel('gemini-2.5-flash')

# # --- USER ROLES ---
# ADMINS = [2116090154]
# TEACHERS = {2116090154: 'miikiki'}
# STUDENTS = {8428924924: 'telegram id'}

# logging.basicConfig(level=logging.INFO)

# def get_user_role(user_id):
#     if user_id in ADMINS: return "Admin"
#     if user_id in TEACHERS: return "Teacher"
#     if user_id in STUDENTS: return "Student"
#     return None

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     role = get_user_role(user_id)
#     if role:
#         await update.message.reply_text(f"Access granted. Role: **{role}**. How can I help?")
#     else:
#         await update.message.reply_text("⛔ Unauthorized. Your ID is not on the list.")

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     role = get_user_role(user_id)

#     if not role:
#         return

#     user_text = update.message.text
#     await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

#     try:
#         # Create a prompt that includes the user's role for a "based" response
#         prompt = f"System Instruction: You are a based AI agent. The user is a {role}. Respond to: {user_text}"
        
#         response = model.generate_content(prompt)
#         await update.message.reply_text(response.text)
        
#     except Exception as e:
#         logging.error(f"Gemini Error: {e}")
#         await update.message.reply_text("My AI circuits are fried. Check the API key.")

# if __name__ == '__main__':
#     application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
#     application.add_handler(CommandHandler('start', start))
#     application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
#     print("Gemini Agent is running...")
#     application.run_polling()