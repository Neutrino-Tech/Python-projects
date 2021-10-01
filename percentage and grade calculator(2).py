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
total_percentage=(english+hindi+maths+science+sst)/5
cgpa=int(total_percentage/9.5)
if total_percentage>=91:
	grade="A1"
elif total_percentage>=81:
	grade="A2"
elif total_percentage>=71:
	grade="B1"
elif total_percentage>=61:
	grade="B2"
elif total_percentage>=51:
	grade="C1"
elif total_percentage>=41:
	grade="C2"
elif total_percentage>=32.5:
    grade="D1"
else:
    grade="FAIL"
print(name,'of class',c+'th',s,'scored',total_percentage,'% &',cgpa,'CGPA','with',grade,)

