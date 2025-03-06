def calculate_sss():
    return 1200

def calculate_philhealth(salary):
    return (salary * 0.05) / 2

def calculate_pagibig():
    return 100

def calculate_tax():
    return 1875

def calculate_deductions(salary):
    sss = calculate_sss()
    philhealth = calculate_philhealth(salary)
    pagibig = calculate_pagibig()
    tax = calculate_tax()

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary

def print_salary_details(salary, sss, philhealth, pagibig, tax, deductions, net_salary):
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

def main():
    salary = float(input("Enter your monthly salary: "))
    sss, philhealth, pagibig, tax, deductions, net_salary = calculate_deductions(salary)
    print_salary_details(salary, sss, philhealth, pagibig, tax, deductions, net_salary)

if __name__ == "__main__":
    main()
