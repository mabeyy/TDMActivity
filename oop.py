class Salary:
    def __init__(self, salary):
        self.salary = salary
        self.sss = 1200
        self.pagibig = 100
        self.tax = 1875

    def calculate_philhealth(self):
        """Calculate PhilHealth deduction based on salary."""
        return (self.salary * 0.05) / 2

    def calculate_deductions(self):
        """Calculate total deductions (SSS, PhilHealth, Pag-IBIG, Tax)."""
        philhealth = self.calculate_philhealth()
        deductions = self.sss + philhealth + self.pagibig + self.tax
        net_salary = self.salary - deductions
        return philhealth, deductions, net_salary

    def print_salary_details(self):
        """Print all salary-related details."""
        philhealth, deductions, net_salary = self.calculate_deductions()

        print("Gross Salary:", self.salary)
        print("SSS Deduction:", self.sss)
        print("PhilHealth Deduction:", philhealth)
        print("Pag-IBIG Deduction:", self.pagibig)
        print("Tax Deduction:", self.tax)
        print("Total Deductions:", deductions)
        print("Net Salary:", net_salary)


def main():
    # Get the user's monthly salary input
    salary_input = float(input("Enter your monthly salary: "))
    salary = Salary(salary_input)
    
    # Print the salary details using the OOP structure
    salary.print_salary_details()


if __name__ == "__main__":
    main()
