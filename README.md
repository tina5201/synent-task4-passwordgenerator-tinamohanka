# 🔐 Password Generator

**Synent Technologies – Python Development Internship**
**Task 4 – Basic Level**

---

## 📌 Description

A command-line password generator that creates strong, secure passwords using Python's `secrets` module. Users can customize the password length and character types, and optionally save generated passwords to a log file.

---

## ✨ Features

- Generate cryptographically secure passwords using `secrets` module
- Choose password length (8–64 characters)
- Select character types: Uppercase, Lowercase, Numbers, Special Symbols
- Password strength indicator (Weak / Medium / Strong / Very Strong)
- Save passwords to a timestamped log file (`password_log.txt`)
- Input validation and error handling
- Generate multiple passwords in one session

---

## 🛠️ Tech Stack

- Python 3.x
- Built-in modules: `secrets`, `string`, `datetime`, `os`

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/synent-task4-passwordgenerator-yourname.git
   ```
3. Navigate to the folder:
   ```
   cd synent-task4-passwordgenerator-yourname
   ```
4. Run the script:
   ```
   python password_generator.py
   ```

---

## 📸 Sample Output

```
==================================================
   🔐 Secure Password Generator
   Synent Technologies Internship
==================================================

--- Settings ---
Enter password length (8-64): 16
Include Uppercase letters? (A-Z) (y/n): y
Include Lowercase letters? (a-z) (y/n): y
Include Numbers?          (0-9) (y/n): y
Include Special Symbols?  (!@#...) (y/n): y

==================================================
  Generated Password : tR#8mK@2xQpL!v5N
  Strength           : 🔵 Very Strong
==================================================
```

---

## 👤 Author

Tina Kumari Mohanka
Python Development Intern – Synent Technologies
