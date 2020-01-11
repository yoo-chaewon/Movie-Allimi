import telegram

bot = telegram.Bot(token = '1069181474:AAH84nrPpIYiTjTWW1F0iviYs5Z1LdIdUgw')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id = 862740368, text = "테스트입니다.")