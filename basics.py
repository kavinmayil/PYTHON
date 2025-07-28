"""
name=input("Enter your name: ")
print(type(name))
print(name)

a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
c=a+b
print(c)
print(type(a))

a=float(input("Enter value of A:"))
b=float(input("Enter value of B:"))
c=a+b
print(c)
print(type(a))


name1,name2,name3=input("Enter 3 name :").split()
print(name1)
print(name2)
print(name3)
"""
name1,name2,name3=input("Enter 3 name :").split(',')
print(name1)
print(name2)
print(name3)
