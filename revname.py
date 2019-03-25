#WAP to print the name of user in reverse  order(i.e. Initials Name .Take input from user )
s=input("enter the name: ")
  
print ("The original string  is : ",end="") 
print (s) 

s= "".join(reversed(s)) 

print ("The reversed string(using reversed) is : ",end="") 
print (s)