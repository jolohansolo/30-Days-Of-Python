dog={
    'name':'reksio',
    'color':'black',
    'breed':'hound',
    'legs':'long',
    'age':17
}

student = {'first_name':'jasiu', 'last_name':'kowalski', 'gender':'m', 'age':7, 'marital status':"single", "skills" : ['reading','writing'], 'country':'poland', 'city':'cracow', 'address':'zlota, 44' }
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('eating')
print(student['skills'])
keys_student = student.keys()
values_student = student.values()
print(student.items())
student.pop('addres')
del dog
