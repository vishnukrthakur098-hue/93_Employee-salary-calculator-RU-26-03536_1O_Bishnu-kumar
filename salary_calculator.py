"""
Employee Salary Calculator
PS No.: 93
Language: Python 3

Tax rule from the assignment:
- Gross salary up to Rs. 25,000: 0% tax
- Gross salary from Rs. 25,001 to Rs. 50,000: 5% tax
- Gross salary above Rs. 50,000: 10% tax

"""

def calculate_gross(basic_salary):
    """Calculate gross salary using HRA (20%) and DA (10%)."""
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross = basic_salary + hra + da
    return hra, da, gross


def calculate_deductions(gross, basic_salary):
    """Calculate PF and tax deductions."""
    pf = basic_salary * 0.12

    if gross <= 25000:
        tax_rate = 0
    elif gross <= 50000:
        tax_rate = 0.05
    else:
        tax_rate = 0.10

    tax = gross * tax_rate
    return pf, tax


def print_slip(name, employee_id, basic_salary):
    """Calculate and print one employee's salary slip."""
    hra, da, gross = calculate_gross(basic_salary)
    pf, tax = calculate_deductions(gross, basic_salary)
    net_salary = gross - pf - tax

    print("\n" + "=" * 44)
    print("             EMPLOYEE SALARY SLIP")
    print("=" * 44)
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")
    print("-" * 44)
    print(f"Basic Salary  : Rs. {basic_salary:,.2f}")
    print(f"HRA (20%)     : Rs. {hra:,.2f}")
    print(f"DA (10%)      : Rs. {da:,.2f}")
    print(f"Gross Salary  : Rs. {gross:,.2f}")
    print("-" * 44)
    print(f"PF (12%)      : Rs. {pf:,.2f}")
    print(f"Tax           : Rs. {tax:,.2f}")
    print("-" * 44)
    print(f"NET SALARY    : Rs. {net_salary:,.2f}")
    print("=" * 44)


def get_positive_salary():
    """Read and validate a positive numeric basic salary."""
    while True:
        salary_text = input("Enter basic salary (Rs.): ").strip()
        try:
            salary = float(salary_text)
            if salary <= 0:
                print("Invalid salary. Enter a positive number.")
                return None
            return salary
        except ValueError:
            print("Invalid salary. Enter a positive number.")
            return None


def main():
    print("=" * 44)
    print("       EMPLOYEE SALARY CALCULATOR")
    print("=" * 44)

    while True:
        name = input("\nEnter employee name: ").strip()
        employee_id = input("Enter employee ID: ").strip()

        if not name or not employee_id:
            print("Name and employee ID cannot be empty.")
            continue

        basic_salary = get_positive_salary()
        if basic_salary is not None:
            print_slip(name, employee_id, basic_salary)

        again = input("\nCalculate salary for another employee? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThank you for using Employee Salary Calculator.")
            break


if __name__ == "__main__":
    main()
