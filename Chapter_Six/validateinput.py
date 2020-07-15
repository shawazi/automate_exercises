while True:
	print('Enter your age:')
	age=input()
	if age.isdecimal():
		break
	print('Please enter a goshdang number for your age, bruh.')

while True:
	print('Select a new password (letters and numbers only, bruh):')
	password = input()
	if password.isalnum():
		break
	print('please enter only lettaz and numbaz, bruh.')