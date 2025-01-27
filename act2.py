# Act2-Zip elements
list1 = {10,20,30,40}
list2 = {'a','b','c','d'}
res = list(zip(list1, list2))
print(res)


# Print elements one by one, but elements of 2nd list will be in reverse order
l1 = [10, 20, 30]
l2 = [100, 200, 300]
for a, b in zip(l1, l2[::-1]):
    print(a, b)


# Zip into dictionary
stud = ['prachi', 'pihu', 'aryan']
roll = [1,2,3]

dict1 = {stud: roll for stud,roll in zip(stud, roll)}
print(dict1)
