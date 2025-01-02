# 1- perform a task
def greet(first_name):
    print(f"Hello {first_name}")


greet("name1")


# 2- return a value
def get_greet(first_name):
    return f"Hello {first_name}"


message = get_greet("name1")
file = open("file.txt", "w")
file.write(message)
file.close()

"""
all python functions return None by default
"""

# this will be return None because greet function do not have a specified return value to return
print(greet("text 1"))


# we can use by default values like this
# all the optional params come after the required parameters
def increment(number, by=4):
    return number + by


print(increment(2, 3))


def multiply(*numbers):
    return sum(numbers)


print(multiply(2, 3, 4, 5))


def multiply_func_2(**user):
    print(user)


multiply_func_2(id=1, name="John", age=20)

message = "hello world"

def multiply_func_3(name):
    pass

def send_mail(name):
    message = "Hello " + name

multiply_func_3("value")
