import telebot
import random
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot("1648838020:AAGg5cnPTPP06qYmXY2_ArHtzOHHzPII1Ng")

something = {}
previous = {}
top = {}
start1 = {}
user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
user_markup.row("1","2")
user_markup.row("/anime")

@bot.message_handler(commands=['start'])
def start(message):
    print(f'[{message.from_user.username}]', "-" ,message.text)
    start1[message.chat.id] = False
    bot.send_message(message.chat.id, "Введи ник на jut.su", reply_markup=user_markup)

@bot.message_handler(commands=['anime'])
def findananime(message):
    global start1
    try:
        name,img,rate = (parse('yummy','notreallyneed'))
        bot.send_photo(message.chat.id,img)
        bot.send_message(message.chat.id,f"{name}\n[{rate}]☆",)
    except:
        bot.send_message(message.chat.id, "ERROR23")


def stop(message):
    global start1, something
    first, second = infinite(message)
    previous.setdefault(message.chat.id,[0,0])
    previous[message.chat.id][0] = (first)
    previous[message.chat.id][1] = (second)
    bot.send_message(message.chat.id, f"Выбирай: [1] {(something[message.chat.id])[first]} или [2] {(something[message.chat.id])[second]}",reply_markup=user_markup)

@bot.message_handler(commands = ['stop'])
def clear(message):
    global start1,something,top,previous
    print(f'[{message.from_user.username}]', "-", message.text)
    try:
        start1[message.chat.id] = False
        del something[message.chat.id]
        top[message.chat.id] = []
        previous[message.chat.id] = [0,0]
        bot.send_message(message.chat.id, "Остановил")
    except KeyError:
        bot.send_message(message.chat.id, "Так ты ещё не начал:(")

@bot.message_handler(content_types=["text"])
def check(message):
    global something, start1, user_markup,top, nick
    start1.setdefault(message.chat.id, False)
    if message.text != "1" and message.text != "2":
        print(f'[{message.from_user.username}]', "-" ,message.text)
    elif start1[message.chat.id]:
        if message.text == "1":
            print(f'[{message.from_user.username}]', "-" , f"[{something[message.chat.id][previous[message.chat.id][0]]}] - {something[message.chat.id][previous[message.chat.id][int(message.text)]]}")
        else:
            print(f'[{message.from_user.username}]', "-",
                  f"{something[message.chat.id][previous[message.chat.id][int(message.text)-2]]} - [{something[message.chat.id][previous[message.chat.id][1]]}]")
    if message.text != "1" and message.text != "2" and start1[message.chat.id] != True:
        nick = message.text
        if parse("jutsu",nick) == 0:
            bot.send_message(message.chat.id, f"Ник: {nick} не правильный, чекни свой ник на сайте:(")
        else:
            bot.send_message(message.chat.id, f"{message.text} принял.")
            something.setdefault(message.chat.id, parse("jutsu",nick))
            start1[message.chat.id] = True
            top.setdefault(message.chat.id,[])
            stop(message)
    elif (message.text == "1" or message.text == "2") and start1[message.chat.id]:
        if message.text == "1":
            top[message.chat.id].append((something[message.chat.id])[int(previous[message.chat.id][1])])
            something[message.chat.id].pop(int(previous[message.chat.id][1]))
            if len(something[message.chat.id]) == 1:
                top[message.chat.id].reverse()
                send = f'Твой топ:\n[1] - {something[message.chat.id][0]}\n'
                for i in range(len(top[message.chat.id])):
                    send += f"[{i + 2}] - {top[message.chat.id][i]}\n"
                bot.send_message(message.chat.id, f"{send}", reply_markup=None)
                del something[message.chat.id]
                start1[message.chat.id] = False
                top[message.chat.id] = []
                print(f"[Bot] - [{send}]")
            else:
                stop(message)
        else:
            top[message.chat.id].append(something[message.chat.id][int(previous[message.chat.id][0])])
            something[message.chat.id].pop(int(previous[message.chat.id][0]))
            if len(something[message.chat.id]) == 1:
                top[message.chat.id].reverse()
                send = f'Твой топ:\n[1] - {something[message.chat.id][0]}\n'
                for i in range(len(top[message.chat.id])):
                    send += f"[{i + 2}] - {top[message.chat.id][i]}\n"
                bot.send_message(message.chat.id, f"{send}", reply_markup=None)
                del something[message.chat.id]
                start1[message.chat.id] = False
                top[message.chat.id] = []
                print(f"[Bot] - [{send}]")
            else:
                stop(message)
    else:
        bot.send_message(message.chat.id, "Не пытайся сломать мне прогу, пожалуйста:0")


def infinite(message):
    global something
    first = random.randrange(0, len(something[message.chat.id]))
    while True:
        second = random.randrange(0, len(something[message.chat.id]))
        if second != first:
            break
    return (first, second)

nick = ''

def get_html(url,nick = None):
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "accept": "*/*"}
    if url == "jutsu":
        url = f'https://jut.su/user/{nick}/anime/'
    else:
        url = 'https://yummyanime.club/top'
    try:
        r = requests.get(url, headers = HEADERS)
        return (r)
    except:
        bot.send_message(255064127,"get_html")

def get_content(html, nick):
    soup = BeautifulSoup(html, "html.parser")
    if nick != "notreallyneed":
        check = (soup.find("h1", class_ = "mail_h_h1 anime_current_h1").get_text)
        if nick in str(check).lower():
            items = soup.find_all("div", class_="aaname")
            list = []
            for i in items:
                item = i.get_text()
                list.append(item)
            return (list)
        else:
            return (0)
    else:
        try:
            items = soup.find_all("a", class_= "anime-title")
            pa = []
            for i in items:
                pa.append(i.get_text())
            items = soup.find_all("img")
            pa2 = []
            k= 0
            for i in items:
                if k > 5 and k != len(pa):
                    pa2.append("https://yummyanime.club/"+str(i.get("src")))
                k+=1
            randomnum = random.randrange(0,len(pa)-1)
            HEADERS = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                "accept": "*/*"}
            r = requests.get(pa2[randomnum], headers=HEADERS)
            img = r.content
            items = soup.find_all("span", class_ = "main-rating")
            pa3 = []
            for i in items:
                pa3.append((i.get_text()))
            return(pa[randomnum],img,pa3[randomnum])
        except:
            bot.send_message(255064127,"???")

def parse(url, nick):
    if url == "yummy":
        url = 'https://yummyanime.club/top'
    elif url == "jutsu":
        url = f'https://jut.su/user/{nick}/anime/'
    html = get_html(url, nick)
    if html.status_code == 200:
        return(get_content(html.text, nick))
    else:
        bot.send_message(255064127,html.text)
        print("ERROR!")





bot.polling()
