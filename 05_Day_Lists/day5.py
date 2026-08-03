#dzień o listach

list=[]
list2=[1,2,3,4,5]
len(list2)
list2.pop(0)
list2.pop(-1)
list2.pop(len(list2)//2)
mixed_data_types=["julian",19,180,"dating","wroclaw"]
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
it_companies[0] = "facebok"
print(it_companies)
it_companies.append("komarch")
it_companies.insert(3,"microslop")
it_companies[0].upper
it_companies + '#; '
print("Google" in it_companies)
list2.sort()
list2.reverse()
it_companies2=it_companies[3:4]
it_companies.remove[0]
it_companies.remove[len(it_companies)//2]
it_companies.remove[-1]
it_companies.clear
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(full_stack.index("Redux"),"Python")
full_stack.insert(full_stack.index("Python"),"SQL")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
maxi=ages[-1]
print(ages[0],ages[-1])
ages+ages[0]+maxi
ages.sort()
if(len(ages)%2==0):
    mediana=(ages[len(ages)//2]+ages[len(ages)//2-1])/2
else:
    mediana=ages[len(ages)//2]
average = sum(ages)/len(ages)
rang = maxi - ages[0]
print(abs(ages[0]-average)>maxi-average)
          
