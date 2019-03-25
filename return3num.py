
#WAP to take three numbers from and user and return their sum,return 0 if any of the two numbers are equal. 
x=int(input("Enter number "))
y=int(input("Enter number "))
z=int(input("Enter number "))
def sum(x,y,z):
	if(x==y or x==z):
		return(0)
	elif(y==z or y==x):
		return(0)
	elif(z==x or z==y):
		return(0)
	else:
		return(x+y+z)
a=sum(x,y,z)
print(a)