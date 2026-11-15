# Student Result Management System

A menu-driven Python application for managing student records and results.

- **Name:** Joel Mary Ayomikun
- **Matric No.:** 24/SCI01/104
- **Department:** Computer Science
- **GitHub:** [maryjoel8980](https://github.com/maryjoel8980)

## Features
- Add, view, search, update and delete students
- Record at least 5 subject scores, with totals, averages and grades (A-F)
- Report cards and class report (sorted by average or name)
- Class statistics (highest, lowest, class average)
- Save reports to a text file (`reports/` folder)
- Data saved in `data/students.json` and loaded on start

## How to run
1. Install Python 3.8+
2. Open the project folder in VS Code
3. In the terminal run: `python main.py`

## Files
| File | Purpose |
|------|---------|
| main.py | Entry point and menu |
| student.py | `Student` class, validation (regex, dates) |
| results.py | Totals, averages, grading, sorting, statistics |
| storage.py | JSON load/save |
| reports.py | Report card and class report |

## Grading
A: 70+ | B: 60-69 | C: 50-59 | D: 45-49 | F: below 45
