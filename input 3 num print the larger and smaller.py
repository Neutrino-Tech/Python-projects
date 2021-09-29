num1=int(input("1'st number: "))
num2=int(input("2'nd number: "))
num3=int(input("3'rd number: "))
if num1>num2:
	if num1>num3:
		print(num1," is the largest")
if num2>num1:
	if num2>=num3:
		print(num2," is the largest")
if num3>num1:
	if num3>=num2:
		print(num3," is the largest")
if num1<num2:
	if num1<num3:
		print(num1," is the smallest")
if num2<num1:
	if num2<num3:
		print(num2," is the smallest")
if  num3<num1:
	if num3<num2:
		print(num3," is the smallest")