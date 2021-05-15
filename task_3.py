students = [
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agness', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Don', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alexey', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susanne', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Stevie', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktanbek', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]


python = []
javascript = []
java = []
for student in students:
    if student['course'] == 'python':
        python.append(student['name'])
    if student['course'] == 'javascript':
        javascript.append(student['name'])
    if student['course'] == 'java':
        java.append(student['name'])
        # print(student['name'])

courses = {'python': python, 'javascript': javascript, 'java': java}
# print(courses)
def age_inf(student_list):
    names_ages = {student['name']: student['age'] for student in students}
    return(names_ages)
# print(age_inf(students))

names_ages = {student['name']: student['age'] for student in students}

names = ['Janyl', 'Nursultan', 'Meerim', 'Emir', 'Susann', 'Marcus', 'Aidin', 'Aigerim', 'Angela', 'Albert', 'Jyldyz', 'Doe', 'Gloria', 'Aliaskar', 'Martin', 'John', 'Andrew','Steve', 'Johnathan','Adyl', 'Chyngyz', 'Michael', 'Atay', 'Mikkel', 'Agnes', 'Aidana', 'Sultan', 'Nash', 'Nicolas', 'Mirbek', 'Aktan', 'Emirlan', 'Jennifer', 'Eniston', 'Alex', 'Mark']

def sovpad(names_age_l, names_l):
    for stud in names_age_l:
        if stud in names_l:
            print(f'{stud} - {names_age_l[stud]}')
        if stud not in names_l:
            print(f'{stud} - Такого имени в словаре не существует')

sovpad(names_ages, names)

