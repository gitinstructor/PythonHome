first = int(input("Enter a first Number : "))
second = int(input("Enter a second Number : "))

try : 
    print(f"{first} / {second} = {first / second}")
except Exception as err: 
    print(err)
finally : 
    print("Program is Over..")
# else : 
#     print("Program is Over")
fopen()