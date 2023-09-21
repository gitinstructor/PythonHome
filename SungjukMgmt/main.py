#main.py
import student_input
import student_calc
import student_output

print("Program is Start...")
student = {}
student_input.myinput(student) # Call by Reference
student_calc.calc(student)
student_output.output(student)
print("Program is Over...")
