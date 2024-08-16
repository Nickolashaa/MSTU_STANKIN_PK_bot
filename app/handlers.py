from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
import os
from dotenv import load_dotenv
from app.files.librian import *
import app.keyboards as kb

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

cnt = [0]

file = [""]


class Stalker(StatesGroup):
    points = State()


class Question(StatesGroup):
    name = State()
    number = State()
    text = State()


class Answer(StatesGroup):
    number = State()
    text = State()
    push = State()


class BackText(StatesGroup):
    text = State()


class Delete(StatesGroup):
    number = State()


class RetextPassword(StatesGroup):
    text = State()


class Retext(StatesGroup):
    name = State()
    text = State()


@dp.callback_query(F.data == 'cancel')
async def hello(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.answer('')
    await call.message.answer('Заявка отменена', reply_markup=await kb.to_main())


@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("OK")


@dp.callback_query(F.data == 'back_to_main')
async def start(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Начальное сообщение.txt'), reply_markup=kb.main, parse_mode="Markdown")


@dp.message(Command('menu'))
@dp.message(CommandStart())
async def start(message: Message):
    if ban_check(f"@{message.from_user.username}"):
        add_to_full_stat("start")
        await message.answer(txt_to_str('Начальное сообщение.txt'), reply_markup=kb.main, parse_mode="Markdown")
        stat = get_stat()
        if message.from_user.username not in stat["members"]:
            await bot.send_message(chat_id=int(os.getenv("Log_id")), text=f"New member: @{message.from_user.username}")
        new_member(message.from_user.username)
    else:
        await message.answer('Извините, вы в черном списке')


@dp.callback_query(F.data == 'direction')
async def direction_group_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Выбор углубленной группы.txt'), reply_markup=kb.direction_group,
                                 parse_mode="Markdown")
    add_to_full_stat("Узнать о направлениях подготовки")


@dp.callback_query(F.data == '01')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('01'),
                                 parse_mode="Markdown")
    add_to_full_stat("01")


@dp.callback_query(F.data == '09')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('09'),
                                 parse_mode="Markdown")
    add_to_full_stat("09")


@dp.callback_query(F.data == '12')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('12'),
                                 parse_mode="Markdown")
    add_to_full_stat("12")


@dp.callback_query(F.data == '15')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('15'),
                                 parse_mode="Markdown")
    add_to_full_stat("15")


@dp.callback_query(F.data == '20')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('20'),
                                 parse_mode="Markdown")
    add_to_full_stat("20")


@dp.callback_query(F.data == '22')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('22'),
                                 parse_mode="Markdown")
    add_to_full_stat("22")


@dp.callback_query(F.data == '27')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('27'),
                                 parse_mode="Markdown")
    add_to_full_stat("27")


@dp.callback_query(F.data == '38')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('38'),
                                 parse_mode="Markdown")
    add_to_full_stat("38")


@dp.callback_query(F.data.contains('.txt'))
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    cods = get_cods()
    for cod in cods:
        if cod in call.data:
            url = txt_to_str(cod, True)[txt_to_str(cod, True).rindex('-') + 2:]
            text = txt_to_str(cod, True)[:txt_to_str(cod, True).index('!') + 1]
            await call.message.answer(text, reply_markup=await kb.to_main(url=url), parse_mode="Markdown")
            break


@dp.callback_query(F.data == 'home')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.delete()
    file = FSInputFile('app/files/images/photo_2024-06-25_07-07-46.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('Про общежития.txt'), reply_markup=await kb.to_main(
        text='Регламент', url="https://priem.stankin.ru/obshchezhitie/"))
    add_to_full_stat("Общежитие")


@dp.callback_query(F.data == 'career')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Центр карьеры.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")
    add_to_full_stat("Центр карьеры СТАНКИНА")


@dp.callback_query(F.data == 'contacts')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Контакты.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")
    add_to_full_stat("Контакты")


@dp.callback_query(F.data == 'SPO')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('СПО_1.txt'), reply_markup=kb.SPO, parse_mode="Markdown")
    add_to_full_stat("У меня диплом СПО, как мне поступить")


@dp.callback_query(F.data == 'exams_how_much')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Какой экз сдавать после СПО.txt'), reply_markup=kb.SPO,
                                 parse_mode="Markdown")


@dp.callback_query(F.data == 'exams_how')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('СПО_2.txt'), reply_markup=kb.SPO, parse_mode="Markdown")


@dp.callback_query(F.data == 'СТАНКИН')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давайте расскажу о моем университете', reply_markup=kb.STANKIN, parse_mode="Markdown")
    add_to_full_stat("О нашем вузе")


@dp.callback_query(F.data == 'dop')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Я могу рассказать про многое :)', reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'modul')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/images/6leqhrt4p9y-1024x626.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('Модульная система.txt'), reply_markup=kb.STANKIN,
                                    parse_mode="Markdown")


@dp.callback_query(F.data == 'rate')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/images/photo_2024-07-25_00-39-33.jpg')
    await call.message.answer_photo(file)
    await call.message.answer(text=txt_to_str('Рейтинговая система.txt'), reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'VUC')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('ВУЦ.txt'), reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'volonter')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    volonetrs = [
        InputMediaPhoto(media=FSInputFile('app/files/images/0GYSpy4WiPc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/AWgELDlY7do.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/E-im7qZzEGU.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/tWi5R0nKfy0.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(volonetrs)
    await call.message.answer(txt_to_str('Клуб волонтеров.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'cyber')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    cybers = [
        InputMediaPhoto(media=FSInputFile('app/files/images/vJ4YtqdvqeA.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/YTTJl9qnp0s.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/zkhYjV0R2ys.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(cybers)
    await call.message.answer(txt_to_str('Кибер_клуб.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'club')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/images/uwY3uEqgWGk.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('Клуб.txt'), reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'tip-top')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/images/4aijGPUSJgo.jpg')
    await call.message.answer_photo(file, caption='Фото с выступления группы tip-top', reply_markup=kb.CLUB,
                                    parse_mode="Markdown")


@dp.callback_query(F.data == 'dance')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    dances = [
        InputMediaPhoto(media=FSInputFile('app/files/images/CDyp87Mg9Vc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/RfxdXh8YXmc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/WNxCT-89Ni8.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/ynCTEkVNq4c.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(dances)
    await call.message.answer('Выступления танцоров', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'vocal')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    vocals = [
        InputMediaPhoto(media=FSInputFile('app/files/images/q-tx_UDvgH0.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/TW92znbSsIo.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/x6zIDxVvp_4.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/xMvq7I4SZTg.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(vocals)
    await call.message.answer('Выступления вокалистов', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'bolt')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    bolts = [
        InputMediaPhoto(media=FSInputFile('app/files/images/Ld1P3UUGPGk.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/kvMLvsGXZKE.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/oSIZ2qSLnts.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/uf3-XTsSs1Y.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/UhaUIUDSlXk.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/images/XK_z1yb4PcE.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(bolts)
    await call.message.answer('Фото с выступления Станкиновкого болта', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'other_clubs')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Другие клубы.txt'), reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'prof')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Профком.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'ya_loh')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Перевод на другие направления.txt'), reply_markup=await kb.to_main(),
                              parse_mode="Markdown")
    add_to_full_stat("Что делать, если не пройду туда, куда хочу")


@dp.callback_query(F.data == 'build')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Всего СТАНКИН имеет 3 корпуса и 1 филиал', reply_markup=kb.BUILD,
                                 parse_mode="Markdown")


@dp.callback_query(F.data == 'osnov')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Вадковский.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'frez')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Фрезер.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'libr')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Библиотека.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'egor')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Егорьевский филиал.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'how_docs')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Вот все варианты подачи документов', reply_markup=kb.VARIANTS, parse_mode="Markdown")
    add_to_full_stat("Как подать документы")


@dp.callback_query(F.data == 'ochn')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Очная подача документов.txt'), reply_markup=kb.VARIANTS,
                                 parse_mode="Markdown")


@dp.callback_query(F.data == 'dist')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Подача документов СДПД.txt'), reply_markup=kb.VARIANTS_2,
                                 parse_mode="Markdown")


@dp.callback_query(F.data == 'post')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('Подача документов почтой России.txt'), reply_markup=kb.VARIANTS,
                                 parse_mode="Markdown")


@dp.callback_query(F.data == 'chances')
async def direction_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await state.set_state(Stalker.points)
    await call.message.answer('Введите сумму ваших баллов ЕГЭ (Например: 255)')
    add_to_full_stat("Узнать шансы на поступление")


@dp.message(Stalker.points)
async def direction_callback(message: Message, state: FSMContext):
    await state.update_data(points=message.text)
    await state.set_state(Stalker.points)
    data = await state.get_data()
    await state.clear()
    cods = get_cods()
    result = "Исходя из данных на 2023 год, вы бы прошли на направления:\n"
    for cod in cods:
        if cod != '01.03.04.txt' and cod != '22.03.01.txt':
            with open(f'app/files/directions/{cod}', 'r', encoding='utf-8') as f:
                res = f.read()
                f.close()
            point = int(res[res.index('-') + 2:res.index('-') + 5])
            if point <= int(data["points"]):
                result += f"{res[:res.index(':')]}\n\n"
    result += 'Отслеживайте свое положение в списках нашего сайте'
    await message.answer(result, reply_markup=await kb.to_main(text='Списки к приказу',
                                                               url='https://priem.stankin.ru/bakalavriatispetsialitet/ranked-lists-ext/?order=1'),
                         parse_mode="Markdown")


@dp.callback_query(F.data == 'rules')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давай разберемся', reply_markup=kb.RULES, parse_mode="Markdown")
    add_to_full_stat("Правила приема")


@dp.callback_query(F.data == 'lgot')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Выбираем льготу', reply_markup=kb.LGOTI, parse_mode="Markdown")


@dp.callback_query(F.data == 'celev')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Целевая квота.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")
    add_to_full_stat("Целевая квота")


@dp.callback_query(F.data == 'osob')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Особая квота.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")
    add_to_full_stat("Особая квота")


@dp.callback_query(F.data == 'otd')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Отдельная квота.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")
    add_to_full_stat("Отдельная квота")


@dp.callback_query(F.data == 'vstupi')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Кто может сдавать вступы после СПО.txt'), reply_markup=kb.RULES,
                              parse_mode="Markdown")
    add_to_full_stat("Кто может писать вступительные экзамены?")


@dp.callback_query(F.data == 'prior')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/Преимущественное право.txt')
    await call.message.answer_document(file,
                                       caption=txt_to_str('Описание приоритетного зачисления.txt'),
                                       reply_markup=kb.RULES, parse_mode="Markdown")
    add_to_full_stat("Что такое приоритетное зачисление")


@dp.callback_query(F.data == 'sys_prior')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Система приоритетов.txt'),
                              reply_markup=await kb.to_main(text='Ранжированные списки',
                                                            url='https://priem.stankin.ru/bakalavriatispetsialitet/ranked-lists/'),
                              parse_mode="Markdown")
    add_to_full_stat("Как работает система приоритетов")


@dp.callback_query(F.data == 'ogranich')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Ограничения на подачу документов.txt'), reply_markup=kb.RULES,
                              parse_mode="Markdown")
    add_to_full_stat("Ограничения на подачу заявления")


@dp.callback_query(F.data == 'ball')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Как формируется конкурсный балл.txt'), reply_markup=kb.RULES,
                              parse_mode="Markdown")
    add_to_full_stat("Как формируется конкурсный балл")


@dp.callback_query(F.data == 'min_ball')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давай разберемся', reply_markup=kb.VIBOR, parse_mode="Markdown")
    add_to_full_stat("Минимальные баллы для подачи заявления")


@dp.callback_query(F.data == 'e')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Минимальные баллы ЕГЭ.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 's')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Минимальные баллы СПО.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'calc')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(f"Калькулятор индивидуальных баллов")
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")
    add_to_full_stat("Калькулятор индивидуальных достижений")


@dp.callback_query(F.data.contains('b+'))
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    res = int(call.data[2:])
    cnt[0] = min(10, cnt[0] + res)
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")


@dp.callback_query(F.data == 'b//0')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    cnt[0] = 0
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")


@dp.callback_query(F.data == 'spiski')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Найти себя в списках легко!', reply_markup=kb.SPISKI, parse_mode="Markdown")
    add_to_full_stat("Как найти себя в списках")


@dp.callback_query(F.data == 'kab')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(
        txt_to_str('Личный кабинет.txt'),
        reply_markup=await kb.to_main(text='Личный кабинет', url='https://info.stankin.ru/lk/login'),
        parse_mode="Markdown")


@dp.callback_query(F.data == 'rang')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(
        txt_to_str('Списки к приказам.txt'),
        reply_markup=
        await kb.to_main(text='Списки к приказу',
                         url='https://priem.stankin.ru/bakalavriatispetsialitet/ranked-lists-ext/?order=1'),
        parse_mode="Markdown")


@dp.callback_query(F.data == 'at')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('Оригинал аттестата.txt'), reply_markup=await kb.to_main(),
                              parse_mode="Markdown")


@dp.message(Command('stat'))
async def direction_callback(message: Message):
    stat = get_stat()
    await message.answer(f"Всего ботом пользовались {stat['cnt']} раз")


@dp.callback_query(F.data == 'q1')
async def question_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await call.message.answer('Хорошо, я создам заявку, которую передам сотрудникам приемной комиссии')
    await call.message.answer('Как мы можем к вам обращаться? (ФИО)', reply_markup=kb.CANCEL)
    await state.set_state(Question.name)


@dp.message(Question.name)
async def question_callback2(message: Message, state: FSMContext):
    if ban_check(f"@{message.from_user.username}"):
        await state.update_data(name=message.text)
        await message.answer('Напишите, пожалуйста, ваш номер телефона', reply_markup=kb.CANCEL)
        await state.set_state(Question.number)
    else:
        await message.answer('Извините, вы в черном списке')
        await state.clear()


@dp.message(Question.number)
async def question_callback2(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer('Опишите вашу проблему одним сообщением, можете прикрепить скриншот, если это необходимо',
                         reply_markup=kb.CANCEL)
    await state.set_state(Question.text)


@dp.message(Question.text)
async def question_callback2(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    s = txt_to_str('Шаблон.txt')
    num = new_task_num()
    s = s.replace('"0"', str(num))
    if message.photo is not None:
        s = s.replace('"1"', str(data['name']))
        s = s.replace('"2"', f"@{message.from_user.username}")
        s = s.replace('"3"', str(data['number']))
        s = s.replace('"4"', message.caption)
        await bot.send_photo(photo=message.photo[-1].file_id, caption=s, chat_id=int(os.getenv("Call_center_id")), reply_markup=kb.TASK)
        new_task(message.chat.id, num, message.caption)
    else:
        s = s.replace('"1"', str(data['name']))
        s = s.replace('"2"', f"@{message.from_user.username}")
        s = s.replace('"3"', str(data['number']))
        s = s.replace('"4"', str(data['text']))
        await bot.send_message(text=s, chat_id=int(os.getenv("Call_center_id")), reply_markup=kb.TASK)
        new_task(message.chat.id, num, str(data['text']))
    await message.answer('Ваша заявка передана и будет отвечена сотрудниками в ближайшее время',
                         reply_markup=await kb.to_main())


@dp.callback_query(F.data == "task")
async def task_callback(call: CallbackQuery):
    await call.answer('')
    await bot.set_message_reaction(call.message.chat.id,
                                   call.message.message_id,
                                   reaction=[{"type": "emoji", "emoji": "❤️"}])
    if call.message.text is not None:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
    else:
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    caption=call.message.caption)
    master_char_id = int(call.from_user.id)
    await bot.send_message(chat_id=master_char_id,
                           text='Режим модератора', reply_markup=kb.MODER)


@dp.message(Command("task"))
async def task_handler(message: Message, state: FSMContext):
    await state.set_state(Answer.number)
    await message.answer('Введите номер заявки')


@dp.callback_query(F.data == 'write')
async def task_handler(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await state.set_state(Answer.number)
    await call.message.edit_text('Введите номер заявки')


@dp.message(Answer.number)
async def task_handler(message: Message, state: FSMContext):
    try:
        await state.update_data(number=int(message.text))
        await state.set_state(Answer.text)
        tasks = all_task()
        await message.answer(f"Заявка №{message.text}\n{tasks[message.text][1]}")
        await message.answer('Введите ваш ответ на заявку')
    except:
        await message.answer("Возникла ошибка, проверьте номер заявки", reply_markup=kb.MODER)
        await state.clear()


@dp.message(Answer.text)
async def task_handler(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(Answer.push)
    await message.answer("Если вы уверены, что заявка обработана без ошибок, напишите 'ДА'")


@dp.message(Answer.push)
async def task_handler(message: Message, state: FSMContext):
    await state.update_data(push=message.text)
    data = await state.get_data()
    await state.clear()
    try:
        if data["push"] == "ДА":
            ab_id = int(search_task(int(data["number"]))[0])
            await bot.send_message(chat_id=ab_id, text="Доброго времени суток! Мы готовы ответить на ваш вопрос!\n")
            await bot.send_message(chat_id=ab_id, text=data['text'], reply_markup=kb.BACK_OR_FEEDBACK)
            tasks = all_task()
            num = data['number']
            first = tasks[str(data['number'])][1]
            second = data['text']
            third = message.from_user.username
            fourth = message.from_user.first_name
            log = f"Ответ на заявку №{num}\n{first}\n\n{second}\n\nОтветственный: @{third}\n{fourth}"
            print(int(os.getenv("Log_id")))
            await bot.send_message(chat_id=int(os.getenv("Log_id")), text=log)
            delete_task(data["number"])
            await message.answer('Заявка обработана без ошибок, проверьте наличие сердечка в беседе')
        else:
            await message.answer("Ответ на заявку отменен")
    except:
        await message.answer('Возникла ошибка, проверьте номер заявки', reply_markup=kb.MODER)


@dp.callback_query(F.data == 'feedback')
async def feedback_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await state.set_state(BackText.text)
    await call.message.answer("Напишите ваш отзыв")


@dp.message(BackText.text)
async def task_handler(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer('Большое спасибо за обратную связь!\nЕсли ваш вопрос остался нерешенным, свяжитесь с нами по '
                         'горячей линии приемной комиссии, номер в вкладке КОНТАКТЫ')
    await message.answer(text=txt_to_str("Начальное сообщение.txt"), parse_mode="Markdown", reply_markup=kb.main)
    one = data["text"]
    two = message.from_user.username
    three = message.from_user.first_name
    log = f"Отзыв\n\n{one}\n\nАвтор: @{two}\n{three}"
    await bot.send_message(chat_id=int(os.getenv("Log_id")), text=log)


@dp.message(Command('ban'))
async def banned(message: Message):
    name = message.from_user.username
    if admin_check(f"@{name}"):
        ban(message.text[5:])


@dp.message(Command('hhh'))
async def hello(message: Message):
    print(message)
    await message.answer(txt_to_str("Тест.txt"))


@dp.message(Command('mod1930'))
async def mod1930(message: Message):
    await message.delete()
    await message.answer("Режим модератора", reply_markup=kb.MODER)


@dp.message(Command('all_tasks'))
async def hello(message: Message):
    result = all_task()
    if len(result.keys()) == 0:
        await message.answer('Заявок нет')
    else:
        s = ""
        for number in result.keys():
            item = result[number][1]
            s += f"Заявка №{number}\n{item}\n\n"
        await message.answer(s, reply_markup=kb.MODER)


@dp.callback_query(F.data == 'look')
async def hello(call: CallbackQuery):
    await call.answer('')
    result = all_task()
    if len(result.keys()) == 0:
        await call.message.answer('Заявок нет')
    else:
        s = ""
        for number in result.keys():
            item = result[number][1]
            s += f"Заявка №{number}\n{item}\n\n"
        await call.message.edit_text(s, reply_markup=kb.MODER)


@dp.message(Command('delete'))
async def delete(message: Message, state: FSMContext):
    await state.set_state(Delete.number)
    await message.answer("№ заявки")


@dp.message(Delete.number)
async def delete(message: Message, state: FSMContext):
    try:
        delete_task(str(message.text))
        await message.answer("Успешно")
    except:
        await message.answer("Ошибка")
    finally:
        await state.clear()


@dp.callback_query(F.data == "green")
async def green(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str("Зеленая зона.txt"), parse_mode="Markdown", reply_markup=kb.RULES)
    add_to_full_stat("Что такое зеленая зона")


@dp.callback_query(F.data == 'upper_prior')
async def upper_prior(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str("Высший приоритет.txt"), parse_mode="Markdown", reply_markup=kb.RULES)
    add_to_full_stat("Что такое высший приоритет")


@dp.callback_query(F.data == 'retext')
async def retext(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await state.set_state(RetextPassword.text)
    await call.message.edit_text("password...")


@dp.message(RetextPassword.text)
async def retext(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    login = f"@{message.from_user.username}"
    if data["text"] == "1930":
        await message.answer("Принято")
        await message.answer("‼️Редактирование корневых файлов‼️")
        all_files = get_files()
        msg = ""
        for key in all_files.keys():
            msg += f"{key}\n"
        await message.answer(msg)
        await state.set_state(Retext.name)
    else:
        await message.answer("Отклонено")
        await bot.send_message(text=f"Нарушитель {login}", chat_id=int(os.getenv("My_id")))


@dp.message(Retext.name)
async def retext(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    if message.text in get_files().keys():
        for key in get_files().keys():
            if message.text == key:
                file = open_file(get_files()[key])
                await message.answer(file)
                await message.answer("Введите текст для ЗАМЕНЫ файла")
                await state.set_state(Retext.text)
                break
    else:
        await state.clear()
        await message.answer("Error")


@dp.message(Retext.text)
async def retext(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    text = data["text"]
    all_files = get_files()
    path = all_files[data["name"]]
    write_file(path, text)
    await message.answer("Выполнено")


@dp.message(Command("full_stat"))
async def full_stat(message: Message):
    stat = get_full_stat()
    text = str()
    for key in stat.keys():
        item = stat[key]
        text += f"{key}: {item}\n"
    await message.answer(text)


@dp.callback_query(F.data == "pobeda")
async def win(call: CallbackQuery):
    await call.message.edit_text(txt_to_str("Конец всего.txt"), reply_markup=await kb.to_main())
    add_to_full_stat("Я поступил, что дальше?")


@dp.message()
async def hello(message: Message):
    await message.answer("Извините, но функция ответа в чате пока не работает 😔. Но вы можете поискать ответ на свой "
                         "вопрос, написав /menu, если ответ не найдется оставьте заявку воспользовавшись 'Хочу задать"
                         " вопрос'")
