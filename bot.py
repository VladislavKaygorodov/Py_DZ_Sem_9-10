import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from pytube import YouTube

import os, glob
import uuid

btn1 = KeyboardButton('Видео')
btn2 = KeyboardButton('Только аудио')
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)


API_TOKEN = '5743026318:AAF1YxA8dZcoZ53b_pVQZwCG429t2raigus'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Привет!\n Я бот который умеет скачивать видео с youtube.com\nПросто скинь ссылку в чат" )


@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text

    if msg[0:24] == "https://www.youtube.com/":
        await message.answer("Выбери тип скачиваемого файла", reply_markup=menu)
        msg_link = msg
        with open('link.txt', 'w') as file:
            for i in msg_link:
                file.write(str(i))
        link = YouTube(msg_link)
        await message.answer(f'Хочешь скачать: {link.title}?')

    elif message.text == 'Видео':
        video_link = ''
        with open('link.txt', 'r') as file:
            for line in file:
                video_link = line
        print(video_link)
        save_video = YouTube(video_link)
        video_id = uuid.uuid4().fields[-1]
        save_video.streams.filter(file_extension='mp4').first().download("video", f"{video_id}.mp4")

        video = open(f'C:\\Users\\kaygo\\Desktop\\Учеба\\Python\\Py_DZ_Sem_10\\video\\{video_id}.mp4', 'rb')
        await bot.send_video(message.chat.id, video)

        for file in glob.glob("video/*"):
            os.remove(file)
        print("Deleted " + str(file))

    elif message.text == 'Только аудио':
        audio_link = ''
        with open('link.txt', 'r') as file:
            for line in file:
                audio_link = line
        print(audio_link)
        save_audio = YouTube(audio_link)
        audio_id = uuid.uuid4().fields[-1]
        save_audio.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")

        audio = open(f'C:\\Users\\kaygo\\Desktop\\Учеба\\Python\\Py_DZ_Sem_10\\audio\\{audio_id}.mp3', 'rb')
        await bot.send_audio(message.chat.id, audio)

        for file in glob.glob("audio/*"):
            os.remove(file)
        print("Deleted " + str(file))

    else:
        await message.answer("Пропуск")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    