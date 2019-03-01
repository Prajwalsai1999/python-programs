
import random
x=0
y=0
l=["r","p","s"]

while True:
	#take input from user
	u=input("enter your choice rock paper  scissor,press n to discontinue")

	#to exit
	if u=='n':
		print("game over")
		exit() 
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)
	print("player chooses ",u)
	#compare the user and computer choice
	if u==c:
		print("tie")
		x=x
		y=y
	elif u=="r" and c=="p":
		print("comp wins")
		y=y+1
	elif u=="r" and c=="s":
		print("player wins")
		x=x+1
	elif u=="p" and c=="s":
		print("computer wins")
		y=y+1
	elif u=="p" and c=="r":
		print("player wins")
		x=x+1
	elif u=="s" and c=="r":
		print("computer wins")
		y=y+1
	elif u=="s" and c=="p":
		print("player wins")
		x=x+1
	else:
		print('Not valid')
	print("computer=",x,"\nuser=",y)

	


	


