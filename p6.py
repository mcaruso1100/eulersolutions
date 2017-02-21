def sumofsquares(x):
	sums=0
	for y in range(1,x):
		print("y^2 {}".format(y**2))
		sums = sums + y**2
	return sums

def squareofsums(x):
	return sum(range(1,x))**2
if __name__=="__main__":
	
	sqr = squareofsums(101)
	sums=sumofsquares(101)
	diff= sqr -sums
	print("Sum of squares = {}".format(sums))
	print("Square of sums = {}".format(sqr))
	print("diff = {}".format(diff))