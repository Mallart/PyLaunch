# PyLaunch
 Python quick function launcher (like a shell)
## Why did I create this ?
My maths and cryptography teacher told us to create programs to calculate faster.
As we use mostly Python in our courses, I decided to create a script for everyone that could need it to have all our functions and formulas in the same place.
## How does it work ?
Basically, I use Python's *inspect* and *signature* libraries to retrieve informations about the functions put in an array of dictionaries.

Each dictionary is a pair of a string and a pointer to a function (also called callback). When the right index is queried in the launcher function, it calls the associated callback.

The "option" field is only there for display purposes.
## Why should I use it ?
If you use your computer like a big calculator and have several functions you often use while working, you can translate them to Python and put them in the functions.py file (or import them from that file).

Think of adding them to the "functions" array though, and to sign (put explicit types) for your functions parameters. 
