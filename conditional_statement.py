#if condition
 
#   if condition:
         #code Block
         
age=15
if age>=18:
    print("ELigible")    
    
    #if-else condition
 
#   if condition:
         #code Block
#   else:
         #code block
         
age=15
if age>=18:
    print("ELigible")    
else:
    print("Not eligible")
              
              #if-elif-else condition
 
#   if condition:
         #code Block
         
#   elif condition:
         #code block        
#   else:
         #code block
         
mark=85
if mark>=90:
    print("A+")    
elif mark>=80:
    print("A")
elif mark>=70:
    print("B+")
elif mark>=60:
    print("B")
else:
    print("Fail")
    
    #Nested if condition
    
#age=int(input("Enter age : "))
citizen=True
if age>=18:
    if citizen:
        print("Eligible to vote")
    else:
        print("not a citizen")
else:
    print("not Eligible to vote")
    
    #Short Hand if condition
    
a=10
b=5
if a>b: print("a is greater")
