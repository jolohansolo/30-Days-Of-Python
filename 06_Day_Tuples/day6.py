tpl=()
brothers=("julian","jan","nordzik")
sisters=("zosia","ala","jula")
siblings=brothers+sisters
print(len(siblings))
family_members=tuple(brothers+sisters+"mother"+"father")
family_list=list(family_members)
family_list.pop(len(family_list//2))
family_list2=family_list[0:2]
family_list3=family_list[-1:-3]
del tpl
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)