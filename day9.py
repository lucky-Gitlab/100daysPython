# TAKING USER INPUT IN PYTHON 
'''
In python , we can take user input directly by using input() function. This input 
functn gives a return value as string/ character hence we have to pass that into a variable
'''
#SYNTAX
'''
variable = input()
'''
'''
but input function returns the value as string. Hence we have to typecast them 
whenever required to another datatype.
'''
#example 
'''
variable = int(input())
variable = float(input())
'''
#we can also dsiplay a text using input funcrtion . this will make 
#input() fucntion take user input and display a message as welll

'''
a = input("enter the name")
'''

a = input ()
print(a)


# SECOND CODE 
a = input()
print ("my name is ", a)

#third code 
a = input("enter your name :")
print ("my name is :", a)

#fourth code 
x = input("enter first number:  ")
y= input("enter second number : ")
print (x+y) # it gives output in string because  , 
#here input gives only retunn value in string so we have to change it in another datatype 

#fifth code
num1 =  input("enter first number:" )
num2=  input ("enter second number :")
print ((int(num1)+int(num2))) #here input will give a integer value not a string value 
