from lib.utils import initialization
from lib.utils import check_env
from lib.core import console

def main():
	if not check_env():
		initialization()

	print('''
    	           ___
 _____ ___|  _|_ _ ___ ___ ___ _____
|     |_ -|  _| | | -_|   | . |     |
|_|_|_|___|_|  \_/|___|_|_|___|_|_|_|
         	MSFvenom-NG
         		Ver:1.1
    	''')
	console().interface()

if __name__ == '__main__':
	main()