import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1069181474:AAH84nrPpIYiTjTWW1F0iviYs5Z1LdIdUgw')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200115'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
imax = soup.select_one('span.imax')
if(imax):
    imax = imax.find_parent('div', class_='col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    bot.sendMessage(chat_id=862740368, text=title + 'IMAX 예매가 열렸습니다.')
else:
    bot.sendMessage(chat_id=862740368, text='IMAX 예매가 아직 열리지 않았습니다.')
