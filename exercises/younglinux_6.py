numbers = input("Pls enter the number ")
numbers = int(numbers)
numbers_2 = 0

while numbers > 0:
	
	n =  numbers % 10
	numbers_2 = numbers_2 + n
	numbers_2 = numbers_2 * 10
	numbers = numbers // 10

numbers_2 = numbers_2 / 10
print(numbers_2)

	

