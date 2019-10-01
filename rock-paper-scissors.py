import random
from termcolor import colored, cprint

user_score = 0
comp_score = 0
isWinner = None
state = 'yes'

while state != 'no':

	print(colored('...Rock...Paper...Scissors...', 'cyan', attrs=['reverse', 'bold']))

	while user_score < 3 and comp_score < 3:

		comp_answer = None
		num = random.randint(1, 3)

		if num == 1:
			comp_answer = 'rock'
		elif num == 2:
			comp_answer = 'paper'
		else:
			comp_answer = 'scissors'

		user_answer = input('Rock, Paper or Scissors? ').lower()

		while user_answer != 'rock' and user_answer != 'paper' and user_answer != 'scissors':

			user_answer = input('Please choose one: Rock, Paper or Scissors? ').lower()

		print(colored(f'Computer plays {comp_answer.title()}, You play {user_answer.title()}', "grey", attrs=['bold']))	

		def comp_win():		
			print(colored("Computer wins!", "red", attrs=['bold']))
			print(colored(f'Computer total score: {comp_score} | Your total score: {user_score}', "grey", attrs=['bold']))

		def user_win():	
			print(colored("You win!", "green", attrs=['bold']))
			print(colored(f'Computer total score: {comp_score} | Your total score: {user_score}', "grey", attrs=['bold']))

		if comp_answer == user_answer:
			print(colored("It's a tie!", "cyan", attrs=['bold']))			
			print(colored(f'Computer total score: {comp_score} | Your total score: {user_score}', "grey", attrs=['bold']))		
		elif comp_answer == 'rock':
			if user_answer == 'paper':
				user_score += 1	
				user_win()
			else: 
				comp_score += 1		
				comp_win()
		elif comp_answer == 'scissors':
			if user_answer == 'rock':
				user_score += 1	
				user_win()
			else:
				comp_score += 1		
				comp_win()
		elif comp_answer == 'paper':
			if user_answer == 'rock':
				comp_score += 1		
				comp_win()
			else: 
				user_score += 1	
				user_win()

	if user_score > comp_score:
		isWinner = "You won this game!"
	else:
		isWinner = "Computer won this game!"

	print(colored(f'{isWinner}', "cyan", attrs=['reverse', 'blink']))

	state = input(colored("Would you like to play again? (yes/no) ", "cyan", attrs=['bold'])).lower()

	while state != 'yes' and state != 'no':
		state = input("Please choose one: 'yes' / 'no' ").lower()

	if state == 'yes':
		user_score = 0
		comp_score = 0

print(colored('Thank you for playing! Have a good day :)', "cyan", attrs=['bold']))























