import crayons

def greet(name, msg=" It's a great day to save lives"):
    print(crayons.red('Hello ' + name + msg))

greet("Ryan")

print(crayons.blue("Hello Friend"))