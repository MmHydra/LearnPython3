Number = int(input("n = "))

def func(Number):
	VarPrint = ""
	if Number == 0:
		return "The number is 0";
	elif Number < 0:
		VarPrint = VarPrint + "Negative"
	else:
		VarPrint = VarPrint + "Positive"
	if Number >= 10 or Number <= -10:
		VarPrint = VarPrint + " two-digit"
		return VarPrint
	else:
		VarPrint = VarPrint + " one-digit"
		return VarPrint


Result = func(Number)
print(f"Result = {Result}")
