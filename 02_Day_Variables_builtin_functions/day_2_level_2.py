import math
name = "Julian"
surname = "Kzoiar"
print(type(name),", ",type(surname))
num_one=5
num_two=4
total = num_one + num_two
diff=num_one - num_two
product= num_one * num_two
division = num_one/num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one//num_two
radius = int(30)
area_of_circle = math.pi * pow(radius,2)
circum_of_circle = 2 * math.pi * radius
radius_from_user = int(input("gimme radius pls"))
print( math.pi * pow(radius_from_user,2))
first_name, last_name, country, age = input("name"),input("surname"),input("country"), input("age")
print(first_name,last_name,country,age)
