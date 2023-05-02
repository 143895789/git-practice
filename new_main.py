# Test python env
def print_hello():
	animals = ['dog', 'cat', 'hamster', 'tiger']
	food = [
		'Spagetti',
		'Pizza',
		'bibimbob'
		] # w/o trailing comma
	names = [
		'John',
		'jane',
		'Gil-dong'
		'dong-hoon',
		'Yeon-jin',
		] # w/ trailing comma
	for f_name in names:
		print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
