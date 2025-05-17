a=["Hulk","Thor","captain","Bucky","Widow",69,88]
print(a)
print(type(a))
print(a[0:3])
print(a[::-1])
b=[7,10,1,100]
[print (i) for i in a]
b.sort()
print(b)
prod=1
for i in b:
    prod*=i
print("Total product is",prod)
height=len(b)-1
print("Largest element is ",b[height])
c=[12,55,76,11,30,4,99]
smallest=c[0]
for i in c:
    if (i<smallest):
        smallest=i
print("Smallest in c list is ",smallest)