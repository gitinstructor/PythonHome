def change(target) : 
    target = 100
    print("In the change : target = %d" % target)

original = 5
print("Before Call change : original = %d" % original)
change(original)
print("After Call change : original = %d" % original)