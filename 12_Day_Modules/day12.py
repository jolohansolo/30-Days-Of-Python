import random
import string
def random_user_id():
    string1 =''
    for i in range(6):
        s=random.randint(1,3)
        if s == 1:
            l=random.choice(string.ascii_letters) 
        if s == 2:
            l=random.choice(string.digits) 
        if s == 3:
            l=random.choice(string.punctuation)
        string1+=l 
    return string1


def random_user_id2(length, ammount):
    list_of_id = []
    for j in range(ammount):
        stringn= ''
        for i in range(length):
            s=random.randint(1,3)
            if s == 1:
                l=random.choice(string.ascii_letters) 
            if s == 2:
                l=random.choice(string.digits) 
            if s == 3:
                l=random.choice(string.punctuation)
            stringn += l 
        list_of_id.append(stringn)
    return list_of_id


def rgb_color_gen():
    return 'rgb(' + str(random.randint(0,255)) + ',' + str(random.randint(0,255)) + ',' + str(random.randint(0,255)) + ')'

def hex_colors():
    string1 ='#'
    for i in range(6):
        s=random.randint(1,2)
        if s == 1:
            l=random.choice(['a','b','c','d','e','f']) 
        if s == 2:
            l=random.choice(string.digits) 
        string1+=l 
    return string1
    
def list_of_hex_colors(n):
    list_of_hex=[]
    for i in range(n):
        list_of_hex.append(hex_colors())
    return list_of_hex

def list_of_rgb_colors(n):
    list_of_rgb=[]
    for i in range(n):
        list_of_rgb.append(rgb_color_gen())
    return list_of_rgb

def generate_colors(type, ammount):
    if type == 'hexa':
        return list_of_hex_colors(ammount)
    if type == 'rgb':
        return list_of_rgb_colors(ammount)
    else:
        return  'provide rgb or hexa'

def array_riddle():
    array=[]
    set=[0,1,2,3,4,5,6,7,8,9]
    for i in range(7):
        n=random.choice(set)
        array.append(n)
        set.remove(n)
    return array

print(array_riddle())