num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
if num1 > num2:
      if num1 > num3:
            largest = num1
if num2 > num1:
      if num2 > num3:
            largest = num2
if num3 > num1:
      if num3 > num2:
            largest = num3
print("The largest number is", largest)

if num1 < num2:
      if num1 < num3:
            smallest = num1
if num2 < num1:
      if num2 < num3:
            smallest = num2
if num3 < num1:
      if num3 < num2:
            smallest = num3
print("The smallest number is", smallest)