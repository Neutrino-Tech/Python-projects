num1=int (input("enter 1st number: "))
num2=int (input("enter 2nd number: "))
num3=int (input("enter 3rd number: "))
if num1>num2 :
	    if num1>num3:
		    print(num1," is the largest number")
elif num2>num1:
        if num2>num3:
            print(num2," is the largest number")
else :
	print(num3," is the largest number")

if num1>num2:
	    if num1>num3:
		    print(num1," is the smallest number")
elif num2>num3:
	    if num2>num3:
		    print(num2," is the smallest number")
else :
	print(num3," is the smallest number")