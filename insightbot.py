from login import bot
from buttons import markup_start

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Для создания своего первого поиска используйте кнопку '🔍 Создать поиск'", reply_markup=markup_start) #без этой команды кнопки не появляются на экране у пользователя
 

  
if __name__ == "__main__":
    # Запускаем бот
    bot.polling(none_stop=True, interval=0)
