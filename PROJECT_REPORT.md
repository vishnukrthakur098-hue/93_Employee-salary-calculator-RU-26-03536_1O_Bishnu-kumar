# Project Report: Employee Salary Calculator

## 1. Introduction
The Employee Salary Calculator is a Python 3 console application developed for PS No. 93. It calculates an employee's gross salary, deductions and net salary, then displays the result as a salary slip.

## 2. Problem statement
Create a program that calculates an employee's net salary from basic pay, allowances (HRA and DA) and deductions (PF and tax).

## 3. Objectives
- Accept employee name, employee ID and basic salary.
- Calculate HRA, DA, gross salary, PF, tax and net salary.
- Use functions, operators, conditions and loops.
- Validate salary input and print a clear salary slip.
- Allow salary calculation for more than one employee.

## 4. Calculation logic
- HRA = 20% of basic salary.
- DA = 10% of basic salary.
- Gross salary = Basic salary + HRA + DA.
- PF = 12% of basic salary.
- Tax on gross salary: up to Rs. 25,000 = 0%; Rs. 25,001–Rs. 50,000 = 5%; above Rs. 50,000 = 10%.
- Net salary = Gross salary - PF - Tax.

The tax percentage is applied to the full gross salary in the selected slab, as indicated by the assignment's expected outputs.

## 5. Functions used
- `calculate_gross(basic_salary)`: calculates HRA, DA and gross salary.
- `calculate_deductions(gross, basic_salary)`: calculates PF and tax.
- `print_slip(name, employee_id, basic_salary)`: displays the salary slip.
- `get_positive_salary()`: checks that the entered salary is numeric and positive.
- `main()`: controls input and the multiple-employee loop.

## 6. Test cases and expected results

| Case | Input | Expected result |
|---|---|---|
| 1 | Basic salary Rs. 30,000 | HRA 6,000; DA 3,000; Gross 39,000; PF 3,600; Tax 1,950; Net 33,450 |
| 2 | Basic salary Rs. 10,000 | HRA 2,000; DA 1,000; Gross 13,000; PF 1,200; Tax 0; Net 11,800 |
| 3 | Basic salary -5,000 or `abc` | `Invalid salary. Enter a positive number.` |
| 4 | Basic salary Rs. 50,000 | HRA 10,000; DA 5,000; Gross 65,000; PF 6,000; Tax 6,500; Net 52,500 |

## 7. How to execute
Run `python salary_calculator.py` in a terminal using Python 3. Enter the requested employee details and follow the prompt to continue or exit.

## 8. Conclusion
The project demonstrates the use of Python functions, arithmetic operators, conditional statements, input validation and loops to solve a basic salary calculation problem.

## 9. Student details
- Student name: ____________________
- Student ID: ____________________
- Course/section: ____________________
- Submission date: ____________________
