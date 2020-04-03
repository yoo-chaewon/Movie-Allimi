import telegram

bot = telegram.Bot(token = '')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id = 862740368, text = "테스트입니다.")
