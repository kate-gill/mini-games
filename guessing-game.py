import random
from termcolor import colored, cprint

state = 'yes'

while state != 'no':

	print(colored("Let's play a guessing game!", 'cyan', attrs=['reverse', 'bold']))

	answer = random.randint(1, 10)
	user_guess = 0

	while int(user_guess) != answer:

		user_guess = input('Enter a number from 1 to 10: ')

		while user_guess not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
			user_guess = input('It has to be a number from 1 to 10! ')

		if int(user_guess) < answer:
			print(colored('Your guess is too low!', 'grey', attrs=['bold']))
		elif int(user_guess) > answer:
			print(colored('Your guess is too high!', 'grey', attrs=['bold']))

	print(colored('You guessed it!', 'cyan', attrs=['reverse', 'bold']))

	state = input(colored('Would you like to play again? (yes/no)', 'cyan', attrs=['bold']))

	while state != 'yes' and state != 'no':
		state = input(colored("Please choose one: 'yes' / 'no' ", attrs=['bold']))

print(colored('Thank you for playing! Have a good day :)', 'cyan', attrs=['bold']))



