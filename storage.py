"""storage.py - Load and save data to a JSON file."""
import json
import os

from student import Student

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "students.json")


def load_students():
    """Load students from JSON. Returns [] if file is missing or corrupt."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: data file is corrupted. Starting with an empty list.")
        return []
    else:
        return [Student.from_dict(d) for d in raw]


def save_students(students):
    """Save all students to JSON, creating the data folder if needed."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in students], f, indent=4)
    except OSError as err:
        print(f"Error saving data: {err}")
        return False
    return True
