from inspect import signature
from functions import *


# Display all options and their associated functions
def pres_options(opt_func):
    
    print("Please choose an option:\n")
    # display all available functions
    [print(str(i) + " > " + opt_func[i]["option"] + "\n") for i in range(len(opt_func))]
    choice=int(input("\t>"))
    # this will retrieve all the required parameters for your functions and their names
    p = {name: param.annotation for name, param in signature(opt_func[choice]["func"]).parameters.items()}
    if(len(opt_func) >= choice):
        # query user input for each parameter
        params = [(type)(input("\nEnter param \"" + str(name) + "\" >")) for name, type in p.items()]
        # execute function
        print((opt_func[choice]["func"])(*params))
    else:
        print("The chosen index is out of bounds. Shutting down.")
    return
    
    
pres_options(functions)