#Tuple
# immutable
#surrounded by Round Brackets for single character end with (,)like = a='c',
a='c',
print(type(a))
a=(1,2.5,True,"Ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
print(a[::-1])
# chane value of tuple convert to list
b=list(a)
print(b)
b.append("kavin")
a=tuple(b)
print(a)
for i in a:
    print(i)
if "Ram" in a:
    print("found")
else:
    print("not found")
print(len(a))
a=(1,)
print(type(a))
"""
del a
print(a)  """
a=(1,2,3,2,4,2,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(2))
a=(1,2,3,2,4,2,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][2])
x=("kavin",)*10
print(x)
a=(1,2,7,4)
print(min(a))
print(max(a))
