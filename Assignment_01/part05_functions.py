"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""
# Warm-up: Small helpers
def area_of_circle(r):
    return 3.14 * r*r

def is_even(n):
    return n % 2==0

def greet(name, lang="ur"):
    if lang=="en":
        return f"Heyyy {name}!"
    else:
        return f"Assalam-o-Alaikum {name}!"

print(area_of_circle(5))
print(area_of_circle(10))
print(area_of_circle(15))

print(is_even(4))
print(is_even(5))
print(is_even(6))

print(greet("Aimen"))
print(greet("Aimen", "en"))
print(greet("Iqra"))

#Build: Marks Toolkit
def average(marks):
    return sum(marks)/len(marks)

def grade(average):
    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    else:
        return "F"

def report(name,marks):
    avg=average(marks)
    grd=grade(avg)
    return f"Student Name: {name}\nAverage Marks: {avg}\nGrade: {grd}"

report1=report("Aimen",[85,90,78,92])
report2=report("Iqra",[75,80,68,72])
report3=report("Ali",[55,60,48,52])
print(report1)
print(report2)
print(report3)

# Challenge: Comprehensions
def squares(n):
    return [i*i for i in range(n)]

def long_name(names):
    return [name for name in names if len(name)>4]

def result_sheet(marks):
    average_marks={}
    for student, scores in marks.items():
        total=sum(scores)
        average=total/len(scores)
        average_marks[student]=average
    return average_marks

print(squares(11))
names=["Ali","Sara","Iqra","Zainab","Saeed"]
print(long_name(names))
marks = {
    "Ali" : [80,72,91],
    "Sara" :[95,88,90],
    "Iqra" : [70,75,80,85],
    "Zainab" : [88,39,85],
    "Saeed" : [60,65,70]
}
print(result_sheet(marks))