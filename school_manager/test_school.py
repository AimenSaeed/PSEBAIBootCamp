
import pytest

from school.student import Student, get_grade, make_comment
from school.manager import SchoolManager


@pytest.fixture
def manager():
    return SchoolManager()


def test_add_student(manager):
    manager.add_student(Student("Ali", 12))
    assert len(manager.students) == 1


def test_duplicate_student(manager):
    manager.add_student(Student("Ali", 12))

    with pytest.raises(ValueError):
        manager.add_student(Student("Sara", 12))


def test_average():
    student = Student("Ali", 12, [80, 90, 70])
    assert student.average() == 80


def test_add_marks(manager):
    manager.add_student(Student("Ali", 12))
    manager.add_marks(12, [80, 90])

    assert manager.find_student(12).marks == [80, 90]


def test_invalid_marks(manager):
    manager.add_student(Student("Ali", 12))

    with pytest.raises(ValueError):
        manager.add_marks(12, [110])


def test_ranking(manager):
    manager.add_student(Student("Ali", 12, [70]))
    manager.add_student(Student("Sara", 13, [90]))

    assert manager.ranking()[0].name == "Sara"


def test_grade_and_comment():
    student = Student("Ali", 12, [90, 85])
    assert get_grade(student.average()) == "A"
    assert make_comment(student) == "Excellent in all subjects, keep it up."
