import random
l1 = ['r','p','s']

u = input("r/p/s")

c = random.choice(l1)

if l1.index(u) == (l1.index(c)+1)%3:
	print(u,">",c)

else:
	print(c,">",u)