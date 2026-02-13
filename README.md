# MyGitProject – Calculator with Input Validation

## Project Description
This project implements a command-line calculator with strong input validation.
The program evaluates mathematical expressions entered by the user in the format:

    number operator number

Example:
    5 + 3
    10 / 2

The calculator supports the following operators:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
**  Exponentiation

The program continues running until the user types "quit".

---

## Problem Definition
Users often enter incorrect or malformed mathematical expressions. 
The goal of this project is to safely process user input and prevent runtime errors.

The program ensures:
- The input contains exactly two operands and one operator.
- Both operands are valid numeric values.
- Only supported operators are allowed.
- Division by zero is prevented.
- Invalid input produces an informative error message instead of crashing.

---

## How to Run the Program

Open terminal inside the project folder and run:

    python3 main.py

Then enter expressions like:

    5 + 3
    10 / 2

Type:

    quit

to exit the program.

---

## Repository Structure

main.py  
Handles the CLI loop and overall program flow.  
Calls validation and calculation functions.

validator.py  
Validates user input format, checks operator validity, ensures numeric operands, and prevents division by zero.

operations.py  
Performs the actual calculation based on the provided operator.

---

## Version Control Workflow

This project demonstrates collaborative version control practices using Git and GitHub:

- Created separate feature branches:
  - feature-main-cli
  - feature-validation
- Made multiple incremental commits.
- Created pull requests for each feature branch.
- Merged changes into the main branch.
- Maintained structured development workflow.

---

## Contribution

Ashvin Shiyani:
- Created GitHub repository.
- Implemented main CLI loop in main.py.
- Implemented input validation in validator.py.
- Implemented calculation logic in operations.py.
- Managed branching, commits, pull requests, and merges.

Due to inability to secure a group member before the deadline and pending instructor response, this project was completed individually while still demonstrating full Git workflow and version control practices.# MyGitProject
This is the repo for my assignment comp1243
