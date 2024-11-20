#String methods
'''Python provides a set of built-in methods that we can use to alter and modify the strings.
NOTE : strings are immutable (there original form remain same
but changes occur in their second form )
upper() :
The upper() method converts a string to upper case.

Example:
str1 = "AbcDEfghIJ"
print(str1.upper())

Output:
ABCDEFGHIJ'''

#CODE1
a = "lucky"
print(len(a))
print(a.upper())


#lower()
'''The lower() method converts a string to lower case.

Example:
str1 = "AbcDEfghIJ"
print(str1.lower())

Output:
abcdefghij '''

#CODE2

a = "vIsHal"
print(len(a))
print(a.lower())


#strip() :
'''The strip() method removes any white spaces before 
and after the string.

Example:
str2 = " Silver Spoon "
print(str2.strip())

Output:
Silver Spoon'''
str2 = " Silver Spoon "
print(str2.strip())

#rstrip() :
'''the rstrip() removes any trailing (NOT LEADING )characters. Example:

str3 = "Hello !!!"
print(str3.rstrip("!"))

Output:
Hello'''

#code3

a = "????  LUCKY  ????"
print(len(a))
print(a.rstrip("????")) # it remove only back
#character not leading character
 

#replace() :
'''The replace() method replaces all occurences of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

Output:
Silver Moon'''

#code4
a= "lucky vishal "
print(len(a))
print(a.replace("vishal", "prince"))


#split() :
'''The split() method splits the given string at the
specified instance and 
returns the separated strings as list items.

Example:
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

Output:
['Silver', 'Spoon']'''
#There are various other string methods 
# that we can use to modify our strings.

  #code5
a = " ???lucky bhardwaj  !!!!!"
print(len(a))
print(a.split("  "))

#capitalize() :
'''The capitalize() method turns only the first character 
of the string to uppercase 
and the rest other characters of the string
are turned to lowercase. The string has no effect
if the first character is already uppercase.

Example:
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)

Output:
Hello
Hello world'''

#code6
a= "lucky Bhardwaj"
cap1 = a.capitalize()
print(cap1)
b= "my mom is my LIFE"
cap2 = b.capitalize()
print(cap2)

#center() :)
'''The center() method aligns the string to the
center as per the parameters given by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))

Output:
            Welcome to the Console!!!'''
#code 7
a = "introduction to js"
len1 = len(a)
print(len1)
print(a.center(30))
print(a.center(80))


#We can also provide padding character.
# It will fill the rest of the fill characters 
# provided by the user.

#Example:
#str1 = "Welcome to the Console!!!"
#print(str1.center(50, "."))

#Output:
#............Welcome to the Console!!!.............

#code8

a = "life is so beautiful"
len1 = len(a)
print(len1)
print(a.center(40))
print(a.center(50,(".")))  #nice work 

#count() :
'''The count() method returns the number of times the given value has occurred within the given string.

Example:
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

Output:
4'''

#endswith() :
'''The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

Example :
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) 

Output:
True'''

#We can even also check for a value in-between the string by providing start and end index positions.

#Example:
#str1 = "Welcome to the Console !!!"
#print(str1.endswith("to", 4, 10))

#Output:
#True

#code 9
a = "lucky"
print(len(a))
print(a.endswith("c",2,3))
print(a.endswith("uc",2,3))


#find() :
'''The find() method searches for the 
first occurrence of the given value and returns
 the index where it is present.
If given value is absent from the string then return -1.

Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))



Output:
10

As we can see, this method is somewhat
similar to the index() method. The major difference 
being that index() raises an exception if 
value is absent whereas find() does not.

Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

Output:
-1 '''



#index() :
'''The index() method searches for the first
+
occurrence of the
given value and returns
the index where it is present. 
If given value is absent from the string
then raise an exception.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

Output:
13


As we can see, this method is somewhat similar to the 
find() method. The major difference
being that index() raises an exception 
if value is absent whereas find() does not.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))

Output:
ValueError: substring not found'''
a = "lucky is from palwal" #space is also count
print(a.find("palwal"))
print(a.find("delhi"))
print(a.index("is"))
print(a.index("lucky"))
print(a.index("from"))

#isalnum() :
'''The isalnum() method returns True
only if the entire string only consists of A-Z, a-z, 0-9.
If any other characters or punctuations are present, 
then it returns False.

Example 1:
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

Output:

True'''
#code10
a = "lucky19"
print(a.isalnum())
b = "lucky19!"
print(b.isalnum())

#isalpha() :
'''The isalnum() method returns True only 
if the entire string only consists of A-Z, a-z. 
If any other characters or punctuations or 
numbers(0-9) are present, then it returns False.

Example :
str1 = "Welcome"
print(str1.isalpha())

Output:
True '''
#code11
a = "lucky"
print(a.isalpha())
b = "lucky19"
print(b.isalpha())

#islower() :
'''The islower() method returns
True if all the characters in the string are lower case,
else it returns False.

Example:
str1 = "hello world"
print(str1.islower())

Output:
True'''
#code12
a = "lucky is an iitian"
print(a.islower())
#isprintable() :
''''The isprintable() method returns True if all the values
within the given string are printable, 
if not, then return False.

Example :
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

Output:
True'''
#code13
a =" vishu is a bad boy \n"
print(a.isprintable()) #/n it is not printable because we cannot print /n


#isspace() :
'''The isspace() method returns True only and only if the string contains white spaces, else returns False.

Example:
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

Output:
True
True'''

#istitle() :
'''The istitile() returns True only if the first letter of each word of the string is capitalized, 
else it returns False.

Example:
str1 = "World Health Organization" 
print(str1.istitle())

Output:
True

Example:
str2 = "To kill a Mocking bird"
print(str2.istitle())

Output:
False'''

#isupper() :
'''The isupper() method returns True if all the characters in the string are upper case, else it returns False.

Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

Output:
True'''

#startswith() :
'''The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

Output:
True'''

#swapcase() :
'''The swapcase() method changes the character casing of the string. 
Upper case are converted to lower case and lower case to upper case.

Example:
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

Output:
pYTHON IS A iNTERPRETED lANGUAGE'''

#title() :
'''The title() method capitalizes each letter of the word within the string.

Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

Output:
He'S Name Is Dan. Dan Is An Honest Man.'''
LUCKY IS MY LIFE 

