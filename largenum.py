#finding max three values using function
#i/p:three value
#o/p:return the largest value


def funcmax(l,m,n):
 	if (l>m) and (l>n):
 		return l

 	elif (m>l) and (m>n):
 		return m 
 	
 	elif (n>l) and (n>m):
 		return n

l= input("1st number ")
m= input("2nd number ")
n= input("3rd number ")


z=max(l,m,n)
print(z,"is the largest number of the three")



