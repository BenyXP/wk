#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28414908
API_HASH = "8d2e5bdb8848ae0b37e869be445a8f32"
BOT_TOKEN = "6596482531:AAHmCTDtxYMflOgT4hmSV7LBNqkEh8IQGrE"
SESSION = "AQAhIHQAKFkDIQMujHVR-ugbpI9BtAgedLu-VNncafMt3WbjPkjh8LW7-dMKKrOlVTfjKtD4MJVIXnLsaSwtqdAqXrKZYIVrC3S2eT89siwgxygceAPXrxdMv0pvwM3shkCBG0U03BdjQJ14cnHKy0Kd0nEO9MCVz7m2UPhsVeCr3eno8mj4J0eqgCDvNf7TmHh1fr0Mt5RxErB6g7tQAR84LJoWwBj7jRbNcP3lOsf_wu0SLtrVQOSTya8YzrBYcLd5hrIyE3QoQjCytilYceaUUUJRAkaj8HekESGhGYuuSvKeXPoCQkGmCVOvlS49Ccmcz9LjTeuTY0fABtY8vcqBhfjeqQAAAABuJAClAA"
FORCESUB = "lepinst4r"
AUTH = "1847853221"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
