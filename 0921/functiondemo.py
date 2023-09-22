#Call by Reference, mutable type
def change(target):
    target[0] = 10000
    print(f"In the change target = {target}")

original = [1,2,3]
print(f"Before change original = {original}")
change(original)
print(f"After change original = {original}")