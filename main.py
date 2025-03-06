class Salary:
    def __init__(self, salary: float, sss: float = None, pagibig: float = None, tax: float = None):
        """
        Initialize Salary object with base salary and optional custom deductions.

        :param salary: Gross monthly salary
        :param sss: SSS contribution (optional, dynamically calculated if None)
        :param pagibig: Pag-IBIG contribution (optional, dynamically calculated if None)
        :param tax: Tax deduction (optional, dynamically calculated if None)
        """
        self.salary = salary
        self.sss = sss if sss is not None else self.calculate_sss()  # Calculate dynamically if None
        self.pagibig = pagibig if pagibig is not None else self.calculate_pagibig()  # Calculate dynamically if None
        self.tax = tax if tax is not None else self.calculate_tax()  # Calculate dynamically if None

    def calculate_philhealth(self) -> float:
        """Calculate PhilHealth deduction based on salary."""
        return round((self.salary * 0.05) / 2, 2)

    def calculate_sss(self) -> float:
        """Dynamically calculate SSS based on salary (example logic)."""
        if self.salary <= 15000:
            return 1200
        else:
            return self.salary * 0.08  # Example dynamic logic

    def calculate_pagibig(self) -> float:
        """Dynamically calculate Pag-IBIG based on salary (example logic)."""
        return min(self.salary * 0.02, 100)  # Example dynamic logic, capped at 100

    def calculate_tax(self) -> float:
        """Dynamically calculate Tax based on salary (example logic)."""
        if self.salary <= 10000:
            return 1000
        elif self.salary <= 30000:
            return 2000
        else:
            return 3000

    def calculate_deductions(self) -> dict:
        """Calculate total deductions (SSS, PhilHealth, Pag-IBIG, Tax)."""
        philhealth = self.calculate_philhealth()
        total_deductions = round(self.sss + philhealth + self.pagibig + self.tax, 2)
        net_salary = round(self.salary - total_deductions, 2)

        return {
            "gross_salary": self.salary,
            "sss": self.sss,
            "philhealth": philhealth,
            "pagibig": self.pagibig,
            "tax": self.tax,
            "total_deductions": total_deductions,
            "net_salary": net_salary,
        }

    def print_salary_details(self):
        """Display salary breakdown with formatted output."""
        details = self.calculate_deductions()

        print("\nSalary Breakdown")
        print("=" * 30)
        for key, value in details.items():
            print(f"{key.replace('_', ' ').title():<20}: ₱{value:,.2f}")


def get_valid_salary_input():
    """Prompt the user for salary and validate input."""
    while True:
        try:
            salary_input = input("Enter your monthly salary: ")
            # Check if input is a valid float
            salary_input = float(salary_input)
           
            # Check if salary is positive
            if salary_input <= 0:
                raise ValueError("Salary must be a positive number.")
           
            return salary_input
        except ValueError as ve:
            print(f"Invalid input. Please enter a valid salary. Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def get_valid_deduction_input(deduction_type: str, default_value: float):
    """Prompt the user for deduction value and validate input."""
    while True:
        try:
            deduction_input = input(f"Enter {deduction_type} contribution (default: ₱{default_value}): ")
            if deduction_input.strip() == "":  # If no input, use the default value
                return default_value
            deduction_input = float(deduction_input)
           
            # Check if deduction is non-negative
            if deduction_input < 0:
                raise ValueError(f"{deduction_type} contribution must be a non-negative number.")
           
            return deduction_input
        except ValueError as ve:
            print(f"Invalid input. Please enter a valid {deduction_type} value. Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def main():
    # Get valid salary input from the user
    salary_input = get_valid_salary_input()
   
    # Ask if the user wants to customize deductions
    choice = input("Do you want to set custom SSS, Pag-IBIG, or Tax values? (yes/no): ").strip().lower()

    if choice == "yes":
        sss = get_valid_deduction_input("SSS", 1200)
        pagibig = get_valid_deduction_input("Pag-IBIG", 100)
        tax = get_valid_deduction_input("Tax", 1875)
        salary = Salary(salary_input, sss, pagibig, tax)
    else:
        salary = Salary(salary_input)

    # Print the salary details using the OOP structure
    salary.print_salary_details()


if __name__ == "__main__":
    main()
