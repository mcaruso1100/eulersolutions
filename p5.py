l = [11,13,14,16,17,18,19,20]
def isDiv(num):
	if all(num%x==0 for x in l):
		return True
	else:
		return False
if __name__ == "__main__":
	x = 20
	for n in range(20,99999999999,20):
		if(isDiv(n)):
			print(n)