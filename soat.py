from pyrogram import Client, Filters
from pyrogram.raw import functions, types
import datetime
import time
import pytz
api_id = 3595783 #my.telegram.org dan olgan apiidni qoying
api_hash = "13d72cc0cb8f2bf82cceaa205b808360" #my.telegram.org dan olgan apihash ni qoying
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone("Asia/Tashkent")
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="O'zbekistonda soat: " +str(x)
    ))
    time.sleep(30)
