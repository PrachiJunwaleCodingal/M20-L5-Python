#Act1- Hands on Map

#1. Add list using lambda function and map
n1 = [1, 2, 3]
n2 = [4, 5, 6]
sum = map(lambda x, y: x + y, n1, n2)
print("Addition:", list(sum))


#2. using map
list1 = [10,20,30,40]  
def cube(n):    
    return n*n*n  

result = list(map(cube, list1))
print("Square using map():", result)
