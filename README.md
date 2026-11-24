# Employee Salary Calculator

**PS No.:** 93  
**Course:** B.Tech Computer Science and Engineering (IBM)  
**Semester:** First Semester  
**Language:** Python 3

## Project overview

The Employee Salary Calculator is a console-based Python program. It accepts an employee's name, employee ID and basic salary, calculates allowances and deductions, and prints a salary slip. It can process multiple employees in one run.

## Salary calculation rules

| Component | Calculation |
|---|---:|
| HRA | 20% of basic salary |
| DA | 10% of basic salary |
| Gross salary | Basic salary + HRA + DA |
| PF | 12% of basic salary |
| Tax | Based on gross salary slab |
| Net salary | Gross salary - PF - Tax |

### Tax slabs

| Gross salary | Tax rate |
|---|---:|
| Up to Rs. 25,000 | 0% |
| Rs. 25,001 to Rs. 50,000 | 5% |
| Above Rs. 50,000 | 10% |


## Requirements

- Python 3
- No external Python packages are required.

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python salary_calculator.py
```

On some systems, use:

```bash
python3 salary_calculator.py
```

4. Enter the employee name, ID and a positive basic salary.
5. Choose `y` to calculate another employee's salary, or `n` to exit.

## Program features

- Uses functions: `calculate_gross()`, `calculate_deductions()` and `print_slip()`.
- Uses operators and conditional statements.
- Validates non-numeric, zero and negative salary input.
- Prints a formatted salary slip.
- Uses a loop to process multiple employees.

## Assignment test cases

| Test case | Basic salary | HRA | DA | Gross | PF | Tax | Net salary |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1. Normal input | Rs. 30,000 | Rs. 6,000 | Rs. 3,000 | Rs. 39,000 | Rs. 3,600 | Rs. 1,950 | Rs. 33,450 |
| 2. Minimum/boundary input | Rs. 10,000 | Rs. 2,000 | Rs. 1,000 | Rs. 13,000 | Rs. 1,200 | Rs. 0 | Rs. 11,800 |
| 3. Invalid input | -Rs. 5,000 / `abc` | — | — | — | — | — | Invalid salary message |
| 4. Different valid scenario | Rs. 50,000 | Rs. 10,000 | Rs. 5,000 | Rs. 65,000 | Rs. 6,000 | Rs. 6,500 | Rs. 52,500 |

## Repository contents

- `salary_calculator.py` — Python source code.
- `README.md` — project description and run instructions.
- `PROJECT_REPORT.md` — concise project report.
- `sample_output.txt` — example console output.
- `.gitignore` — ignores common temporary files.

## Author

Bishnu kumar_RU-26-03536_1-O
