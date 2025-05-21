a={"Name":"John","Age":24,"Class":2}
print(a)
x=a.values()
print(x)
print(a.__len__())
y=a.keys()
print(y)
z=a.copy()
print(z)
m=a.items()
print(m)
for x,y in a.items():
    print(x,"-",y)
for x in a:
    print(a[x])
n=a.get("Name")
print(n)
o=a.setdefault("Class",24)
print(o)
a.popitem()
print(a)
a.pop("Age")
print(a)
a.clear()
print(a)
a.update({"Name":"Lisa","Stat":"Great"})
print(a)
emp={1:{"Name":"Sachin","Age":20},
     2:{"Name":"Shella","Age":67}}
print(emp[1])
#Sort according to values
op={"a":1,"b":99,"C":10,"d":7,"e":66}
sor=sorted(op.values())
print(sor)
sqr={}
for i in range(1,16):
    sqr.update({i:i*i})
# while True:
#     x=int(input("Enter the integer "))
#     y=x*x
#     sqr.update({x:y})
#     cont=input("Do you want to break ")
#     if cont=="yes" or cont=="YES":
#         break
print(sqr)