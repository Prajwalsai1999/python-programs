#defining a function with no parameters
def func1():
	print("AEIOU")
	print("XYZ")
func1()
#defn a function using parameters
def func2(a):
	z=a*3
	print(z)
func2(4)

#defn a function using more than one parameter
def func3(x,y,z):
	P=x+y+z
	print(x)
	print(y)
	print(z)
	print(P)
func3(1,2,3)

#defn a function with default parameter
def func4(grade = "SEE",rank = 4):
	print(grade,rank,"topper\t")
func4("percentage",98)
func4()
#defn function with return value
def func5(x,y):
	k=x*y
	return(k)

g = func5(4,5)
print(g)

#defn function from another function or function calling another function
def func6(o):
	l = func5(9,8)
	w =l+o
	print(w)
func6(2)


















#finding max three values using function
#i/p:three value
#o/p:return the largest value

#2)sum of all the elements of the list 
 #i/p:list
 #o/p:sum of elements of the list