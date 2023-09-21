#emp_calc.py

def getSalary(level, ho) : 
    #급, 호별 급여 반환하는 함수
    salary = None
    if level == 1 :
        if ho == 1 : salary = 95000
        elif ho == 2 : salary = 92000
        elif ho == 3 : salary = 89000
        elif ho == 4 : salary = 86000
        elif ho == 5 : salary = 83000
    elif level == 2 : 
        if ho == 1 : salary = 8000
        elif ho == 2 : salary = 75000
        elif ho == 3 : salary = 70000
        elif ho == 4 : salary = 65000
        elif ho == 5 : salary = 60000
    return salary
        
def getTaxAndJojung(money):
    #지급액별 세율및 조정액을 반환하는 함수
    if money < 70000 : return (0, 0)
    elif 70000 <= money < 80000 : return (0.005, 300) 
    elif 80000 <= money < 90000 : return (0.007, 500)
    else : return (0.012, 1000)
    
def calc(employee) : 
    salary = getSalary(employee["emp_level"], employee["emp_ho"]) #급여
    money = salary + employee["emp_bonus"]  #지급액
    tax_rate, jojung = getTaxAndJojung(money)  #세율과 조정액 
    tax = int((money * tax_rate) - jojung)    #세금
    total = int(money - tax) #차인지급액
    employee["emp_money"] = money 
    employee["emp_tax"] = tax
    employee["emp_total"] = total 
    
    