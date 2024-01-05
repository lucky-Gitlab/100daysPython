#String Slicing & Operations on String
'''Length of a String
We can find the length of a string using len() function.

Example:
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

Output:
Mango is a 5 letter word.'''

#String as an array
'''A string is essentially a sequence of characters also called an array.
Thus we can access the elements of this array.

Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

Output:
Apple
i'''

#Note: This method of specifying the start and 
# end index to specify a part of a string is called slicing.

'''Slicing Example:
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

Output:
Apple
Pie
pleP
ApplePie'''

#Loop through a String:
'''Strings are arrays and arrays are iterable. Thus we can loop through strings.

Example:
alphabets = "ABCDE"
for i in alphabets:
    print(i)

Output:
A
B
C
D
E
'''

#code1
name = "lucky, bhardwaj"
print(name[0:5]) 
#note for slicing we use square bracket[] 
#but for fucntion we use bracket()

#CODE2
vishal = "lucky bhardwaj"
print(len(vishal))

#code3
fruit = "banana"
len1 = len(fruit)
print("banana is a ", len1,"letter word.")


#code4
fruit ="mango" 
len1 = len(fruit)
print(len1)
print(fruit[0:4]) #including 0  but not 4
print(fruit[1:4]) #INCLUDING 1 BUT BOT 4
print(fruit[0:5])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) # THERE IS NO SENSSE OF 4 TO 2 i.e 4:2
print(fruit[-3:-1])#2:4 
