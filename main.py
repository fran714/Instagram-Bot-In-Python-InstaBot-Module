import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
from instabot import Bot
bot = Bot()
bot.login(username="Enter Your UserName Here ",password=" Enter Your Account Password Here")
bot.upload_photo("galo.jpg", caption="Enter Your caption here")





