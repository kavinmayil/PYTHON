#set
# collection of unorder and unindex datatype  // add or remove cannot change value
names={'ram','sam','ravi'}
print(names)
print(type(names))

for name in names:
    print(name)
    #adding new element
names.add('sara')
print(names)
#Update Another set of data
a={'mare','sami','gaiga'}
names.update(a)
print(names)
#remove function
#names.remove('sam')
names.discard('saujhbra')
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names
#print(names)
names={'ram','ram','sam','ravi','mare','sami','gaiga'}  #remove duplicate in set
print(names)
a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

#symentric difference
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)
