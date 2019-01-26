import random
z=random.randrange(1,100)
gamewon=0
print("you have 10 turns")
for x in range(1,10+1):
	h=10-x
	y=int(input("guess the random number"))
	if(y>z):
		print("go lower")
		print("you have " , h , " turns left")
	elif(y<=z):
		print("go higher")
		print("you have " , h , " turns left")
	elif(y==x):
		print("you are smarty pants ")
		print("you have " , h , " turns left")
		gamewon=1
		break

if gamewon==0:
	print("you loose")
	print("the secret number was " , z)	
else:		
	print("you win")			
