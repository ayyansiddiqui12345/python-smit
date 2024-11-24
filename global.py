# global
complete = "ayyan will be "


# a function with parameter
def sentence(user_age):
    # a local variable
    exclamation = "!"
    # calling global
    global complete
    complete = f"{complete}{user_age}{exclamation}"
    print(complete)


user_age = "turning 18 this january"
sentence(user_age)
print("the complete variable is now a whole senence:\t\n", complete)
