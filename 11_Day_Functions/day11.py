import math

def add_two_numbers(a,b):
    return a+b
def area_of_circle(r):
    return math.pi * r * r
suma=0 
def add_all_nums(*arg):
    for i in arg:
        if isinstance(i,float):
            suma+=i
        else:
            print('jeden lub wiele argumentów to nie liczby')
def convert_celsius_to_fahrenheit(temp):
    return (temp*9/5)+32

def season(month):
    year = {
    'winter':['december','january','february'],
    'spring':['march','april','june'],
    'summer':['july','august','september'],
    'winter':['october','november','december'],
    }
    if month in year['summer']:
        print ('summer')
    elif month in year['spring']:
        print('spring')
    elif month in year['winter']:
        print('winter')
    else:
        print('autumn')
def slope(a,b):
    return math.atan(a)
def solve_quadratic(a,b,c):
    delta=b*b-4*a*c
    if delta<0:
        return 'no real solutions'
    else:
        return str((-1*b+math.sqrt(delta))/2*a)+', '+str(-1*b-math.sqrt(delta))/2*a
def print_list(list):
    for i in range(len(list)):
        print(list[i])

def even_and_odds(a):
    if a > 0:
        if a % 2 ==0:
            print('even: ' + str(a//2+1)+'odds: '+str(a//2))
        else:
             print('even: ' + str(a//2)+'odds: '+str(a//2+1))
    else:
        print('function requires positive number')

def factorial(n):
    fact=1
    for i in range(n+1):
        if i ==0:
            continue
        else:
            fact*=i
    return fact

print(factorial(4))

def is_empty(thing):
    return is_empty(thing)

def greet(name):
    if is_empty(name):
        return 'hello guest'
    else:
        return 'hello' + name

def show_args(**kwargs):
    print('received: ')
    for i,j in kwargs:
        print (i+ ' = '+ j)

def is_prime(n):
    tmp=0
    if type(n)!=type(tmp):
        return False
    if n<=0:
        return False
    if n%2==0 and n!=2:
        return False
    i = 3
    while i*i <= n:
        if n % i ==0:
            return False
        i += 2
    return True

def is_distinct_list(lista):
    set1=set(lista)
    if len(set1) == len(lista):
        return True
    else:
        return False

owoce = ["jabłko", "banan"]

def all_data_type(lista):
    typ=type(lista[0])
    for i in lista:
        if typ!=type(lista[i]):
            return False
    return True



