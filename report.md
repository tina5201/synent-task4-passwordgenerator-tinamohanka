# Project Report - Password Generator

**Internship:** Synent Technologies - Python Development  
**Task:** Task 4 - Basic Level  
**Author:** Tina Kumari Mohanka
**Date:** June 2026  

---

## Objective

To build a secure command-line password generator that creates strong passwords based on user preferences, with a strength indicator and file logging feature.

---

## Tools Used

- Python 3
- `secrets` module - cryptographically secure random generation
- `string` module - character sets
- `datetime` module - timestamp for log file
- VS Code - code editor
- GitHub - version control

---

## Steps Performed

1. Took user input for password length (8-64 characters)
2. Allowed user to choose character types - uppercase, lowercase, numbers, symbols
3. Used `secrets.choice()` to generate a secure password
4. Ensured at least one character from each selected type is included
5. Built a strength checker based on character variety and length
6. Added option to save generated password to `password_log.txt` with timestamp
7. Added input validation for all user inputs
8. Tested all edge cases - invalid input, only one character type selected, etc.

---

## Output

- Strong, secure passwords generated successfully based on user choice
- Strength indicator displayed - Weak / Medium / Strong / Very Strong
- Passwords saved to `password_log.txt` with date and time

---

## What I Learned

- Difference between `secrets` and `random` module - `secrets` is cryptographically secure
- How to validate user inputs properly in CLI applications
- File handling in Python - appending data with timestamps
- How to build a clean menu-driven CLI program
