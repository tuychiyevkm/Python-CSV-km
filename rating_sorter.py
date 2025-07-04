import csv

with open('students.csv') as f:
    reader = csv.DictReader(f)
    students = list(reader)

students_sorted = sorted(students, key=lambda x: int(x['score']), reverse=True)

with open('rating.csv', 'w') as f2:
    fieldnames = ['rank', 'name', 'score']
    writer = csv.DictWriter(f2, fieldnames=fieldnames)
    writer.writeheader()

    for i, student in enumerate(students_sorted, start=1):
        writer.writerow({
            'rank': i,
            'name': student['name'],
            'score': student['score']
        })

