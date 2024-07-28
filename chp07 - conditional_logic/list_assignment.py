def enrollment_stats(uni_stats):
    enrollments = []
    tuition = []
    for i in uni_stats:
        enrollments.append(i[1])
        tuition.append(i[2])
    return enrollments, tuition

def total(values):
    total = 0
    for n in values:
        total += n
    return total

def mean(values):
    return int(total(values) / len(values))

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        index = int(len(values) / 2 - 0.5)
        median = values[index]
    else:
        median = (values[len(values) / 2] + values[len(values) / 2 - 1]) / 2
    return median

universities=[
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

enrollments, tuition = enrollment_stats(universities)
print(enrollments)
print(tuition)

print(f"""
**************************
Total students: {total(enrollments)}
Total tuition: $ {total(tuition)}

Student mean: {mean(enrollments)}
Student median: {median(enrollments)}

Tuition mean: $ {mean(tuition)}
Tuition median: $ {median(tuition)}
**************************
""")
