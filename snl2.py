import random
d={8:37,11:2,25:4,38:9,30:68,65:46,32:81,93:64,76:97,89:70}
p=random.choice([2,8,11,34,38,89,93,52])
print("you got ",p)
if  p in d:
	if p>d[p]:
		print("snake")
	else:
		print("ladder")
	print("you can move to")
