def my_func (first):
    p = prefix()
    last = input("Hi " + p + first + "! Please enter last name: ")
    print("Nice to meet you " + first + " " + last + "!")

def prefix():
    return "Mr. "

my_func("Elaina")

