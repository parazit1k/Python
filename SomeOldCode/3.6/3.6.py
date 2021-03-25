import random
import string
routes = {'m': 'Москва','r': 'Рязань', 'p': 'Санкт-Петербург', 's': 'Смоленск','k':'Крым','h':'Сочи'}
trains = ['mr','mp','ms','rm','pm','sh','hs','hk','kh']
"""
Поиск пути

"""
a=routes.values()
b=''
print('Города: ',','.join(a))
while True:
	choose1=input('Введите отправной город: ').title()
	choose2=input('Введите город прибытия: ').title()
	#choose1='Москва'
	#choose2='Смоленск'
	k=0
	for i in routes:
		if choose1 == routes.get(i):
			choose1 = i
			k+=1
		elif choose2 == routes.get(i):
			choose2 = i
			k+=1
	if k<2:
		print('Неправильно написан город!')
		continue
	else:
		break
choose = choose1 + choose2
if choose in trains:
	print('Поезд№ '+random.choice('abcdefghijklmnopqrstuvwxyz')+str(random.randrange(0,10)))
	date='Дата отправления: '+str(random.randrange(1,31))
	date+='.'+str(random.randrange(1,13))
	date+='.'+'2020'
	print(date)
	time='Время отправления: '+str(random.randrange(1,25))+':'+str(random.randrange(0,6))+str(random.randrange(0,9))
	timed=''
	for i in time:
		if i.isdigit():
			timed+=i
		elif i == ':':
			timed+=' '
	time2='Время прибытия: '+str(random.randrange(1,25))+':'+str(random.randrange(0,6))+str(random.randrange(0,9))
	timed2=''
	for i in time2:
		if i.isdigit():
			timed2+=i
		elif i == ':':
			timed2+=' '
	c=-1
	t=''
	for i in timed:
		if i == ' ':
			c+=1
		elif c == 1:
			continue
		elif c==0:
			t+=str(i)
	c=-1
	t2=''
	for i in timed2:
		if i == ' ':
			c+=1
		elif c == 1:
			continue
		elif c==0:
			t2+=str(i)
	dated=''
	dated2=''
	c=0
	for i in date:
		if i.isdigit() and c==0:
			dated+=i
		elif i == '.':
			c+=1
		elif c == 1:
			dated2+=i
	if int(t)>int(t2):
		date2='Дата прибытия: '+str(int(dated)+1)
		date2+='.'+dated2+'.'+'2020'
	elif int(t)<=int(t2):
		date2='Дата прибытия: '+dated
		date2+='.'+dated2+'.'+'2020'
	print(date2)
	print(time+'\n'+time2)
	print('Стоймость: ',random.randrange(1000,2000),' рублей, с учётом НДС')
	print(routes[choose1]+'  --->  '+routes[choose2])
