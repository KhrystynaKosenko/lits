import os, sys

print "Привіт"
print 'Зіграємо? так/ні'
a1= raw_input(' ')
#while True:
if a1 == 'так':
   	print 'Вітаю у грі'
   	print '               '
   	print '***НЕНСІ ДРЮ***'
   	print '               '
elif a1 == 'ні':
	print 'Шкода. Гарного дня' 
	sys.exit()
	#break #можна додати ви впевнені
else:
	print "Дайте відповідь так або ні"
	a1= raw_input()
name = raw_input('Як вас звати?')
print 'Отже ' + str(name)+', уявіть що ви посеред гір і снігу,\n'
print 'ви приїхали відпочити, і покататись на сноуборді, але в перший ж\n'
print 'ж день з вашого готельного номеру було викрадено ваш сноуборд. '
print 'І вам необхідно знайти його.'
print '                  '
print 'Зараз ви в кімнаті, оглядаєте речі, і бачите ключ на столі'
keys= raw_input('Чи хочете ви їх взяти? так/ні')
pocket=0
if keys == 'так':
	pocket = 1
	print 'Чудово. Тепер ключі у вашій кишені'
	print '            '
elif keys == 'ні':
    pocket = 0
	#print 'Ви обрали не забирати ключі'     
#else:
#	print 'Оберіть, будь ласка, варіант. Так, ні або пізніше'
print 'На столі також бачимо листочок з чотирьма порожнімі квадратиками. І математичним виразом 525+(26*2)+1226/2'
print 'Розв`язати зараз. так/ні'
answer_math= raw_input()
if answer_math == 'так':
	print 1190 #import math
	print 'Рухаємось далі'
elif answer_math =='ні':
	print 'Рухаємось далі'
print '' 
print 'Далі йдемо до холу, бачимо двох людей, хлопця в червоній куртці,'
print 'що розгляда мапу і дівчину, котра читає'
print''  
print 'Вирішуємо поговорити з хлопцем, але він не розуміє української, тому переходимо на англійську'
print 'Hi, I`m ' + str(name)+ ' And what`s your name?'
print 'I`m Phillip'
print 'Перелік запитань, які ми можете задати Філіпу'
questions ={'1': 'Where are you from?',
            '2': 'For how long are you staying here?', 
            '3': 'Do you like it here?',
            '4': 'What do you usually do here?',
            '5': 'Do you know anyone who is staying here too?',
            '6': 'How do you think who is responsible for all missing and broken items' }
print questions
for key in questions:
	answer = raw_input('Введіть номер запитання')
	if answer == '1':
		print questions ['1']
		print 'I`m from Lima, Peru. And you?'
		print 'Oh, i heard it`s a really nice place. I`m from Lviv, Ukraine'
		print 'Задати інше запитання? так/ні'
		answer_end= raw_input()
		if answer_end == 'так':
			continue
		else:
			break
	elif answer == '2':
		print questions ['2']
		print 'I`m here already for 3 months'
		print 'That`s a lot'
		answer_end= raw_input()
		if answer_end == 'так':
			continue
		else:
			break
	elif answer == '3':
		print questions ['3']
		print'Yes, i`m going too stay here for a while'
		print 'Задати інше запитання? так/ні'
		answer_end= raw_input()
		if answer_end == 'так':
			continue
		else:
			break
	elif answer == '4':
		print questions ['4']
		print'I`m usually go snowboarding or hiking'
		print 'Задати інше запитання? так/ні'
		answer_end= raw_input()
		if answer_end == 'так':
			continue
		else:
			break
	elif answer == '5':
		print questions ['5']
		print'Yes, there is a girl from Spain, she actually was here couple minutes ago,\n'
		print 'and there is a guy from Japan, but i don`t talk to him much'
		print 'Задати інше запитання? так/ні'
		answer_end= raw_input()
		if answer_end == 'так':
			continue
		else:
			break
	elif answer == '6':
		print questions ['6']
		print'Honestly, i dont know and i really dont want to know'
		print 'Ok then, see you later, bye'
		print 'See you'
		break
	else: 
		print 'Упс, ви не ввели номер запитання. Введіть номер запитання'
print 'Йдемо перевіримо, що відбувається знадвору, спершу знайдемо снігохід'
print 'Запитуємо про нього. Йдемо далі, бачимо снігохід, але на ньому чотирьох значний код'
print 'Введіть код'
x=raw_input() # числа,що вгадуємо
#сам код, що потрібно відгадати
while x != '1190':
	print'Спробуйте ще раз'
	x = raw_input()
	if x == '1190':
		print 'Вітаю, снігохід ваш'
		break
print ''
print 'Тепер потрібно відчинити двері. Якщо у вас уже є ключ, то двері відчиняться автоматично'
if pocket==1:
	print'Двері відчинено'
	print ''
elif pocket==0:
	print 'Верніться в кімнату і візьміть ключі.Забрали ключі, повертаємось до снігохода'
else:
	pass
print'               '
print'                                          '
print 'Снігохід є, двері відчинені, але нам бракує карти, йдемо на рецепцію по карту'
print 'Але, на жаль, на рецепції, не розмовляють українською, тому перемикаємось на англійську'
print 'Hi, i need a map'
print 'Sure, but firstly you need to solve one pazzle. Are you in? yes/no'
answer_map = raw_input()
while True:
	if answer_map == 'yes':
		print 'Great'
		break
	elif answer_map== 'no':
		print 'So no map for you. Game is over'
		sys.exit()
	else:
		print 'Please answer the question yes or no'
		answer_map = raw_input()
print '' 
print'So the game is about guessing flags of different countries I`m going to say the country and you`ll need to say the colours on the flags. Do you understand? yes/no'
answer_flag =raw_input()
if answer_flag == 'yes':
	print'Lets start a game'
elif answer_flag == 'no':
	print 'When for you game is over'
else:
	'Answer please yes or no'
print 'Spanish flag has 2 colors yellow and which else these colours Spanish flag has?'
colors = ['green', 'yellow','red', 'blue', 'white', 'black']
print colors
print 'Choose the color'
guess = raw_input()
while True:
  if guess == 'red':
    print 'Great'
    break
  elif guess != 'red': 
    print 'Try another color'
    guess = raw_input()
  else:
    print 'Enter one of the colors'
#if len(flag1) < 2:
#	print'Type all colours'
#else:
#	bre
print 'Correct, one more'
print ''
print 'Nepali flag has 3 colors red, blue and?'
colors = ['green', 'yellow','red', 'blue', 'white', 'black']
print colors
print 'Choose the color'
guess = raw_input()
while True:
  if guess == 'white':
    print 'Great'
    break
  elif guess != 'white': 
    print 'Try another color'
    guess = raw_input()
  else:
    print 'Enter one of the colors'
print 'Correct, last one'
print ''
print 'Brasilian flag has yellow and?'
colors = ['green', 'yellow','red', 'blue', 'white', 'black']
print colors
print 'Choose the color'
guess = raw_input()
while True:
  if guess == 'green':
    print 'Great'
    break
  elif guess != 'green': 
    print 'Try another color'
    guess = raw_input()
  else:
    print 'Enter one of the colors'
print 'Congrads, here is your map'
print 'Тепер в нас є мапа, вирушаємо до дверей'
print 'Тільки підійшовши до дверей ми бачимо, що хтось якраз виїхав. Ми вирішуємо їхати за ним'
print 'Бачимо, що снігохід перед нами зупиняється перед невеликою хатиною, впізнаємо в ньому Філіпа'
print 'Підійшовши до дверей бачимо замок з кодом, для того, щоб зайти нам необхідно підібрати код'
print 'Оглянувшись навколо біля вікна бачимо видряпані цифри і номери кольорів, що їм відповідають'
colors_code ={'1': 'white',
            '2': 'blue', 
            '3': 'yellow',
            '4': 'black',
            '5': 'red',
            '6': 'green' }
print colors_code
print 'Спробуємо відгадати код'
code_hut = raw_input()
while code_hut != '151':
	print 'Неправильно'
	code_hut = raw_input()
	if code_hut == '151':
		print 'Вітаю, ви вгадали'
		break
print 'Відкривши двері, ви бачите Філіпа'
print 'BUSTED'
print ''
print 'Вітаю, ви знайшли свій сноуборд і спіймали злодія'
print ''


