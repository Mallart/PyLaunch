from inspect import signature
from functions import *


# Display all options and their associated functions
def pres_options(opt_func):
    
    print("Please choose an option:\n")
    [print(str(i) + " > " + opt_func[i]["option"] + "\n") for i in range(len(opt_func))]
    choice=int(input("\t>"))
    p = {name: param.annotation for name, param in signature(opt_func[choice]["func"]).parameters.items()}
    if(len(opt_func) >= choice):
        params = [(type)(input("\nEnter param \"" + str(name) + "\" >")) for name, type in p.items()]
        print((opt_func[choice]["func"])(*params))
    return
    
    
pres_options(functions)