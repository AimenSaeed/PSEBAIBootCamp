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
def result_sheet(marks):
    average_marks={}
    for student, scores in marks.items():
        total=sum(scores)
        average=total/len(scores)
        average_marks[student]=average
    return average_marks
marks = {
    "Ali" : [80,72,91],
    "Sara" :[95,88,90],
    "Iqra" : [70,75,80,85],
    "Zainab" : [88,39,85],
    "Saeed" : [60,65,70]
}
print(result_sheet(marks))