
import json
import logging
from dataclasses import asdict

from school.student import Student

logging.basicConfig(level=logging.INFO)


class SchoolManager:

    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        if any(s.roll_no == student.roll_no for s in self.students):
            raise ValueError("Roll number already exists")

        self.students.append(student)

    def find_student(self, roll_no: int) -> Student:
        for student in self.students:
            if student.roll_no == roll_no:
                return student

        raise ValueError("Student not found")

    def add_marks(self, roll_no: int, marks: list[int]) -> None:
        if not marks or any(m < 0 or m > 100 for m in marks):
            raise ValueError("Marks must be between 0 and 100")

        student = self.find_student(roll_no)
        student.marks.extend(marks)

    def ranking(self) -> list[Student]:
        return sorted(
            self.students,
            key=lambda s: s.average(),
            reverse=True
        )

    def save(self, path: str = "school.json") -> None:
        data = [asdict(s) for s in self.students]

        with open(path, "w") as file:
            json.dump(data, file, indent=4)

        logging.info("Student data saved")

    def load(self, path: str = "school.json") -> None:
        try:
            with open(path, "r") as file:
                data = json.load(file)

            self.students = [Student(**d) for d in data]
            logging.info("Student data loaded")

        except FileNotFoundError:
            logging.info("No previous student records found")
