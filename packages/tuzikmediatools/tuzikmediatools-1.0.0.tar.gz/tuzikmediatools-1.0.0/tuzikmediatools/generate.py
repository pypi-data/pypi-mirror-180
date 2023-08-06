# Copyright RimMirK (rimmirk) 2022 | https://t.me/RimMirK | GPLv3 license

from random import randint

def get_result(lenght, category, symbols_pack=None, numbers_range=None):
	result = ''
	if category == 'numbers':
		for _ in range(lenght):
			result += str(randint(numbers_range[0], numbers_range[1]))
		return result

	else:
		for _ in range(lenght):
			result += str(symbols_pack[randint(0, len(symbols_pack)-1)])
		return result

def generate(lenght, 
			 symbols='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[]{};\':",./<>?/\\|№', 
			 numbers_range=(0, 9),
			 case=None):

	if symbols == 'numbers':
		return get_result(lenght, 'numbers', numbers_range=numbers_range)

	elif symbols == 'a-z':
		if case == 'low':
			return get_result(lenght, 'symbols', symbols_pack='qwertyuiopasdfghjklzxcvbnm')
		elif case == 'up':
			return get_result(lenght, 'symbols', symbols_pack='QWERTYUIOPASDFGHJKLZXCVBNM')
		else:
			return get_result(lenght, 'symbols', symbols_pack='qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
	


	else:
		return get_result(lenght, 'symbols', symbols_pack=symbols)

