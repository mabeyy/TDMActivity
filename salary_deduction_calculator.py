class Salary:
    def __init__(self, salary: float, sss: float = 1200, pagibig: float = 100, tax: float = 1875):
        """
        Initialize Salary object with base salary and default deductions.

        :param salary: Gross monthly salary
        :param sss: SSS contribution (default: 1200)
        :param pagibig: Pag-IBIG contribution (default: 100)
        :param tax: Tax deduction (default: 1875)
        """
        self.salary = salary
        self.sss = sss
        self.pagibig = pagibig
        self.tax = tax

    def calculate_philhealth(self) -> float:
        """Calculate PhilHealth deduction based on salary."""
        return round((self.salary * 0.05) / 2, 2)

    def calculate_deductions(self) -> dict:
        """Compute all deductions and return a dictionary of results."""
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


def main():
    # Get the user's monthly salary input
    salary_input = float(input("Enter your monthly salary: "))

    # Ask if the user wants to customize deductions
    choice = input("Do you want to set custom SSS, Pag-IBIG, or Tax values? (yes/no): ").strip().lower()

    if choice == "yes":
        sss = float(input("Enter SSS contribution: "))
        pagibig = float(input("Enter Pag-IBIG contribution: "))
        tax = float(input("Enter Tax deduction: "))
        salary = Salary(salary_input, sss, pagibig, tax)
    else:
        salary = Salary(salary_input)

    # Print the salary details using the OOP structure
    salary.print_salary_details()


if __name__ == "__main__":
    main()
