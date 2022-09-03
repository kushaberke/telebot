import telegram.ext
import telegram


with open('token.txt','r') as f:

    TOKEN = f.read()

    
def start(update,source):
    update.message.reply_text('<b>Kusha Mühendislik Sayfasına Hoşgeldin!</b>', disable_web_page_preview=True, parse_mode=telegram.ParseMode.HTML)
    

update = telegram.ext.Updater(TOKEN,use_context=True)
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler('/start',start))

update.start_polling()
update.idle()