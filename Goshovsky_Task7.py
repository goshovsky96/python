# Створення прикладних програм на мові Python
# Лабораторна робота №7
# Гошовський Іван, №6
area = 0
naselennia = 1
continent = 2

def showSpisok (**sp):
	"""Функція приймає аргументом словник з ключем - назва країни, значення -
		список з інформацією про країну [площа, населення, материк]
		через цикл фор виводимо інформацію про країни, які є в словнику
	"""
	for x in sp:
		print ('{} - площа: {} кв², населення: {}, {}'.format(x, sp[x][area], sp[x][naselennia], sp[x][continent]) )
	print('*** '*15)


def inSearch (name, **sp):
	""" Функція приймає аргументом назву материка - name, та словник з списком країн sp
		Через цикл for провіряємо чи є в словнику країна з назвою материка name
		Якщо є - добавляємо її в змінну результату. 
		Якщо немає жодної країни з назвою материка name - виводить про це повідомлення.
	"""
	res = ''
	k = 0
	for x in A:
		if A[x][continent] == s:
			res += x + ' '
			k += 1
	if k == 0:
		res = 'В списку немає жодної країни або вказано не правильно континент'
	return res


A = {
	'Україна': [603628,42322028,'Європа'],
	'Німеччина': [357168,82800000,'Європа'],
	'Індія': [3287590,1210193422,'Азія'],
	'Аргентина': [2766890,40117096,'Південна Америка'],
	'Японія': [377972,127110047,'Азія'],
	'Фінляндія': [338145,5457429,'Європа'],
	'Алжир': [2381741,55813722,'Африка'],
	'Судан': [1886068,36992490,'Європа'],
	'Канада': [9984670,37067011,'Північна Америка'],
	'Сідней': [12144.6,4840600,'Австралія']
}

showSpisok(**A)

s = input('Введіть назву материка:')

print(inSearch(s,**A))

