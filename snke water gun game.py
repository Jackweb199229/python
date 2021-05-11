import random
list = ['s' , 'w' , 'g' ]
c = 10
no_of_ch = 0
cp = 0
hp = 0
print("\t for snake , water , gun Game \n\n ")
print(" \t s for snake\n \t w for water \n \t g for gun\n ")
#making the game in while loop.
while no_of_ch < c:
	user = input("\nenter snake , water ,gun : ")
	x = random.choice(list)
	if user == x:
		print(" Tie both 0 point to each \n ")
#   if user input (snake)
	elif user == 's' and x == 'g':
		cp = cp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print("computer wins 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
	elif user == 's' and x == 'w':
		hp = hp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print(" you  win 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
#  if user input (water)
	elif user == 'w' and x == 's':
		cp = cp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print("computer wins 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
	elif user == 'w' and x == 'g':
		hp = hp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print("You win 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
# user input (gun)
	elif user == 'g' and x == 's':
		hp = hp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print("You win 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
	elif user == 'g' and x == 'w':
		cp = cp+1
		print(f"your guess {user} and computer guess is {x}\n ")
		print("computer wins 1 point \n")
		print(f"computer point is {cp} and your point is {hp} \n ")
	else:
		print("you have input wrong \n ")
	no_of_ch = no_of_ch +1
print(f"{c - no_of_ch} is left of {c} \n ")
print("Game Over \n ")
if cp == hp:
	print("Tie")
elif cp>hp:
	print("computer wins and you loss\n")
else:
	print("You win\n")
print(f"your point is {hp} and computer point is {cp} \n")