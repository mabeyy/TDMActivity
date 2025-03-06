 # Made the parameters changeable but have default values - Yugo
def compute_deductions(salary, sss = 1200, pagibig = 100, tax = 1875):

    philhealth = (salary * 0.05) / 2

    total_deductions = sss + philhealth + pagibig + tax
    # Changed variable name deductions to total_deductions for better understanding - Yugo
    net_salary = salary - total_deductions

    return{
        "gross_salary": salary,
        "sss": sss,
        "philhealth": philhealth,
        "pagibig": pagibig,
        "tax": tax,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }

# Added display_salary_details function to print out results uniformly - Yugo
def display_salary_details(salary_info):
    print("\nSalary Breakdown")
    print("=" * 30)
    print(f"Gross Salary      : {salary_info['gross_salary']:.2f}")
    print(f"SSS Deduction     : {salary_info['sss']:.2f}")
    print(f"PhilHealth Deduction: {salary_info['philhealth']:.2f}")
    print(f"Pag-IBIG Deduction: {salary_info['pagibig']:.2f}")
    print(f"Tax Deduction     : {salary_info['tax']:.2f}")
    print(f"Total Deductions  : {salary_info['total_deductions']:.2f}")
    print(f"Net Salary        : {salary_info['net_salary']:.2f}")
    # Used f strings to improve readability - Yugo

salary = float(input("Enter your monthly salary: "))
# You can change the values of sss, pagibig, and tax here - Yugo
salary_details = compute_deductions(salary)
display_salary_details(salary_details)