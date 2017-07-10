from games import colors, quiz, run

def mainMenu():
	print("Welcome to Python Minigames\n""===========================")
	("Choose from the following available options:")
	userInput=1
	while userInput:
		print("1. Running in Python\n")
		print("2. Colors and words\n")
		print("3. Time for a quiz\n")
		print("0. Exit\n""===========================")
		userInput = input("Enter your choice: ")
		if userInput == "1":
			run.startrunning()
		elif userInput == "2":
			colors.createGUI()
		elif userInput == "0":
			break
		else:
			userInput = input("Something terribly wrong happened\nTry again! ")


if __name__ == '__main__':
	mainMenu()