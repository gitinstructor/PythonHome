# 1,2,3,4,5
#list_ = [1,2,3,4,5]
count = 0
for num in range(1, 101):
    if num % 7 == 0 :
        print(num, end = '\t')
        count += 1
        if count % 5 == 0 : 
            print()
print() 