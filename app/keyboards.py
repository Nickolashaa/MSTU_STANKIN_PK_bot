from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.files.librian import *

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я поступил, что дальше? 🥳', callback_data='pobeda')],
    [InlineKeyboardButton(text='Узнать о направлениях подготовки 🎓', callback_data='direction')],
    [InlineKeyboardButton(text='Правила приема 📖', callback_data='rules')],
    [InlineKeyboardButton(text='Как подать документы 📑', callback_data='how_docs')],
    [InlineKeyboardButton(text='Общежитие 🏡', callback_data='home')],
    [InlineKeyboardButton(text='Узнать шансы на поступление ❓', callback_data='chances')],
    [InlineKeyboardButton(text='У меня диплом СПО, как мне поступить 👨‍🎓', callback_data='SPO')],
    [InlineKeyboardButton(text='Как найти себя в списках? 🧐', callback_data='spiski')],
    [InlineKeyboardButton(text='Что делать, если не пройду туда, куда хочу 🥺', callback_data='ya_loh')],
    [InlineKeyboardButton(text='Центр карьеры СТАНКИНА 🔧', callback_data='career')],
    [InlineKeyboardButton(text='О нашем вузе 👩‍🏫', callback_data='СТАНКИН')],
    [InlineKeyboardButton(text='Контакты 📞', callback_data='contacts'),
     InlineKeyboardButton(text='Хочу задать вопрос 👩‍💻', callback_data='q1')]
])


RULES = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Квоты', callback_data='lgot')],
    [InlineKeyboardButton(text='Что такое приоритетное зачисление', callback_data='prior')],
    [InlineKeyboardButton(text='Как работает система приоритетов', callback_data='sys_prior')],
    [InlineKeyboardButton(text='Что такое зелёная зона?', callback_data='green')],
    [InlineKeyboardButton(text='Что такое высший приоритет?', callback_data='upper_prior')],
    [InlineKeyboardButton(text='Калькулятор индивидуальных достижений', callback_data='calc')],
    [InlineKeyboardButton(text='Ограничения на подачу заявлений', callback_data='ogranich')],
    [InlineKeyboardButton(text='Как формируется конкурсный балл', callback_data='ball')],
    [InlineKeyboardButton(text='Минимальные баллы для подачи заявления', callback_data='min_ball')],
    [InlineKeyboardButton(text='Кто может писать вступительные экзамены?', callback_data='vstupi')],
    [InlineKeyboardButton(text='Расписание вступительных экзаменов', url='https://priem.stankin.ru/bakalavriatispetsialitet/exam_schedule/')],
    [InlineKeyboardButton(text='Я поступил, что дальше?', callback_data='pobeda')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


SPO = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Какие экзамены мне нужно сдать?', callback_data='exams_how_much')],
    [InlineKeyboardButton(text='Как проходят вступительные экзамены', callback_data='exams_how')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


LGOTI = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Целевая квота', callback_data='celev')],
    [InlineKeyboardButton(text='Особая квота', callback_data='osob')],
    [InlineKeyboardButton(text='Отдельная квота', callback_data='otd')],
    [InlineKeyboardButton(text='Назад', callback_data='rules')]
])


direction_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Математика', callback_data='01')],
    [InlineKeyboardButton(text='Информатика и вычислительная техника', callback_data='09')],
    [InlineKeyboardButton(text='Фотоника, приборостроение', callback_data='12')],
    [InlineKeyboardButton(text='Машиностроение', callback_data='15')],
    [InlineKeyboardButton(text='Техносферная безопасность и природообустройство', callback_data='20')],
    [InlineKeyboardButton(text='Технологии материалов', callback_data='22')],
    [InlineKeyboardButton(text='Управление в технических системах', callback_data='27')],
    [InlineKeyboardButton(text='Экономика и управление', callback_data='38')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


STANKIN = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дополнительные активности', callback_data='dop')],
    [InlineKeyboardButton(text='Модульная система', callback_data='modul')],
    [InlineKeyboardButton(text='Рейтинг', callback_data='rate')],
    [InlineKeyboardButton(text='ВУЦ', callback_data='VUC')],
    [InlineKeyboardButton(text='Корпуса и филиалы', callback_data='build')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


dop_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Для волонтеров', callback_data='volonter')],
    [InlineKeyboardButton(text='Кибер-клуб', callback_data='cyber')],
    [InlineKeyboardButton(text='Клуб', callback_data='club')],
    [InlineKeyboardButton(text='Профком студентов', callback_data='prof')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


CLUB = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вокал', callback_data='vocal')],
    [InlineKeyboardButton(text='Тип-топ', callback_data='tip-top')],
    [InlineKeyboardButton(text='Танцы', callback_data='dance')],
    [InlineKeyboardButton(text='Станкиновский Болт', callback_data='bolt')],
    [InlineKeyboardButton(text='Другие клубы', callback_data='other_clubs')],
    [InlineKeyboardButton(text='Назад', callback_data='dop')]
])


BUILD = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Основные корпуса', callback_data='osnov')],
    [InlineKeyboardButton(text='Фрезер', callback_data='frez')],
    [InlineKeyboardButton(text='Библиотека', callback_data='libr')],
    [InlineKeyboardButton(text='Егорьевский филиал', callback_data='egor')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


VARIANTS = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дистанционно', callback_data='dist')],
    [InlineKeyboardButton(text='Очно', callback_data='ochn')],
    [InlineKeyboardButton(text='Почта России', callback_data='post')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


VARIANTS_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инструкция ГосУслуги', url='https://vk.com/video-73442711_456239640')],
    [InlineKeyboardButton(text='Инструкция по нашему сайту приема документов', url='https://www.youtube.com/watch?v=1gxO8XMAKIc')],
    [InlineKeyboardButton(text='Наш сайт приема документов', url='https://sdpd.stankin.ru/')],
    [InlineKeyboardButton(text='Очно', callback_data='ochn')],
    [InlineKeyboardButton(text='Почта России', callback_data='post')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


VIBOR = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ЕГЭ или ВВИ', callback_data='e')],
    [InlineKeyboardButton(text='СПО', callback_data='s')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


SPISKI = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Списки к приказу', callback_data='rang')],
    [InlineKeyboardButton(text='Личный кабинет', callback_data='kab')],
    [InlineKeyboardButton(text='Про оригинал аттестата', callback_data='at')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


MODER = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Просмотреть активные заявки', callback_data='look')],
    [InlineKeyboardButton(text='Ответить на заявку', callback_data='write')],
    [InlineKeyboardButton(text='Редактирование корневых файлов', callback_data='retext')]
])


CANCEL = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
])


TASK = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ответить на вопрос', callback_data='task')]
])


BACK_OR_FEEDBACK = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оставить отзыв о работе бота', callback_data='feedback')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])


async def to_main(text='Учебный план', url=None):
    builder = InlineKeyboardBuilder()
    if url is not None:
        builder.add(InlineKeyboardButton(text=text, url=url))
    builder.add(InlineKeyboardButton(text='Назад', callback_data='back_to_main'))
    return builder.adjust(1).as_markup()


async def directions(group):
    builder = InlineKeyboardBuilder()
    results = get_directions(group)
    for item in results:
        builder.add(InlineKeyboardButton(text=item[0][:item[0].index(':')], callback_data=item[1]))
    return builder.adjust(1).as_markup()


async def b():
    builder = InlineKeyboardBuilder()
    results = get_b()
    for item in results.keys():
        builder.add(InlineKeyboardButton(text=item, callback_data=f"b+{results[item]}"))
    builder.add(InlineKeyboardButton(text='Обнулить баллы', callback_data='b//0'))
    builder.add(InlineKeyboardButton(text='Назад', callback_data='rules'))
    return builder.adjust(1).as_markup()
