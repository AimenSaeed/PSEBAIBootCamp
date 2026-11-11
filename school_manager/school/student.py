
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_no: int
    marks: list[int] = field(default_factory=list)

    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)


def get_grade(average: float) -> str:
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 33:
        return "D"
    return "F"


def make_comment(student: Student) -> str:
    if not student.marks:
        return "No marks available yet."

    avg = student.average()

    if avg >= 80:
        return "Excellent in all subjects, keep it up."
    elif avg >= 60:
        return "Good effort, keep improving."
    elif avg >= 33:
        return "You passed, but more practice is needed."
    else:
        return "Work harder and keep practicing."
