from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart,Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyborts as kb 
from states import Register

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!',reply_markup=kb.main)
    await message.reply("Как дела?")

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer ('Ты бля запутался?')

@router.message(F.text=='Каталог')
async def catalog(message:Message):
    await message.answer ('выберите категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data=='t-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Переход в категорию футболки')# уведомление
    await callback.message.answer('Переход в категорию футболки')# сообщение

@router.message(Command('rigister'))
async def rigister(message:Message, state : FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')


@router.message(Register.name)
async def register_name(message:Message,state:FSMContext):
    await state.update_data(name=message.txt)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')
    
@router.message(Register.age)
async def register_age(message:Message,state:FSMContext):
    await state.update_data(age=message.txt)
    await state.set_state(Register.number)
    await message.answer('Введите ваш возраст')
    