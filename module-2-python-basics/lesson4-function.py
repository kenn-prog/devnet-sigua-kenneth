"""
Module 2 — Lesson 4: Functions
Student: Kenneth Sigua
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
functions is a reusable block of code that perform a specific task.
Instead of repeating writing the same code multiple times, I can use function
and put that code inside the function. I can call that function whenever i need it.

Functions can also receive information through parameters. After doing its task, a 
function can use return to send a result back to the part of the program that called it.

============================================
KEY VOCABULARY
============================================
- function: Its a reusable block of code that perform a specific task.
- parameter: Its a value that I can pass to a function to provide input or information.
- return: Its a statement that send a result back to the part of the program that called
-argument: Its a value that I pass to a function when I call it. It is used to provide input 
or information to the function.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_ave(grade1, grade2, grade3):
    total = grade1 + grade2 + grade3
    ave = total / 3
    return ave

math_grade = 90
python_grade = 85
networking_grade = 80

average_grade = calculate_ave(math_grade, python_grade, networking_grade)

print("Average Grade:", average_grade)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I mistake that i done is to confusing the parameter and argument.  A parameter 
is  the varaible written when we creating a variable, while argument is the actual
value that we pass to the function when we call it.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions can be useful in a project because we can use it to organize our code and 
prevent repeating writing the code multiple times.
"""
