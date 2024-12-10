# Put all your functions here, or import them from other files

# putting the type for your parameters is mandatory
def modulo(expr:str, mod:int):
    return eval(expr) % mod

functions = [
    # other way to add your functions
    # { "option": "Compute expression and its modulo\n",    "func":modulo },
    { "option": "Evaluate expression\n",                  "func":eval },
]

# add an entry to the avaiable functions (for the launcher)
def add_option(function, description):
    functions.append({"option": description, "func":function})

# add your functions like this
add_option(modulo, "Compute modulo")