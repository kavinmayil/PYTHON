s= [1,2,3,4,5]
print(s)
print(type(s))
s[0]=100
print(s)
print("slicing")
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])
b=s[::-1]
if b==s:
    print("yse")
else:
    print("no")
print("------------------------------------------------------------------")
a=[1,True,'Ram',2.5]
print(a)
print(type(a))
for i in range(len(a)):
    print(type(a[i]))
print("------------------------------------------------------------------")
a=[1,True,'Ram',[1,2,3]]
print(a)
print(type(a))
for i in range(len(a)):
    print(type(a[i]))
print(a[3][1])

a=[10,20,30,40,50]
print(a)
a.clear()
print(a)
a=[10,20,30,40,50]
b=a.copy()
print(b)
a=[10,20,30,40,50,20,33,20,20]
print(a.count(20))
print(a.index(30))
print(len(a))
print(max(a))
print(min(a))
print(a)
print(a.pop(5))#remove elements using index
print(a)
a=[1,2,3,4,5,6,3,4,5,2,3,1]
a.remove(2)
print(a)
print("---------------------------------------------------")
name=["ram"]
"""
while True:
    line=input()
    if line:
        name.append(line)
    else:
        break
print(name)
"""
name1=["ravi","somu"]
name.extend(name1)
print(name)
print(name[1])
name.insert(1,"surya")
print(name)
print("-----------------------------------------------")
print(list(range(5)))
print(list("kavinmayil"))
a=list(input())
print(a)
print("----------------------------")
a=[1,4,2,5,3]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple","zebra"]
a.sort(key=len)
print(a)
