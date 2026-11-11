
import pytest
from grades import grade


@pytest.mark.parametrize("mark, expected", [
    (32, "F"),
    (33, "D"),
    (59, "D"),
    (60, "C"),
    (69, "C"),
    (70, "B"),
    (79, "B"),
    (80, "A")
])
def test_grade(mark, expected):
    assert grade(mark) == expected


def test_invalid_marks():
    with pytest.raises(ValueError):
        grade(101)


def test_negative_marks():
    with pytest.raises(ValueError):
        grade(-1)
