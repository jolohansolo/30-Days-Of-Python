from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_countries():
    for i in countries:
        print(i)

def print_names():
    for i in names:
        print(i)

def print_numbers():
    for i in numbers:
        print(i)

upper_countires = list(map(lambda country : country.upper(),countries))
print(upper_countires)

sqr_num = list(map(lambda n: n**2,numbers))
print(sqr_num)

upper_names = list(map(lambda name : name.upper(),names))
print(upper_names)

def is_land_in_name(name):
    if 'land' in name:
        return True
    else:
        return False
countries_with_land = list(filter(is_land_in_name,countries))
print(countries_with_land)

six_letter_countries = list(filter(lambda x : len(x)==6,countries))

six_letter_or_more_countries = list(filter(lambda x : len(x)>=6,countries))

countries_on_E = list(filter(lambda x : x[0]=='E',countries))
print(countries_on_E)

filtered_nums = list(filter(lambda x : x>=69,map(lambda x : x**2,numbers)))
print(filtered_nums)

def get_string_lists(lst):
    string_lst=list(filter(lambda x: type(x)==str,lst))
    return string_lst

sum = int(reduce(lambda x,y : x + y,numbers))

sentence = str(reduce(lambda x,y: x+', '+y,countries))+' are north european countries'

def countries_in_dictionary(lst):
    keys = list(map(lambda k,: k[0],lst))
    values = []
    for i in keys:
        values.append(filter(lambda x : x[0],lst))
    

countries_in_dictionary(countries)