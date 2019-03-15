n = input("pls enter the degree ")
m = input("pls enter the number ")
n, m = [int(n), int(m)]
b = 0
if n == 0:
	b = 1
else:
	while n > 0:
	
		if b == 0:
			b = m
		else:
			b = b * m
		n = n - 1

print(b)

