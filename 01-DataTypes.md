# Introduction to Data Types - April 18, 2020

Hi everyone! As you are going through the Python 
courses on edX, you have already been working with 
some of the most useful **data types** in Python, 
including _integers_, _floats_, and _strings_. Data 
types are a core component of any programming 
language, allowing you to store and manipulate many 
different kinds of data, like numbers, words, and 
lists. Here, we'll discuss how data types are 
implemented in Python and provide a reference for 
some of the most useful data types for biological 
data analysis.


## How do data types work in Python?

At first, the existence of different data types in 
Python may not be obvious. In many other programming 
languages, such as C++, data types are _explicitly_ 
defined when you declare a variable. For example, if 
we want to make a new variable `num` to hold the 
number 5, we would write

```c++
int num = 5;
```

In C++, we have to tell the compiler what type the 
variable is before we can use it, and we do that here with 
the `int` keyword. The developers of Python saw this 
code structure as redundant: we already know that 
`num` is an integer because we are giving it the value 
of 5. This, when you are declaring a variable in 
Python, the type identifier is omitted for simplicity:

```python
num = 5
```

Also, since Python is a scripting language, it can do 
something called **dynamic memory allocation**: rather 
than having to block off memory in the computer before 
the program runs, Python can grab the memory it needs 
as it progresses through your script. Different 
data types require different amounts of space in memory; however, 
since Python allocates memory dynamically, we are free 
to change the type of a variable whenever we want. For 
example,

```python
my_var = 5  # my_var is declared as an integer
my_var += 2  # we can add 2 to my_var to make it 7
my_var = "blue"  # now it's a string!
```


## Data types reference
