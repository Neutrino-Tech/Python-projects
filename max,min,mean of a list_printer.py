ls=[]
n=int(input("Enter number of elemets: "))
for i in range(n):
    ele=int(input("Enter number: "))
    ls.append(ele)

print("Your list is:",ls)
max = ls[0]
min = ls[0]
for i in range(n):
    if ls[i] > max:
        max = ls[i]
    if ls[i] < min:
        min = ls[i]
print(max,"is the maximum")
print(min,"is the minimum")

mean=sum(ls)/n
print(mean,"is the mean")
