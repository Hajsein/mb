from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '7331545811:AAGeRp1rXt1vzkon_4WG-myUmuTZJnX5Tqs'
CHANNEL_USERNAME = '@testbot7676'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("دریافت ادلیست جدید اسپینر", callback_data='check_membership')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('لطفا ابتدا در کانال یادآور عضو شوید:', reply_markup=reply_markup)

def check_membership(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    user_id = query.from_user.id
    status = context.bot.get_chat_member(CHANNEL_USERNAME, user_id).status
    
    if status in ['member', 'administrator', 'creator']:
        query.edit_message_text(text="https://t.me/addlist/2_spmikbsQI4MWI0")
    else:
        keyboard = [
            [InlineKeyboardButton("عضو شدم", callback_data='check_membership')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="شما عضو کانال یادآور نیستید. لطفا عضو شوید و دوباره تلاش کنید:", reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TOKEN)
    
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(check_membership))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()