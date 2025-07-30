def welcome():
   print("Wellcome") 
   
welcome()

def sub(a,b):
   print(a-b)
sub(10,5)

def mul():
   return(5*10)
print(mul())

def div(a,b):
   return a/b
print(div(10,2))

def class_10(*name):
   print(name)
class_10("Alice", "Bob", "Charlie")

def day(name,age):
   print(name," age is ",age)
   
day("kavin",20)
day(78,"baby")
day(age=22,name="baby")

def day(**book):
   print(book)
   
day(title="Python Basics", author="John Doe", year=2023)

def user(name,city="salem"):
   print(name,"from ",city)
   
user("kavin")
user("kavin","tirupur")

def stu(mark):
   return sum(mark)
print(stu([1,2,3,4,5]))

def factorial(x):
   if x==1:
      return 1
   else:
      return x*factorial(x-1)
print(factorial(5))

c=lambda a:a+50
print(c(5))
