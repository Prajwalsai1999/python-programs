import random
p=0
d=0
snl={8:37,11:2,25:4,38:9,30:68,65:46,32:81,93:64,76:97,89:70}

def rolldice():
	return random.randint(1,6)

#get 1 or 6 to enter the game. 
while True:
	r = input("Press r to roll the dice, q to quit:")
	if r == "r":
		d = rolldice()
		print(" you got ",d)		
		if d == 1  or d == 6:
			p=d
			print("Congratulations ,you are in the game.You are at:",p)
			print("You start on ",p)
			break
		else:
			print("you need to get 6 or 1 to start.Try again.")
	elif r == 'q':
		exit()
while True:
	r=input("press r to roll dice")
	if (r == "r"):
		d=rolldice()
		print("you got ",d)
		p=p+d
		if p == 100:
			print("hurray! you won")
			exit()
		if p > 100:
			p=p-d
			print("you need ",100-p, "to win")
		if p in snl:
			if(p<snl[p]):
				print ("ladder!!!",p)
			else:
				print("snake!!!",p)
			p=snl[p]
			print(p)
		print("you are at ",p)
	elif r == 'q':
		exit()


		


