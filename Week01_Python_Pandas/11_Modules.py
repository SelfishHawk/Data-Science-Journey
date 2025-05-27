import datetime
x=datetime.datetime.now() #1st way of writing
print()
from datetime import date #2nd way of writing
y=date(1997,10,14)
print(y)
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%b"))
print(y.strftime("%m"))
print(y.strftime("%Y"))
print(y.strftime("%y"))
print(y.strftime("%M"))
print(y.strftime("%I"))
# print(y.strftime("%s"))
print(y.strftime("%f"))
print(y.strftime("%W"))
print(y.strftime("%w"))
import random
a=random.seed()
print(a)
b=random.randint(1,10)
print(b)
for i in range(2):
    random.seed()
    print(random.randint(1, 1000))
list1 = [1, 2, 3, 4, 5, 6] 
print(random.choice(list1))
c = ['apple', 'banana', 'cherry', 'date']
res = random.choices(c, k=3)
print(res)  
import math
d=max(98,88,999)
print(d)
e=min(98,88,999)
print(e)
f=pow(2,4)
print(f)
print(math.floor(2.4))
print(math.ceil(2.4))
print(abs(-2.4))
print(math.sqrt(969))
print(math.gcd(9,6))
print(math.exp(2))
import demo
print(demo.sum(2,3))
print(demo.b["name"])