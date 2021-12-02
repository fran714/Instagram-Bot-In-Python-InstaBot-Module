import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

from instabot import Bot

bot = Bot()

bot.login(username="sudoalpha26",password="promisecare")


bot.upload_photo("fire.jpg", caption="Fireworks Happy New Month")





