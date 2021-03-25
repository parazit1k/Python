#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TOKEN=''

def message_handler(bot: Bot,update: Updater):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Аноним'
    text = update.effective_message.text
    if text == '/start':
        reply_text=f'Привет, {name}!\n\nЧтобы узнать функции напиши /help'
    elif text == '/help':
        reply_text='Выбери кинотеатр: 1- Родина, 2- Обнинск'
    elif text == '1':
        reply_text=get_matches()
    elif text == '2':
        reply_text=get_matches1()
    else:
        reply_text='Я вас не понимаю, напишите /help!'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text
    )
    return

def main():
    bot = Bot(
        token=TOKEN,
        base_url='https://telegg.ru/orig/bot',
    )
    updater = Updater(bot=bot)

    handler=MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)
    
    updater.start_polling()
    updater.idle()
def get_html(url):
    if url:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(url, headers=headers)
        html = r.text
        return (html)


def read(html):
    vse=''
    l = BeautifulSoup(html, 'lxml')
    cat = l.find('div', class_='category films')
    cont = cat.find_all('div', class_="head")
    k=0
    for i in range(len(cont)):
        f = cont[i].find('span', itemprop='name')
        if f is None:
            pass
        else:
            f = str(f)
            f = f.replace('<span itemprop="name">', '')
            f = f.replace('</span>', '')
            ses0 = str(cont[i])
            ses0 = ses0.replace('<div class="head"><a href="', '')
            ses = ''
            for i in ses0:
                if i == '"':
                    break
                else:
                    ses += i
            htt = 'https://rodina-cinema.ru/'
            ses = htt + ses
            if k == len(cont):
                vse+=f'{f}, Ссылка на расписание: {str(ses)}'
            else:
                vse+=f'{f}, Ссылка на расписание: {str(ses)}\n'
        k+=1
    return(vse)

def get_matches():
    url = 'https://rodina-cinema.ru/afisha'
    data = read(get_html(url))
    return (data)
def read1(html):
    vse=''
    l = BeautifulSoup(html, 'lxml')
    cont = l.find_all('div', class_='afisha-seance-theater-wrapper')
    k=0
    for i in range(len(cont)):
        f = cont[i].find('div', class_='afisha-view afisha-view-list show')
        f=str(f)
        k=0
        fo=''
        for i in range(len(f)):
            if f[i:i+41] == '<span class="film-title"><a href="/filmy/':
                ko=k+41
                while True:
                    if f[ko]=='<':
                        fo+='\n'
                        break
                    else:
                        fo+=f[ko]
                    ko+=1
            k+=1
        k=0
        for i in fo:
            if i == '>':
                k+=1
            if i != '>' and k==1 and i != '\n':
                vse+=i
            if i != '>' and k==1 and i == '\n':
                vse+=i
                k=0
        fo=''
        k=0
        fk=''
        p=''
        for i in range(len(f)):
            if f[i:i+35] == '<a class="seance" href="#" onclick=':
                ko=k+35
                while True:
                    if f[ko-41:ko] == '<span class="film-title"><a href="/filmy/':
                        break
                    ko-=1
                while True:
                    if f[ko]=='<':
                        fk+='\n'
                        break
                    else:
                        fk+=f[ko]
                    ko+=1
                ko=k+35
                while True:
                    if f[ko]=='<':
                        fo+=' '
                        break
                    else:
                        fo+=f[ko]
                    ko+=1
            k+=1
        k=0
        vse1=''
        vse2=''
        for i in fk:
            if i == '>':
                k+=1
            if i != '>' and k==1 and i != '\n':
                vse2+=i
            if i != '>' and k==1 and i == '\n':
                vse2+=i
                k=0
        for i in fo:
            if i == '>':
                k+=1
            if i != '>' and k==1 and i != ' ':
                vse1+=i
            if i != '>' and k==1 and i == ' ':
                vse1+=i
                k=0
        if ' ' in vse2:
            while ' ' in vse2:
                vse2=vse2.replace(' ','')
        vse1=vse1.split()
        vse2=vse2.split()
        print(vse2)
        k=0
        c1=''
        otv=''
        vse1=''.join(vse1)
        for i in range(0,len(vse1),5):
            c1+=vse1[i:i+5]+' '
        vse1=c1
        vse1=vse1.split(' ')
        c1=''
        if len(vse2) != 0:
            for i in range(len(vse1)-1):
                if vse1[i]>vse1[i+1]:
                    c1+=vse1[i]+'\n'
                else:
                    c1+=vse1[i]
            if vse2[len(vse1)-2] > vse1[len(vse1)-1]:
                c1+='\n'+vse1[len(vse1)-1]
            else:
                c1+=vse1[len(vse1)-1]
            c1=c1.split()
            print(list(c1))
            vse2=(list(set(vse2)))
            for i in range(len(vse2)):
                otv+='Фильм: '+str(vse2[i])+'. Сеансы: '+str(c1[i])+'\n'
            vse+='\n'+'\n'+otv
            return(vse)
        else:
            otv+='На данный момент сеансов нет('
            vse+='\n'+'\n'+otv
            return(vse)
            
            
        
def get_matches1():
    url = 'https://kino-obninsk.com/#afisha'
    data = read1(get_html(url))
    return(data)
if __name__ == '__main__':
    main()

