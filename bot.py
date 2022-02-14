from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hola, Humano!')


if __name__ == '__main__':
    updater = Updater(
        token='5153127043:AAHHgo8EQq_IHUgg5o548FfsKl3G85t_pNc', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
