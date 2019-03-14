import math

def triangle():
	var1, var2, var3 = input("pls, input sides ").split()
	var1, var2, var3 =[int(var1), int(var2), int(var3)]
	P_half = (var1 + var2 + var3) / 3
	S = math.sqrt(P_half*(P_half-var1)*(P_half-var2)*(P_half-var3))
	return(f"The answer is {S}")

figure = input("Enter the figure ")

if figure == "triangle":
	print(triangle())
elif figure == "circle":
	circle()
elif figure == "rectangle":
	rectangle()
else:
	print("Haven't this figure, retry")



