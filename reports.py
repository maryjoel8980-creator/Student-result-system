"""reports.py - Report card, class report and file export."""
import os
from datetime import datetime

from results import (total_score, average_score, get_grade,
                     sort_students, class_statistics)


def report_card(student):
    lines = [
        "=" * 50,
        "              STUDENT REPORT CARD",
        "=" * 50,
        f"ID      : {student.student_id}",
        f"Name    : {student.name}",
        f"Class   : {student.student_class}",
        f"Gender  : {student.gender}",
        f"DOB     : {student.dob}",
        "-" * 50,
        f"{'Subject':<30}{'Score':>10}",
        "-" * 50,
    ]
    for subject, score in student.scores.items():
        lines.append(f"{subject:<30}{score:>10.1f}")
    avg = average_score(student)
    lines += [
        "-" * 50,
        f"Total   : {total_score(student):.1f}",
        f"Average : {avg:.2f}",
        f"Grade   : {get_grade(avg)}",
        f"Result entered on: {student.date_entered or 'N/A'}",
        "=" * 50,
    ]
    return "\n".join(lines)


def class_report(students, by="average"):
    lines = ["=" * 78, "CLASS RESULT SUMMARY".center(78), "=" * 78,
             f"{'Pos':<5}{'ID':<14}{'Name':<25}{'Total':>9}{'Average':>10}{'Grade':>8}",
             "-" * 78]
    for pos, s in enumerate(sort_students(students, by), start=1):
        avg = average_score(s)
        lines.append(f"{pos:<5}{s.student_id:<14}{s.name:<25}"
                     f"{total_score(s):>9.1f}{avg:>10.2f}{get_grade(avg):>8}")
    stats = class_statistics(students)
    if stats:
        lines += ["-" * 78,
                  f"Highest average : {stats['highest']:.2f} ({stats['highest_name']})",
                  f"Lowest average  : {stats['lowest']:.2f} ({stats['lowest_name']})",
                  f"Class average   : {stats['class_average']:.2f}"]
    lines.append("=" * 78)
    return "\n".join(lines)


def save_report_to_file(text, filename=None):
    """Save report text into reports/ folder and return the path."""
    os.makedirs("reports", exist_ok=True)
    if filename is None:
        filename = datetime.now().strftime("report_%Y%m%d_%H%M%S.txt")
    path = os.path.join("reports", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
