import asyncio
from dotenv import load_dotenv
from aiogram import Dispatcher, Router, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject
from connection import create_table
from service import *
import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Показать пользователей")],
        [KeyboardButton(text="➕ Добавить задачу")],
    ],
    resize_keyboard=True,
)

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token)
dp = Dispatcher()


@dp.message(Command("start"))
async def startbot(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer(f"Hello {message.from_user.first_name} dear! 😀", reply_markup=main_kb)
    else:
        await save_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer(f"Hello {message.from_user.first_name} dear! 😀",  reply_markup=main_kb)
        
    
    

@dp.message(Command("help"))
async def startbot(message: Message):
    await message.answer(f"""
Menu helps             
Команды:
/start для запуска бота
                 
                         """)



@dp.message(Command("add_task"))
async def startbot(message: Message, command: CommandObject):
    task=command.args
    task= task.split("/")
    print(task)
    await message.answer(f"You entered {task}")


@dp.message(F.text == "📋 Показать пользователей")
@dp.message(Command("show_user"))
async def show_users(message: Message):
    users = await get_all_user()
    text = ""
    for user in users:
        text+=f"""
\nUser {user['user_id']}
Username {user['username']} 
Full name {user['full_name']} 
telegram id {user['telegram_id']}
        """
    await message.answer(text)
        


async def main():
    print("Start Bot")
    await create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())