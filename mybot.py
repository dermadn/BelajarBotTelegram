import telebot
import mysql.connector

import mytoken

from telebot import types
from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_bot_tele')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        # photo = open('img/rpl1.png', 'rb')
        # myBot.send_photo(message.from_user.id, photo)
        teks = "\n-- Test hello dari dmare bot -- "+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x) + '\n'
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))

    @myBot.message_handler(commands=['rpl2'])
    def menu_data_rpl2(message):
        query="select nama,kelas from tabel_siswa where kelas like '%XI RPL 2%'"
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        rpl2data=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                rpl2data =rpl2data+ str(x) + '\n'
                print(rpl2data)
                rpl2data = rpl2data.replace('(', '')
                rpl2data = rpl2data.replace(')', '')
                rpl2data = rpl2data.replace("'", '')
                rpl2data = rpl2data.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(rpl2data))

    @myBot.message_handler(commands=['rpl1'])
    def menu_data_rpl1(message):
        query="select nama,kelas from tabel_siswa where kelas like '%XI RPL 1%'"
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        rpl1data=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                rpl1data =rpl1data+ str(x) + '\n'
                print(rpl1data)
                rpl1data = rpl1data.replace('(', '')
                rpl1data = rpl1data.replace(')', '')
                rpl1data = rpl1data.replace("'", '')
                rpl1data = rpl1data.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(rpl1data))


print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
