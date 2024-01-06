import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    LabeledPrice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, \
    CallbackQueryHandler, PreCheckoutQueryHandler

TOKEN = '6692563300:AAGLWP8HfNrYGU9v_48rryBKDu_pWT_ftFY'
BASE_DIR = 'files/'

SELECT_ACTION, LIST_FILES, FILE_DESCRIPTION = range(3)


def start(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [KeyboardButton("Список файлов")],
        [KeyboardButton("Помощь")],
        # Добавьте дополнительные кнопки по вашему усмотрению
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Добро пожаловать в магазин бота!', reply_markup=reply_markup)
    return SELECT_ACTION


def list_files(update: Update, context: CallbackContext) -> int:
    files = os.listdir(BASE_DIR)

    if not files:
        update.message.reply_text("Нет доступных файлов.")
        return SELECT_ACTION

    keyboard = [
        [InlineKeyboardButton(f"{file}", callback_data=f"file_{file}")]
        for file in files
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Доступные файлы:", reply_markup=reply_markup)
    return SELECT_ACTION


def file_description(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    file_name = query.data.replace('file_', '')
    file_path = os.path.join(BASE_DIR, file_name)

    if not os.path.exists(file_path):
        query.message.reply_text(f"Файл {file_name} не найден.")
        return SELECT_ACTION

    # Добавим описание файла и кнопки
    description = "Описание файла: Очень полезный файл."
    keyboard = [
        [InlineKeyboardButton("НАЗАД", callback_data="back")],
        [InlineKeyboardButton("ОПЛАТА", callback_data=f"pay_{file_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(f"{description}", reply_markup=reply_markup)
    return SELECT_ACTION


def send_file(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    file_name = query.data.replace('pay_', '')
    file_path = os.path.join(BASE_DIR, file_name)

    if not os.path.exists(file_path):
        query.message.reply_text(f"Файл {file_name} не найден.")
    else:
        with open(file_path, 'rb') as file:
            query.message.reply_document(file)

    return SELECT_ACTION


def pre_checkout_callback(update: Update, context: CallbackContext) -> None:
    query = update.pre_checkout_query
    if query.invoice_payload != 'YOUR_CUSTOM_PAYLOAD':
        query.answer(ok=False, error_message="Некорректная оплата")
    else:
        query.answer(ok=True)


def successful_payment_callback(update: Update, context: CallbackContext) -> None:
    payment_info = update.message.successful_payment
    user_id = update.message.chat_id
    file_name = context.user_data.get('file_name')

    # Здесь вы можете проверить payment_info и предоставить пользователю доступ к файлу
    # Например, добавьте user_id и file_name в базу данных для отслеживания оплаты

    # После успешной оплаты, вы можете отправить пользователю сообщение с файлом
    file_path = os.path.join(BASE_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            update.message.reply_document(file)
    else:
        update.message.reply_text(f"Файл {file_name} не найден.")


def help_info(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("""
    Этот бот предоставляет следующие функции:
    - /start: Начать взаимодействие с ботом.
    - /list: Показать список доступных файлов.
    - /get <file_name>: Получить конкретный файл.
    - Список файлов: Показать доступные файлы через кнопку.
    - Помощь: Показать это сообщение.
    """)
    return SELECT_ACTION


def button_click(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    data = query.data

    if data.startswith('pay_'):
        file_name = data.replace('pay_', '')
        context.user_data['file_name'] = file_name
        query.message.reply_invoice(
            title=f"Оплата файла {file_name}",
            description="Описание оплаты",
            provider_token='1744374395:TEST:6eef1bbf5474c6fcf382',  # Токен вашего платежного провайдера
            currency='RUB',
            prices=[LabeledPrice(label='Стоимость', amount=10000)],
            # Установите необходимую стоимость в копейках (100 рублей)
            start_parameter='pay_for_file',
            payload='YOUR_CUSTOM_PAYLOAD'  # Уникальная строка для вашего приложения
        )
    elif data == 'help':
        return help_info(update, context)
    elif data.startswith('file_'):
        return file_description(update, context)


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_ACTION: [
                MessageHandler(Filters.regex('^(Список файлов)$'), list_files),
                MessageHandler(Filters.regex('^(Помощь)$'), help_info),
                CallbackQueryHandler(button_click),
            ],
            FILE_DESCRIPTION: [
                CallbackQueryHandler(file_description),
                MessageHandler(Filters.regex('^(Список файлов)$'), list_files),
            ]
        },
        fallbacks=[],
    )

    updater.dispatcher.add_handler(PreCheckoutQueryHandler(pre_checkout_callback))
    updater.dispatcher.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
