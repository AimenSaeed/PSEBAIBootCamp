def calculate_average(marks):
    return sum(marks) / len(marks)


def check_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    else:
        return "C"