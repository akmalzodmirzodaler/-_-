from aiogram import Router, types
from aiogram.filters import Command
from .quiz import load_quiz_questions
from .qa import QASystem

router = Router()

# Global QA system
qa_system = QASystem(api_key="your_openai_api_key")

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот для изучения законодательства Республики Таджикистан. Выберите: /quiz для тестов или задайте вопрос.")

@router.message(Command("quiz"))
async def quiz_command(message: types.Message):
    questions = load_quiz_questions()
    # Implement quiz logic
    await message.reply("Тесты в разработке.")

@router.message()
async def handle_question(message: types.Message):
    answer = qa_system.search(message.text)
    await message.reply(answer)