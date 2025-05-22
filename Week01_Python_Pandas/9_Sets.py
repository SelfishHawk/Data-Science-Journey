s1={"Ironman","Hulk","Captain America","Bucky"}
s2={"Thor","Loki","Odin","Hela"}
s3={"Bucky","Hulk"}
a={"Captain America","Thor","Loki","Spiderman","Dr. Strange","Panther"}
b={"Captain America","Thor","Loki","Falcon","Antman","Thanos"}
s2.add("Black Widow")
print(s2)
s2.pop()
print(s2)
s2.discard("Black Widow")
print(s2)
s4=s2.copy()
print(s4)
print(s2.isdisjoint(s1))
print(s3.issubset(s1))
print(s3.issuperset(s1))
print(s1.issuperset(s3))
s4.update(s3)
print(s4)
s4.clear()
print(s4)
print(s3.union(s2))
x=s1.difference(s3)
print(x)
s1.difference_update(s3)
print(s1)
y=a.intersection(s1)
print(y)
s1.intersection_update(a)
print(s1)
z=a.symmetric_difference(b)
print(z)
a.symmetric_difference_update(b)
print(a)
# Min and max
c={12,33,44,444,86,98,99}
print(min(c))
print(max(c))