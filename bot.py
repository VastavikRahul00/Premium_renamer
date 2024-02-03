import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6377504948:AAFOULubtPkPL3LETFgkEJd5ZZ37LJJC-zY")

API_ID = int(os.environ.get("API_ID", "28590119"))

API_HASH = os.environ.get("API_HASH", "2494557bf21e6c5152f26070aa1a97c7")

STRING = os.environ.get("STRING", "AQE9cVgAA5THKM8GQByVjRxqa9cMkI4f49Mi4nIeNNB-JypfnlwuV7kXeTud9rw5AQFpX9eas0-R3g2_8pTJTUtBbeoLqIxArKxe9gJ1svbQ7TSYpQtEe69eAlVzjYDVFfacMB7_SeWWD89cnk_p2wNhY6PUG0J2tXI4HpCcCTnPcmR_hfi6ENaVPvlP3f2c5Z_g_HQt0kZ53t71oOw8hfBlZN9f1utbMNQmfbu4ViTVuXatgCiIHnkSqhc6_-sAffNndIXqQM3aYfd6L50kS4dBEsxuyhAgzGiHVpTTHCv1TBECreH3O5YvgdnxfZncnKTzolDQ2dPtZe71AqJl67zeOUJ-rQAAAAGBMESgAA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
