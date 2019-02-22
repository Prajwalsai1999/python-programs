import random
p=0
d=0

while True:
	r = input("Press r to roll the dice:")

	if r =="r":
		d=random.randint(1,6)
		print("You got:",d)

	if d==1  or d==6:
		p=d
		break
print("Congratulations ,you are in the game.You are at:",p)
