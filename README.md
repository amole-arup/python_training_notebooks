
# Python Training Notebooks

Notebooks for teaching Python programming

The buttons launch MyBinder live notebooks (note: these can take a few minutes to load, please be patient). Sometimes it may fail to start, at which point you can return to this page and click the button again.

## Links to Active Online Notebooks

**Python Fundamentals - Online Notebooks**

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%201%20-%20Numbers%20%26%20Variables.ipynb) Session 1 - Numbers and Variables 
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%202%20-%20Collections%20%26%20Loops.ipynb) Session 2 - Collections and Loops 
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%202%20-%20Strings%20%26%20Dates.ipynb) Session 2 - Strings and Dates
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%202%20-%20Tuples,%20Dictionaries%20%26%20Sets.ipynb) Session 2 - Tuples, Dictionaries and Sets
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%203%20-%20Functions.ipynb) Session 3 - Functions
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%203%20-%20Python%20%26%20Excel.ipynb) Session 3 - Python and Excel
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%204%20-%20Python%20%26%20Other%20Software.ipynb) Session 4 - Python and Other Software
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%204%20-%20Scripting%20for%20Grasshopper%20and%20Dynamo.ipynb) Session 4 - Scripting for Grasshopper and Dynamo
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%205%20-%20NumPy%20and%20Pandas.ipynb) Session 5 - NumPy and Pandas
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%205%20-%20Plotting%20with%20Matplotlib.ipynb) Session 5 - Plotting with Matplotlib
* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/python_fundamentals/Session%206%20-%20GUI%20tkinter.ipynb) Session 6 - GUI tkinter

**Functional Python - Online Notebooks**

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amole-arup/python_training_notebooks/main?urlpath=lab/tree/notebooks/functional_python/Functional_Python_1.ipynb) Functional Python 1: List Comprehensions, Lambda Functions & map() 

## Python Fundamentals

[Link to notebook directory](https://github.com/amole-arup/python_training_notebooks/tree/main/notebooks/python_fundamentals)

Python Fundamentals are a series of Jupyter Notebooks that were developed in parallel with a series of training videos, but may also be used independently. The series is focussed on features of Python that are relevant to engineers. It assumes familiarity with Excel but not necessarily any other programming experience. If the notebooks are downloaded and run locally or run online using MyBinder (see links above), then each cell can be run, modified and rerun to learn how the language works.

The sessions cover the following topics:

1. Introduction + Numbers + Variables
2. Dates, Text, Collections (Lists, Tuples, Dictionaries, Sets) & Loops
3. Functions, Python & Excel
4. Python for Scripting of Grasshopper, Dynamo & other software
5. Plotting, NumPy & Pandas
6. Graphical User Interfaces (GUIs)

Note that the folder includes both teaching notebooks (name starts with "Session") and some exercises that are linked to a quiz (not provided here).

## Fundamentals of Functional Programming

[Link to notebook directory](https://github.com/amole-arup/python_training_notebooks/tree/main/notebooks/functional_python)

This section is focussed on approaching Python with a functional programming paradigm. Notebooks are provided that demonstrate the principles.

### What are programming paradigms?

In general, programming paradigms are a consistent set of features that can be identified in programming languages and used to classify them. These features are often related to the way that data is organised and that logic is organised and abstracted. The following is a common list of paradigms. For more detail see the Wikipedia articles Programming paradigm - Wikipedia and Comparison of programming paradigms - Wikipedia.

* Imperative
* Procedural
* Declarative
* Object-oriented
* Functional
 
The first programming languages were unstructured, such as FORTRAN and Cobol. These had no constraints on programming style and would allow the logic to jump from any one place to another (the dreaded GOTO statement). Code didn't have to be organised into modules, variables could be modified (even pointing to different types of data, changing from an integer to a string etc). Modular code was then introduced with subroutines to help organise the code (and GOTO was removed in many languages). Some languages took an object-oriented way of organising abstract classes of information together with standard attributes and methods that acted on the objects. Generalised actions could then be taken on objects, the detailed implementation of which would depend on the object. For example, the action to 'add', could mean summing two numbers, but could result in the concatenation of two text strings.

### Paradigms as Constraints

One way of looking at the various paradigms is to identify what constraints they introduce, as laid out by Bob Martin in the following video - The Last Programming Language.

* The structured programming paradigm is discipline imposed on direct transfer of control (unhindered use of GOTO).
* The object-orientated paradigm is discipline imposed on the indirect transfer of control (on the use of pointers to functions)
* The functional paradigm is discipline imposed upon assignment (restricting mutability - which means that you can't change the value of a variable once you have initialised it).
 

### How old is the functional programming paradigm?

Functional programming languages have become quite popular recently (Haskell, Clojure, Erlang and F#.NET). However, it is actually one of the earliest and academically robust programming paradigms. An early functional programming language was LISP, developed in the late 1950s (~1957), based on computing theory called lambda calculus. This makes it much older than C, which was developed in the 1970s. Common Lisp (first presented publicly in 1982) was based on LISP, and the AutoCAD automation language, AutoLISP was a Common LISP extension.

### What is the functional programming paradigm?

From its name, you can guess that functions are key to it somehow.

* The basic features are sequencing (the sequential execution of operations), selection (flow control, i.e. if-statements) and iteration (using recursion - a function calling itself).
* Pure functions: no side effects - they produce one set of outputs for any one set of inputs and they don't change anything else outside the function. Lambda functions are anonymous functions that can be used in many situations.
* Functions are first-class citizens - they can be used as inputs and can be generated as outputs to other functions. As a result they are often strung together. Ideally a      function should do one thing only.
* Variables are immutable (after they have been initiated, they cannot be changed)
* Special functional functions:  map, filter, reduce, partial.
* Provable - functional code can be validated mathematically.

Benefits:

* Reviewing the logic (debugging) can be straightforward - functions do not change their behaviour based on some hidden state (like a global variable). You can test each function without setting breakpoints.
* They only store values at the end of a sequence (pipe) of functions. This saves storage.
* Immutability solves concurrency problems which means that processes can be shared out to multiple threads or even cores - parallel processing.

Disadvantages:

* Functional programs are typically slower than imperative programs like C and FORTRAN (but they can take advantage of multiple threads or cores).
* Recursion is difficult to implement. Loops would be easier but are not included in strictly functional languages because they require changing variables.
* Combining functions into a complete functional program can be difficult.
* Implementing a GUI typically requires a different paradigm, or adapting other GUI paradigms to FP.
 

## Everyday Examples of Functional Programming

Actually, most people are familiar with functional programming at some level.

**Spreadsheets** are forms of zeroth-order strict-evaluation functional programming system. Each cell takes inputs and generates output as a pure function. They also display the result (which is like having an automatic 'print' statement but has the disadvantage of hiding the code). The cells are strung together to generate the overall flow and logic. Information (data) flows in one direction only.

**Grasshopper** is a graphical scripting environment sitting on top of Rhino3D that is made up of components that take inputs and generate outputs. The components are strung together to generate the overall flow and logic. Information (data) flows in one direction only (mostly).

## Basic Features in Python

At its heart, Python is an interpreted object-oriented programming language with its roots in a program called ABC and borrowings from various programs such as Modula-3 and SETL. The standard implementation of the language is written in C. As an interpreted language, information is fed into it one piece at a time, each of which can modify the state of the data model. Every object (other than numbers) is defined by a dictionary. Data types have to be inferred / identified when each line of code is interpreted, which means that optimisation of code is restricted. This is the reason why some Python code can be much slower than C, which is what the underlying code is written in. Strategies are often available that can speed up Python code.

## Functional Features in Python

1. Immutability - By default, variables in Python are mutable, and indeed new values don't even have to be the same type. While it is possible to define immutable data types, it is simpler just to follow a functional paradigm by implementing a strategy that variables are not reassigned.
2. Pure Functions - Python functions are already first class data types, and can be defined as named functions or as anonymous expressions (lambda functions). While      global variables can be defined and used and changed from within functions, following a functional paradigm would mean that variables are only either passed into the function as arguments to the function (parameters) or defined (hard-wired) inside the function (stateless functions).
3. Composited functions - Functions are built up from using function composition. This can be used with list comprehension and related data structures to simplify the code, and these can also optimised for speed.

## Continuing...

The notebooks contain more information and examples that can be run on MyBinder.

## Online Resources

* [Python manual page: Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
* [Python manual page on sorting](https://docs.python.org/3/howto/sorting.html)
* [Kite: Best Practices for Using Functional Programming in Python (1 page)](https://www.kite.com/blog/python/functional-programming/)
* [Real Python: when and how to use functional programming](https://realpython.com/python-functional-programming/)
* [Real Python: functional programming with Python (a course)](https://realpython.com/learning-paths/functional-programming/)
* [Python Practice Book](https://anandology.com/python-practice-book/index.html) contains a section on functional programming


Copyright - all rights reserved. Material may be viewed, including interaction on MyBinder, but may not be distributed without explicity permission (contact the author via [Issues](https://github.com/amole-arup/python_training_notebooks/issues)).


