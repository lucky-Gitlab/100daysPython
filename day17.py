# implementing loops

number= int(input("enter a number : "))
result = 0
for i in range(1,number+1):
    #logic 
    result = i**2 + result

print(result)