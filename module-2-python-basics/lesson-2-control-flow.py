"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Kenneth Sigua
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Control flow allows a program to make a decisions based on 
different conditions. The program check if something is true or false 
and then decides which part to the code to run

In the code we use if statement to check if a condition is true. If the
first condtion is false, it will check the next condtion which is elif statement.
If all condition are false, it will run the else command.

============================================
KEY VOCABULARY
============================================
- condition: Its a rule or statement that the program check to see if it is True or False.
- if / elif / else: Its a statement that used to make decisions in the program.
- comparison operator: Its a symbol used tocompare values like ==,!=, >, <, >=, <=
- boolean expression: Its a expression that evaluates to either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

grade = 85

if grade >= 90:
    print("You got an A grade!")
elif grade >= 75:
    print("You passed")
else:
    print("You failed")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I always forget to use colon (:) at the end of the if, elif, and else statement.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Control flow can be used in a project that need to make a decisions.For example
student grade and display whether the student passed or failed.
"""
