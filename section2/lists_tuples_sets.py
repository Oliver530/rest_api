# list (mutable)
grades = [70, 75, 80]

# tuple (immutable)
tuple_grades = (70, 75, 80)

# set (unique and unordered)
set_grades = {5, 6, 7, 9}

print(sum(tuple_grades) / len(tuple_grades))

print(set_grades)

#

grades[0] = 20
grades.append(86)
print(grades)

tuple_grades = tuple_grades + (100,)
print(tuple_grades)

## set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(your_lottery_numbers.difference(winning_numbers))
