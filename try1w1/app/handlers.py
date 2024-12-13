from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from aiogram import F, Router

import app.keyborts as kb 

router=Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!',reply_markup=kb.main)
    await message.reply("Как дела?")

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer ('Ты бля запутался?')




    