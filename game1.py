import random
lst=['s' , 'w' , 'g']
ch= 10 # chance
n = 0  # no of chance
cp = 0 #computer point
hp = 0 #human point
print("\t\t Snake , water , gun , Game \n\n ")
print("S for snake \n W for water \n g for gun\n")
 # MAKING THE GAME IN WHILE LOOP.
while n<ch:
	a = input("Sanke,water,gun: ")
	rand = random.choice(a)
    if(a==rand):
 	   print("Tie Both 0 point to each\n")
 # USER INPUT (S)
    elif a == "s" and rand=="g":
    	cp = cp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("computer wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
    elif a=="s" and rand=="w":
    	hp=hp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("Human wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
 		
 		#USER INPUT "W"
    elif a=="w" and rand=="s":
    	cp=cp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("computer wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
 		
    elif a=="w" and rand=="g":
    	hp=hp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("Human wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
 		
 	# USER INPUT "G"
    elif a=="g" and rand=="s":
    	hp=hp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("Human wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
 		
    elif a=="g" and rand=="w":
    	cp=cp+1
 	   print(f"your guess {a} and computer guess is {rand}\n")
 	   print("computer wins 1 point\n")
 	   print(f"computer_point is {cp} and your point is {hp}\n")
 	
    else:
    	print("You have input wrong \n")
 	   n=n+1
 	   print(f"{ch-n} is left of {ch} \n")
 	   print("Game over")
    if cp == hp:
    	print("Tie")
    elif cp>hp:
    	print("computer wins and you lose")
    else:
    	print(f"your point is {hp} and computer point is {cp}")
 		
 
 