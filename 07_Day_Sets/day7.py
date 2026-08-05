it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)
it_companies.add('Twitter')
it_companies.update('komarch','IBM')
it_companies.remove('Twitter')
#discard works allways remove only when item exists
A.union(B)
A.intersection(B)
print(A.issubset(B))
print(A.isdisjoint(B))
A.symmetric_difference(B)
del(A)
del(B)
sage = set(age)
print(len(age)>len(sage))
sentence = 'I am a teacher and I love to inspire and teach people.'
set_of_words = set(sentence.split(' '))
print(len(set_of_words))