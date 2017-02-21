

def isPali(x):
	s = str(x)
	if s == s[::-1]:
		print(s)
		return True



if __name__ == "__main__":
	z=0
	for x in range(100,999):
		for y in range(100,999):
			prod = x*y
			if isPali(prod) and prod>z:
				z=prod
					
	print(z)
