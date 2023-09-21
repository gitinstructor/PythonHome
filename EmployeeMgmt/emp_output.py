# emp_output.py

def output(employee): 
    print("        <<급여 관리 프로그램>>")
    print("-----------------------------------------------------------")
    print("사번\t급수\t호\t수당\t지급액\t세금\t차인지급액")
    print("-----------------------------------------------------------")
    print(f"{employee['emp_num']}\t{employee['emp_level']}", end='\t')
    print(f"{employee['emp_ho']}\t{employee['emp_bonus']:,}", end='\t')
    print(f"{employee['emp_money']:,}\t{employee['emp_tax']}", end='\t')
    print(f"{employee['emp_total']:,}")