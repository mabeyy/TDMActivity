class Salary:
    def __init__(self, salary):
        self.salary = salary
        self.sss = self.calculate_sss()  # Calculate dynamically based on salary
        self.pagibig = self.calculate_pagibig()  # Calculate dynamically based on salary
        self.tax = self.calculate_tax()  # Calculate dynamically based on salary

    def calculate_philhealth(self):
        """Calculate PhilHealth deduction based on salary."""
        return (self.salary * 0.05) / 2

    def calculate_sss(self):
        """Dynamically calculate SSS based on salary (example logic)."""
        if self.salary <= 15000:
            return 1200
        else:
            return self.salary * 0.08  # Example dynamic logic

    def calculate_pagibig(self):
        """Dynamically calculate Pag-IBIG based on salary (example logic)."""
        return min(self.salary * 0.02, 100)  # Example dynamic logic, capped at 100

    def calculate_tax(self):
        """Dynamically calculate Tax based on salary (example logic)."""
        if self.salary <= 10000:
            return 1000
        elif self.salary <= 30000:
            return 2000
        else:
            return 3000

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
    