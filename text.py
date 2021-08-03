import copy

list1 = ['1.03MB', '113.39KB', '115.18KB', '137.33KB', '256.04KB']
list2 = copy.copy(list1)
list3 = []
for x in list1:
    if 'MB' in x:
        x = float(x[:-2])*1024
    elif 'KB' in x:
        x = float(x[:-2])
    list3.append(x)

print(list3,list2)