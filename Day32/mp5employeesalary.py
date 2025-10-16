# Mini Project 2: Employee Salary Calculator
# AI POWERED PYTHON DJANGO MYSQL LEARNING MATERIAL

# Taking employee details as input
emp_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter total allowances: "))

# Tax deduction rate (in percentage)
tax_rate = 10  # 10% tax

# Calculating deductions and final salary
tax_deduction = (basic_salary + allowances) * (tax_rate / 100)
net_salary = (basic_salary + allowances) - tax_deduction

# Displaying data types for learning
print(f"\nType of emp_name: {type(emp_name)}")
print(f"Type of basic_salary: {type(basic_salary)}")
print(f"Type of allowances: {type(allowances)}")
print(f"Type of net_salary: {type(net_salary)}")

# Displaying formatted salary slip
print("\n========== EMPLOYEE SALARY SLIP ==========")
print(f"Employee Name : {emp_name}")
print("------------------------------------------")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"Allowances    : ₹{allowances:.2f}")
print(f"Tax Deduction : ₹{tax_deduction:.2f}  ({tax_rate}%)")
print("------------------------------------------")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("==========================================")
print("Thank you for using the Employee Payroll System!")
