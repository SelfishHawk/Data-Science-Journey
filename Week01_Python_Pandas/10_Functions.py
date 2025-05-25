#Basics
def hello():
    print("Hello world")
hello()
def add(x,y):
    print(x+y)
add(12,14)
#Arbitrary arg
def name(*a):
    print("My name is ",a[1])
name("john","lisa","peter")
#recursion
def fac(n):
    if n==1:
        return 1
    return (n*fac(n-1))
print(fac(7))
#Lambda function
a= lambda b,c,z:b*c+(c+z)
print(a(5,2,8))
#local variable 
x=24
print(x)
def var():
    x=25
    return x
print(var())
print(x)
#Global variable
def var1():
    global x
    x=25
    return x
print(var1())
print(x)
#Prime check
def prime(n):
    if(n<=1):
        print("The no. is not prime")
        return 1
    trueN=n
    n=n-1
    while n!=1:
        if(trueN%n==0):
            print("The number is composite")
            return 1
        n-=1
    print("The no. is prime")
prime(17)
#create a list and print 
def list():
    a=[]
    n=1
    while n!=51:
        a.append(n**2)
        n+=1
    return a
abc=list()
print(abc)
def list1():
    x=len(abc)
    sum=0
    for i in range (0,x):
        sum+=abc[i]
    return sum
print(list1())
#Fibbonacci Series
def fibo(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
       return (fibo(a-1)+fibo(a-2))
print(fibo(7))