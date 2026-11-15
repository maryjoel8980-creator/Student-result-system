"""
Student Result Management System
--------------------------------
Name       : Joel Mary Ayomikun
Matric No. : 24/SCI01/104
Department : Computer Science
GitHub     : maryjoel8980
Course     : Introduction to Python Programming (New Horizon)

Run with:  python main.py
"""
from student import Student, is_valid_id, is_valid_date
from results import has_enough_subjects, MIN_SUBJECTS
from storage import load_students, save_students
from reports import report_card, class_report, save_report_to_file

students = []


def find_by_id(student_id):
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def ask_score(subject):
    """Keep asking until a valid score between 0 and 100 is entered."""
    while True:
        try:
            score = float(input(f"  Score for {subject} (0-100): "))
        except ValueError:
            print("  Please enter a number.")
            continue
        if 0 <= score <= 100:
            return score
        print("  Score must be between 0 and 100.")


def add_student():
    sid = input("Student ID: ").strip()
    if not is_valid_id(sid):
        print("Invalid ID (3-20 letters, digits, / _ -).")
        return
    if find_by_id(sid):
        print("A student with that ID already exists.")
        return
    name = input("Full name: ").strip()
    cls = input("Class/Form: ").strip()
    gender = input("Gender (M/F): ").strip().upper()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    if not name or not cls or gender not in ("M", "F") or not is_valid_date(dob):
        print("Invalid details. Student not added.")
        return
    students.append(Student(sid, name, cls, gender, dob))
    save_students(students)
    print("Student added.")


def view_students():
    if not students:
        print("No students registered yet.")
        return
    print(f"{'ID':<14}{'Name':<25}{'Class':<10}{'Gender':<8}DOB")
    print("-" * 65)
    for s in students:
        print(s)


def search_student():
    term = input("Enter ID or name to search: ").strip().lower()
    found = [s for s in students
             if term == s.student_id.lower() or term in s.name.lower()]
    if not found:
        print("No match found.")
    for s in found:
        print(s)


def update_student():
    s = find_by_id(input("Student ID to update: ").strip())
    if not s:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    s.name = input(f"Name [{s.name}]: ").strip() or s.name
    s.student_class = input(f"Class [{s.student_class}]: ").strip() or s.student_class
    gender = input(f"Gender [{s.gender}]: ").strip().upper()
    if gender in ("M", "F"):
        s.gender = gender
    dob = input(f"DOB [{s.dob}]: ").strip()
    if dob and is_valid_date(dob):
        s.dob = dob
    save_students(students)
    print("Student updated.")


def delete_student():
    s = find_by_id(input("Student ID to delete: ").strip())
    if not s:
        print("Student not found.")
        return
    if input(f"Delete {s.name}? (y/n): ").lower() == "y":
        students.remove(s)
        save_students(students)
        print("Student deleted.")


def record_scores():
    s = find_by_id(input("Student ID: ").strip())
    if not s:
        print("Student not found.")
        return
    print(f"Enter at least {MIN_SUBJECTS} subjects for {s.name}.")
    count = 0
    while True:
        subject = input("Subject name (blank to finish): ").strip().title()
        if not subject:
            if count < MIN_SUBJECTS and not has_enough_subjects(s):
                print(f"You must record at least {MIN_SUBJECTS} subjects.")
                continue
            break
        s.set_score(subject, ask_score(subject))
        count += 1
    save_students(students)
    print("Scores saved.")


def update_score():
    s = find_by_id(input("Student ID: ").strip())
    if not s:
        print("Student not found.")
        return
    if not s.scores:
        print("This student has no scores yet.")
        return
    print("Subjects:", ", ".join(s.scores))
    subject = input("Subject to update: ").strip().title()
    if subject not in s.scores:
        print("Subject not found.")
        return
    s.set_score(subject, ask_score(subject))
    save_students(students)
    print("Score updated.")


def show_report_card():
    s = find_by_id(input("Student ID: ").strip())
    if not s:
        print("Student not found.")
    elif not s.scores:
        print("No scores recorded for this student.")
    else:
        print(report_card(s))


def show_class_report():
    graded = [s for s in students if s.scores]
    if not graded:
        print("No results available yet.")
        return
    choice = input("Sort by (1) average or (2) name? ").strip()
    by = "name" if choice == "2" else "average"
    text = class_report(graded, by)
    print(text)
    if input("Save this report to a file? (y/n): ").lower() == "y":
        print("Saved to", save_report_to_file(text))


MENU = """
===== STUDENT RESULT MANAGEMENT SYSTEM =====
 1. Add student            6. Record scores
 2. View all students      7. Update a score
 3. Search student         8. Show report card
 4. Update student         9. Class report / statistics
 5. Delete student         0. Exit
"""

ACTIONS = {
    "1": add_student, "2": view_students, "3": search_student,
    "4": update_student, "5": delete_student, "6": record_scores,
    "7": update_score, "8": show_report_card, "9": show_class_report,
}


def main():
    global students
    students = load_students()
    print(f"Loaded {len(students)} student(s).")
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            try:
                action()
            except KeyboardInterrupt:
                print("\nCancelled.")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
