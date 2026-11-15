"""results.py - Score calculation and grading logic."""

MIN_SUBJECTS = 5


def total_score(student):
    return sum(student.scores.values())


def average_score(student):
    if not student.scores:
        return 0.0
    return total_score(student) / len(student.scores)


def get_grade(average):
    """Assign a grade from the average score."""
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    return "F"


def has_enough_subjects(student):
    return len(student.scores) >= MIN_SUBJECTS


def sort_students(students, by="average"):
    """Sort by average (highest first) or by name (A-Z)."""
    if by == "name":
        return sorted(students, key=lambda s: s.name.lower())
    return sorted(students, key=average_score, reverse=True)


def class_statistics(students):
    """Return highest, lowest and class average of student averages."""
    graded = [s for s in students if s.scores]
    if not graded:
        return None
    averages = [average_score(s) for s in graded]
    best = max(graded, key=average_score)
    worst = min(graded, key=average_score)
    return {
        "highest": max(averages), "highest_name": best.name,
        "lowest": min(averages), "lowest_name": worst.name,
        "class_average": sum(averages) / len(averages),
        "count": len(graded),
    }
