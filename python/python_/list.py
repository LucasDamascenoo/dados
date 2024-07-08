
my_list = [1, 2, 3, 4, 5]

print(my_list)

# list comprehension

dobro = [x**2 for x in my_list]
print(dobro)

impar = [x for x in my_list if x % 2 == 1]
print(impar)
