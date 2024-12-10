# Put all your functions here


def modulo(expr:str, mod:int):
    return eval(expr) % mod

functions = [
    # other way to add your functions
    # { "option": "Compute expression and its modulo\n",    "func":modulo },
    { "option": "Evaluate expression\n",                  "func":eval },
]

def add_option(function, description):
    functions.append({"option": description, "func":function})
    
add_option(modulo, "Compute modulo")