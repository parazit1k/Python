import telebot
import random
import conf
#token
bot = telebot.TeleBot(conf.config['token'])

#markups
markup = telebot.types.ReplyKeyboardMarkup(True, True)
markdown = telebot.types.ReplyKeyboardRemove()
markup.row('Смотрю','Буду смотреть')

#kod
kod = str(random.randrange(1,10)) + str(random.randrange(1,10)) + str(random.randrange(1,10))

#anime
anime0=open('anime.txt')
anime=''
for i in anime0:
    anime+=i
anime0.close()
anime0=open('fanime.txt')
fanime=''
for i in anime0:
    fanime+=i
    
#Начало
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери: ', reply_markup=markup)
#админ
@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.username == 'parazitik':
        bot.send_message(message.chat.id, f'Твой код: {kod}')
        
#Выбор
@bot.message_handler(content_types=['text'])
def Chose(message):
    if message.text.lower() == 'смотрю':
        bot.send_message(message.chat.id, f'\n{anime}', reply_markup=markup)
    elif message.text.lower() == 'буду смотреть':
        bot.send_message(message.chat.id, f'\n{fanime}', reply_markup=markup)
    elif kod in message.text:
        a = message.text
        k=0
        b=''
        b1=''
        b2=''
        for i in a:
            if i == ' ' and k == 0:
                k+=1
            elif i !=' ' and k == 0:
                b+=i
            elif k == 1 and not i.isdigit():
                b1+=i
            elif i.isdigit():
                b2+=i
                k+=1
        f = open('result.txt','w+')
        f.write(b1)
        f.write(b2)
        f.close()
        bot.send_message(message.chat.id, 'Готово')


f= open('result.txt','r')
k=0
a1=''
a2=''
for i in f:
    for j in i:
        if j.isdigit():
            a2+=str(j)
            k+=1
        elif k == 0:
            a1+=j
f.close()
f = open('result.txt','w+')
f.close()
    
        
#loop
bot.polling( none_stop = True )
