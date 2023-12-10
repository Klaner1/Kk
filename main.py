import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
p = dict(root='plugins')
from kvsqlite.sync import Client as fdb

db = fdb('data.sqlite', 'fuck')
if not db.exists("admin_list"):
    db.set('admin_list', [1354518673,6221145647])
if not db.exists("sessions"):
    db.set('sessions', [])
if not db.exists("ban_list"):
    db.set("ban_list", [])
x = Client(name='lossclhos', api_id=13812635, api_hash='37492df55e9a6ec5b73cab35dfb34e39', bot_token='5228324503:AAFOcBiFuXzNf6uSxOaEKwIM8KTO4_QZRfc', workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
