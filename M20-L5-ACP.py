#ACP-Perform List Comprehension

n = [1, 2, 3,4,5,6]
even =filter(lambda x: x % 2 == 0, n)
odd =filter(lambda x: x % 2 != 0, n)
print("Even numbers:", list(even))
print("Odd numbers:", list(odd))

