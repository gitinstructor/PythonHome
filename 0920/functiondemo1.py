def calc_sum(start, end) :   #Parameter, 매개변수
    sum = 0
    for i in range(start, end + 1) :
        sum += i

    return sum
#함수의 끝    

start = 50  
end = 70  
result =  calc_sum(start, end)    #인자, 인수, Argument, Call by Value
print("%d부터 %d까지의 합은 %d입니다" % (start, end, result))