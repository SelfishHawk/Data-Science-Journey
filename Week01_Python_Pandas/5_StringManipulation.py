a="Harry potter and the Prisoner of Azkaban"
print(a)
print(len(a)) #Gives the length of a string
print(a.count("a")) #counts no. of times a occured
print(a.lower())
print(a.upper())
print(a.casefold())
print(a.index("o",15,32))
print(a.find("o",26,32))
print(a.capitalize())
name="John"
age="24"
b="My name is {}.And the age is {}"
print(b.format(name,age))
print(name.center(10,"*"))
print(a.endswith("n"))
print(a.startswith("h"))
print(a.swapcase())
c="    *****harry potter_____ "
print(c)
print(c.strip("*, ,_"))
d="#OOF#OMW#GRWM#LOL#LMAO"
print(d.split("#"))
x=name.ljust(20,"*")
print(x,"is my name.")
y=name.rjust(20,"&")
print(y,"is my name.")
e="My name is john"
print(e.replace("john","Lisa"))
print(a.rindex("er"))
print(a.rfind("er"))
#String slicing
print(a[:5])
print(a[6:12])
print(a[-7:])
#Reverse a string
f="Apsara"
print(f[::-1])
print(f[::2])