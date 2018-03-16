def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))

#

print(methodception(lambda: 35 + 77))

my_list = [13, 56, 132, 201]
print(list(filter(lambda x: x % 2 == 0, my_list)))

# same as
print([x for x in my_list if x % 2 == 0])
