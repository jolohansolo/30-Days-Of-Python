age = input('enter your age:')
age_int=int(age)
if age_int >=18 :
    print('you are old enough to drive')
else:
    print('you need ' +str(18 - age_int) +' more years to learn to drive')

my_age = input('enter my age:')
your_age = input('enter your age:')
my_age_int=int(my_age)
your_age_int=int(your_age)
if my_age_int > your_age_int :
    if abs(str(my_age_int-your_age_int)) == 1:
        print('i am older' + str(abs(my_age_int-your_age_int)) + 'year')
    else:
        print('i am older' + str(abs(my_age_int-your_age_int)) + 'years')
elif my_age_int == your_age_int:
    print( 'we are the same age')
else:
    if str(abs(my_age_int-your_age_int)) == 1:
        print('you are older' + str(abs(my_age_int-your_age_int)) + 'year')
    else:
        print('you are older' + str(abs(my_age_int-your_age_int)) + 'years')

a = input('num1')
b = input("num2")
if a> b:
    print('a bigger than b')
elif b >a:
    print('b bigger than a')
else:
    print('a is equal to b')

grade=input('give a grade')
grade_int= int(grade)
if grade_int>=90:
    print('A')
elif grade_int>=80 and grade_int<90:
    print('B')
elif grade_int>=70 and grade_int<80:
    print('C')
elif grade_int>=60 and grade_int<70:
    print('D')
else:
    print('F')

year = {
    'winter':['december','january','february'],
    'spring':['march','april','june'],
    'summer':['july','august','september'],
    'winter':['october','november','december'],
    }

month = input('month:')
if month in year['summer']:
    print ('summer')
elif month in year['spring']:
    print('spring')
elif month in year['winter']:
    print('winter')
else:
    print('autumn')

fruit = input('fruit')
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print(fruit + ' is in the list')
else:
    fruits.append(fruit)
    print('fruit added')
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if len(person['skills'])!=0: 
    print (person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print (person['skills'])
else:
    print('no skills')

# 3* nie chce mi się robić

if person['is_married']==True and person['country']=='Finland':
    print(person['first_name'] + ' lives in ' + person['country']+ ' and is married')
