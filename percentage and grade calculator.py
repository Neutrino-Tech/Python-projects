print("""Welcome to Percentage & Grade Calculator
YOUR MARKS WILL NOT BE SAVED
Please enter your marks out of 100\n""")
name=input("Enter your Name: ")
c=input("Enter your Class: ")
s=input("Enter your Section: ")
english=int(input("Marks in English: "))
hindi=int(input("Marks in Hindi: "))
maths=int(input("Marks in Maths: "))
science=int(input("Marks in Science: "))
sst=int(input("Marks in Social Science: "))
total_percentage = (english+hindi+maths+science+sst)/5
print(name,'of class',c+'th',s,'scored',total_percentage,'%')
if total_percentage>=97:
	print("Your Grade: A+")
elif total_percentage>=93:
    print("Your Grade: A")
elif total_percentage>=90:
    print("Your Grade: A-")
elif total_percentage>=87:
    print("Your Grade: B+")
elif total_percentage>=83:
	print("Your Grade: B")
elif total_percentage>=80:
	print("Your Grade: B-")
elif total_percentage>=77:
    print("Your Grade: C+")
elif total_percentage>=73:
    print("Your Grade: C")
elif total_percentage>=70:
	print("Your Grade: C-")
elif total_percentage>=67:
	print("Your Grade: D+")
elif total_percentage>=65:
	print("Your Grade: D")
elif total_percentage>=64:
	print("Your Grade: D-")
elif total_percentage>=60:
	print("Your Grade: E")
elif total_percentage>=50:
	print("Your Grade: F")
elif total_percentage>=40:
	print("Your Grade: G")
elif total_percentage>=33:
    print("Your Grade: H")
elif total_percentage<=32:
    print("FAIL")
print("""\nCongratulation for your achievement
Choose what you like
Study hard in your upcoming classes""")

