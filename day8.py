#the conversion of one data type into 
# other data type is known as type casting in pyhton or type conversion in python

#these are of two types 
# Ist is : explicit type conversion
#2nd is : implicit type conversion
# the conversion of one data type into another data type , done via developer or programmers manuallly as per the requirement , known as the 
# explicit type conversion 
#It can be achievd with the help of pythons built in type conversion function as int(), float()etc.



a = "1" #here this is string not integer 
b = "6"# here this is string not integer 
print (a+b)
 
 #for example explicit function
a = "1"
b = "5"
print (int(a)+ int(b))

#but in implicit type casting it convert automatically
c = 1.9
d= 8
print (c+d) #here impllicit type casting convert 8(int )into a  float datatype which is automatically 
