import asyncio
import logging
import re
import group_games
# from config_reader import config
from my_token import TOKEN
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command,CommandObject, CommandStart
from aiogram.types import Message,FSInputFile, URLInputFile, BufferedInputFile, LinkPreviewOptions
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.markdown import hide_link





logging.basicConfig(level = logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_routers(group_games.router)
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")


@dp.message(Command('start'))
async def cmd_hello(message: Message):
    
    await message.answer(
        f"Приветствую на нашем сервере, <b>{message.from_user.full_name}</b>",
            parse_mode=ParseMode.HTML
    
    )
    kb = [
        [types.KeyboardButton(text="commands")],
        [types.KeyboardButton(text="help")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("выбирите 'commands' что бы просмотреть, что умеет этот бот", reply_markup=keyboard ),
    await message.answer('выбирите "help" что бы понять, как использовать команды', reply_markup=keyboard)







@dp.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'book_(\d+)'))
))
async def cmd_start_book(
        message: Message,
        command: CommandObject
):
    book_number = command.args.split("_")[1]
    await message.answer(f"Sending book №{book_number}")






@dp.message(Command('images'))
async def upload_photo(message: Message):
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться
    file_ids = []


    with open("buffer_emulation.jpg", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="image from buffer.jpg"
            ),
            caption="наш слоняра"
        )
        file_ids.append(result.photo[-1].file_id)




    # Отправка файла из файловой системы
    image_from_pc = FSInputFile("image_from_pc.jpg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    # Отправка файла по ссылке
    image_from_url = URLInputFile("https://picsum.photos/seed/groosha/400/300")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("Отправленные файлы:\n"+"\n".join(file_ids))





@dp.message(Command("link"))
async def cmd_links(message: Message):
    links_text = (
        "https://eyes.nasa.gov/apps/solar-system/#/home"
        "\n"
        "https://t.me/telegram"
    )
    options_3 = LinkPreviewOptions(
        url="https://eyes.nasa.gov/apps/solar-system/#/home",
        prefer_large_media=True
    )
    await message.answer(
        f"Большое превью\n{links_text}",
        link_preview_options=options_3
    )





from aiogram.utils.markdown import hide_link

@dp.message(Command("hidden_link"))
async def cmd_hidden_link(message: Message):
    await message.answer(
        f"{hide_link('https://memepedia.ru/bobr-kurva/')}"
        f"бобер курва: *существует*\n"
        f"Пользователи: *не знают мем*\n"
        f"бобер:"
    )




@dp.message(Command("gif"))
async def send_gif(message: Message):
    await message.answer_animation(
        animation="<file_id гифки>",
        caption="Я сегодня:",
        show_caption_above_media=True
    )






@dp.message(F.text.lower() == "commands")
async def with_puree(message: types.Message):
    await message.answer('на данный момент доступны команды,\n такие как: images - вывод картинки,\n reply_builder - выбор чисел от 1 до 9,\n dice - подброс кубика,\n info  - информация о том, когда был запущен бот,\n link - переход по ссылке,\n hidden_link -  сообщение без ссылки,\n random - выводится любое число от 1 - 1000000')

@dp.message(F.text.lower() == "help")
async def without_puree(message: types.Message):
    await message.answer("все команды вводятся через '/', если команда не работает, проверьте ее написание")












@dp.message(Command("reply_builder"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await message.answer(
        "Выберите число от 1 до 9:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    kb = [
        [types.KeyboardButton(text="commands")],
        [types.KeyboardButton(text="help")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )




@dp.message(F.text.lower() == "1")
async def without_puree(message: types.Message):
    await message.answer("абоба")

@dp.message(F.text.lower() == "2")
async def without_puree(message: types.Message):
    await message.answer("бобер")

@dp.message(F.text.lower() == "3")
async def without_puree(message: types.Message):
    await message.answer("квадробер")

@dp.message(F.text.lower() == "4")
async def without_puree(message: types.Message):
    await message.answer("пес")

@dp.message(F.text.lower() == "5")
async def without_puree(message: types.Message):
    await message.answer("кот")

@dp.message(F.text.lower() == "6")
async def without_puree(message: types.Message):
    await message.answer("слоняра")

@dp.message(F.text.lower() == "7")
async def without_puree(message: types.Message):
    await message.answer("чебурек")

@dp.message(F.text.lower() == "8")
async def without_puree(message: types.Message):
    await message.answer("raw")

@dp.message(F.text.lower() == "9")
async def without_puree(message: types.Message):
    await message.answer("pipipypychek")


@dp.message(Command('answer'))
async def cmd_answer(message: types.Message):
    await message.answer("простое сообщение")
@dp.message(Command('reply'))
async def cmd_reply(message: types.Message):
    await message.reply("сообщение с ответом на сообщение")

@dp.message(Command('dice'))
async def cmd_answer(message: types.Message):
    await message.answer_dice("emoji=🎲")

@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(4)
    await message.answer("Добавлено число 4")

@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")

@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")




async def main():

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=[1, 2, 3])



if __name__ == "__main__":
    asyncio.run(main())