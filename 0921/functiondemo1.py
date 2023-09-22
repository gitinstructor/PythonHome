student = {}

def myinput(man) : 
    name = input("Enter your Name : ")
    age = input("Enter your Age : ") 
    man["name"] = name 
    man["age"] = age

myinput(student)
print(student)
