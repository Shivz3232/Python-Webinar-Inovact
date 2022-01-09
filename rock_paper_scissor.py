# Random library provided by python. Check docs for more info
import random

# List of available options
options = ["rock", "scissor", "paper"]

# Game menu
print("Enter 1 to play rock!")
print("Enter 2 to play scissor!")
print("Enter 3 to play paper!")

# Take input
userChoice = int(input())

# Find the option played from the list
userPlay = options[userChoice - 1]

# Use the sample function of random library to choose one option randomly from the 
# list of options
pythonPlay = random.sample(options, 1)

# Sample function will return a list with number of elements
# Since we have sampled only one option, we will take the first element from this array
# Uncomment the below line to see the output of sample function
# print(pythonPlay)
pythonPlay = pythonPlay[0]

# Rock Paper Scissor Logic
if userPlay == pythonPlay:
	print("Python played " + pythonPlay + ", so its a draw!")

elif userPlay == "rock":
	if pythonPlay == "scissor":
		print("Python played " + pythonPlay + ", you won!")
	else:
		print("Python played " + pythonPlay + ", you lost!")

elif userPlay == "paper":
	if pythonPlay == "rock":
		print("Python played " + pythonPlay + ", you won!")
	else:
		print("Python played " + pythonPlay + ", you lost!")

else:
	if pythonPlay == "rock":
		print("Python played " + pythonPlay + ", you lost!")
	else:
		print("Python played " + pythonPlay + ", you won!")
