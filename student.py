"""student.py - Student class and validation helpers.

Author : Joel Mary Ayomikun
Matric : 24/SCI01/104
"""
import re
from datetime import datetime

# Regex: e.g. 24/SCI01/104 or STU001 style IDs
ID_PATTERN = re.compile(r"^[A-Za-z0-9/_-]{3,20}$")
DATE_FORMAT = "%Y-%m-%d"


def is_valid_id(student_id):
    """Return True if the student ID matches the allowed pattern."""
    return bool(ID_PATTERN.match(student_id))


def is_valid_date(text):
    """Return True if text is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(text, DATE_FORMAT)
        return True
    except ValueError:
        return False


class Student:
    """Represents one student and their subject scores."""

    def __init__(self, student_id, name, student_class, gender, dob,
                 scores=None, date_entered=None):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores is not None else {}  # {subject: score}
        self.date_entered = date_entered  # when results were last entered

    def set_score(self, subject, score):
        """Add or update a subject score and record the date."""
        self.scores[subject] = float(score)
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "student_class": self.student_class,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_entered": self.date_entered,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["student_id"], d["name"], d["student_class"],
                   d["gender"], d["dob"], d.get("scores", {}),
                   d.get("date_entered"))

    def __str__(self):
        return (f"{self.student_id:<14}{self.name:<25}"
                f"{self.student_class:<10}{self.gender:<8}{self.dob}")
