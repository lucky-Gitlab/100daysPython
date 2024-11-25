"""
a = "iit jammu"
def nameOfIitJammu():
    b  ='nirf67 '
    print(a+b)
    print(a,b)
    print(a+"nirf67")

nameOfIitJammu()    
...
"""
"""a = "global iit jammu"
print(a)
def nameOfIitJammu():
    a = "local iit bombay"
    print(a)
    a = "local iit roorkee"
    print(a)

a = "global iit jodhpur"
print(a)
nameOfIitJammu()    
print(a)

#2nd question
x = 'awesome'
def myfun():
    x = "fantastic"
    print("python is" + x)
myfun()
print(x)    
print("python is ",x)
print("python is "+ x)
"""
y = "great"
#use of global variable in a function or as a local
def myfun():
    print("entering in function check y vslue ")
    global y
    print(y)
    print("i am function see my y value is going to fsntstic ")
    print("c++ is " +y)
    y = "fantastic"
    print("c++ is " +y)

myfun()
print(y)
y = "awesome"
print(y)
myfun()