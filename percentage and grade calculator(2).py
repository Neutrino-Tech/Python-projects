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
if total_percentage>=97:
	grade="A+"
elif total_percentage>=93:
    grade="A"
elif total_percentage>=90:
    grade="A-"
elif total_percentage>=87:
    grade="B+"
elif total_percentage>=83:
	grade="B"
elif total_percentage>=80:
	grade="B-"
elif total_percentage>=77:
    grade="C+"
elif total_percentage>=73:
    grade="C"
elif total_percentage>=70:
	grade="C-"
elif total_percentage>=67:
	grade="D+"
elif total_percentage>=65:
	grade="D"
elif total_percentage>=64:
	grade="D- "
elif total_percentage>=60:
	grade="E"
elif total_percentage>=50:
	grade="F"
elif total_percentage>=40:
	grade="G"
elif total_percentage>=33:
    grade="H"
elif total_percentage<=32:
    grade="FAIL"
print(name,'of class',c+'th',s,'scored',total_percentage,'% &',grade,'Grade')
print("""\nCongratulation for your achievement
Choose what you like
Study hard in your upcoming classes""")



