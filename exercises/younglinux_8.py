var1, var2, var3 = input("pls enter the sides: ").split()
var1, var2, var3 = [int(var1), int(var2), int(var3)]

maxValue = max(var1, var2, var3)
print(f"MaxValue = {maxValue}")

thisList = [var1, var2, var3]
thisList.remove(maxValue)

sideOne = thisList[0]
sideTwo = thisList[1]
print(f"SideOne = {sideOne} , SideTwo = {sideTwo}")

totalSize = sideOne + sideTwo

if totalSize > maxValue:
	print("Triangle is existing")
else:
	print("Triangle isn't existing")
