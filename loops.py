#loops 
# 1.while loops
# while condition:
    # code block
    
i=1
while i<=5:
    print(i)
    i+=1
print("----------------------")

#2.for loop
# for variable in sequence:
    #code block
    
for i in range(1,6):
    print(i)
# range(n)  0 to n-1
# range(a,b)  a to b-1
# range(a,b,s) a to b-1,step size s
print("------------------ ----")
for i in range(2,10,2):
    print(i)
print("-----------------------")

#iterative over string
for ch in "Kavin":
    print(ch)
print("-----------------------")
#iterative over list
fruit=["apple","mango","cherry"]
for ch in fruit:
    print(ch)
print("-----------------------")  
#Nested Loop
for i in range(1,4):
    for j in range(1,4):
        print(1,"*",j,"=",i*j)
    print("---------------")
    
#Loop with else
for i in range(3):
    print(i)
else:
    print("Loop ended normaly")
