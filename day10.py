#What are strings?
'''In python, anything that you enclose between single or double quotation marks is considered a string. 
A string is essentially a sequence or array of textual data. Strings are used when working 
with Unicode characters.

Example
name = "Harry"
print("Hello, " + name)'''

#Output
'''
Hello, Harry
'''

#Note: It does not matter whether you enclose your strings in single or double quotes, 
# the output remains the same.

#Sometimes, the user might need to put quotation marks in between the strings. Example, 
# consider the sentence: 
#He said, “I want to eat an apple”.

#How will you print this statement in python?: He said, "I want to eat an apple".
# We will definitely use single quotes for our convenience

#print('He said, "I want to eat an apple".')

'''
Multiline Strings
If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Accessing Characters of a String
In Python, string is like an array of characters. We can access
parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])

#Looping through the string
We can loop through strings using a for loop like this:

for character in name:
    print(character)

Above code prints all the characters in the string name one by one!'''


#code 1
name = "lucky"
print("hello ," + name )

#code2
#apple ="he said ," i want to eat an apple" 
# here i used  two times  of double colon so we have to either use single 
# #or /with double colon
#print(apple)

#code3
kiwi ='he said ," i want to eat an apple'
print(kiwi)
#here i used single colon and my sentence is correct 

#code4
onion  ="he said ,\" i want to eat an apple"
print(onion)
 
 #code8
vishal = '''he is very good coder 
and he will definitly will 
take a good job ''' # due to triple colon we can print  more stirngs
print(vishal )

#code5
name = "lucky"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) #it will not print because string consist only 0 to 4 characters in lucky 

#code 9
vishal = '''he is very good coder 
and he  definitly will 
get a good job ''' # due to triple colon we can print  more stirngs
print("lets use a for loop\n")
for character in vishal :
    print(character)

