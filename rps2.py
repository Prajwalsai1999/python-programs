
import random
x=0
y=0
l=["rock","paper","scissor"]
d={"r":"rock","p":"paper","s":"scissor"}
while True:
	#take input from user
	u=input("enter your choice rock paper  scissor,press n to discontinue ")

	#to exit
	if u=='n':
		print("game over")
		exit() 
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)
	print("player chooses ",d[u])
	#compare the user and computer choice
	if d[u]==c:
		print("tie")
		x=x
		y=y
	elif d[u]=="rock" and c=="paper":
		print("comp wins")
		y=y+1
	elif d[u]=="rock" and c=="scissor":
		print("player wins")
		x=x+1
	elif d[u]=="paper" and c=="scissor":
		print("computer wins")
		y=y+1
	elif d[u]=="paper" and c=="rock":
		print("player wins")
		x=x+1
	elif d[u]=="scissor" and c=="rock":
		print("computer wins")
		y=y+1
	elif d[u]=="scissor" and c=="paper":
		print("player wins")
		x=x+1
	else:
		print('Not valid')
	print("computer=",x,"\nuser=",y)

	


	


