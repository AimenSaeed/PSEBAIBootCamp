# Build:

def grade(mark: int) -> str:

    if mark < 0 or mark > 100:
        raise ValueError("Marks must be between 0 and 100")

    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 33:
        return "D"
    else:
        return "F"
