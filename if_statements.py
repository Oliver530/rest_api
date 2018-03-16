should_continue = True

if should_continue:
    print("Hello")

# Exercise

def who_do_you_know():
    string_of_names = input("Enter people you know: ")
    people_list = string_of_names.split(",")
    
    people_without_spaces = [name.strip() for name in people_list]
    return people_without_spaces

def ask_user():
    name = input("Enter a name: ")
    if name in who_do_you_know():
        print("I know {} too!".format(name))
    else:
        print("I don't know {}!".format(name))

ask_user()
