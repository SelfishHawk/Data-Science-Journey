# Pattern problem 1
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
#pattern 2
print("Pattern 2")
for i in range (1,6):
    for j in range (6-i,0,-1):
        print(i,end=" ")
    print("\n")
#pattern 3
print("Pattern 3")
for i in range(1,6):
    for j in range(6-i,0,-1):
        print(" ",end=" ")
    for k in range (i):
        print("*",end=" ")
    print("\n")
#pattern 4
print("Pattern 4")
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
#pattern 5
print("Pattern 5")
for i in range (1,11):
    for j in range(1, i+1):
        print(i*j,end=" ")
    print()
#Fibbonaci Series
a=0
b=1
n=int(input("Enter the no. of digits in series"))
print("0 1",end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print("\n")
#Prime or not
n=int(input("Enter the no. to check "))
for i in range(2,n):
    if n%i==0:
        print("No. is composite ")
        break
else:
    print("It is a prime no.")
#sum of all even number upto 50
sum=0
for a in range (2,51):
    if a%2==0:
        sum+=a
print("Sum of all even no. upto 50 is ",sum)
#check a no. is divisble by 8 and 12 simultaneously upto 100
num=int(input("Enter the number "))
if(num>=0) and (num<=100):
    for b in range(1,101):
        if(b%8==0) and (b%12==0):
            print(b,end=" ")
else:
    print("No. out of bounds")