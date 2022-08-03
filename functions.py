#intendation indicates the body of function 
def say_hello():
    print("Hello User")
    print("You're Welcome!")

    print('erfdffh')
print("not in function")

#calling the function
say_hello()

#function with passing parameters
def sayName(name, age):
    print("Hello " + name + ", you are " + age)

sayName("Sewwa", "25")

#function with return statement
def square(length):
    return length*length

print((square(4)))
