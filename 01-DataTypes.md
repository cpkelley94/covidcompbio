# Introduction to Data Types - April 18, 2020

Hi everyone! As you are going through the Python 
courses on edX, you have already been working with 
some of the most useful **data types** in Python, 
including _integers_, _floats_, and _strings_. Data 
types are a core component of any programming 
language, allowing you to store and manipulate many 
different kinds of information, like numbers, words, and 
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
of 5. Thus, when you are declaring a variable in 
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

Just because data types are _implicit_ in Python 
doesn't mean they aren't important. For example, if 
you try to run something like this,

```python
my_int = 5
my_string = "blue"
print(my_int + my_string)
```

you'll get the following error:

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-adf924bcdbe7> in <module>()
----> 1 print(my_int + my_string)

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

If you try to add a string to an integer, Python 
doesn't know what to do! Data types define not 
only the kind of information contained in a variable, 
but also how you use it, the methods available 
to it, and how it interacts with other variables. 


## Data types reference sheet

Different data types have different use cases, 
and some are more efficient than others for 
specific operations. In addition, while Python 
itself has many data types that are broadly useful, 
external libraries also can provide their own data 
types that add extra functionality and efficiency 
for specific types of analysis. In this section, we'll 
provide a reference for some of the most common 
data types in computational biology, and we'll 
go over when they are best to use.

### Python built-in types

- **Boolean (`bool`):** either `True` or `False`. This is the simplest data type, with only two possible values. Booleans are the foundation of programming logic: for example, booleans allow the computer to decide if code in an `if` block should be run, or if a `while` loop should end. Any comparison we perform (such as `my_int < 5`) will give either `True` or `False`, allowing us to run some code only when a condition is met, or run other code when it is not.
  - Example declaration: `var = True`
  - Booleans are also useful as _flags_ that we can set in response to something in our data and retrieve later. For example, if we want to include a line in our output file about _TARDBP_ read counts only if our data has at least one read that maps to that gene, we might make a boolean variable called `data_has_TARDBP` to keep track of this. We could initialize it as `data_has_TARDBP = False` and then flip it to `True` if we detect a _TARDBP_ read at any point in our data analysis. At the end of the script, we would then check if this flag is `True` using `if`, and modify our output accordingly.
  - To check if a boolean variable (eg. `my_bool`) is True, simply write `if my_bool:`. To check if it's False, use the `not` keyword (`if not my_bool:`).

- **Integer (`int`):** any whole number, including positive and negative numbers (eg. 5, 0, -107). Integers are commonly used for counting, indexing iterable types like lists (eg. `my_list[1]`), and iterating through indices in a `for` loop using `range()`. Unlike most programming languages, Python does not place a limit on the largest possible integer.
  - Example declaration: `var = 2`
  
- **Floating-point (`float`):** a decimal number (eg. 1.1, 3.14159265, 2.998e8). Floats are the basic data type for storing decimal numeric data, like physical measurements, ratios, and distances. Floats in Python store 53 bits of information, or approximately 16 significant digits of precision.
  - Example declaration: `var = 1.1`
  - In Python 3, fractions of integers automatically evaluate to floats (eg. 3/7 becomes 0.42857142857142855).
  - In order to create very large or very small numbers, you can also use scientific notation to declare floats. To do this, place an `e` in between the decimal number and the exponent (eg. `5.4e10`).
  - **Warning**: Computers fundamentally store information using binary representation (0's and 1's), not in the base 10 that we humans work with, and this can cause some funny behavior if we don't structure our code carefully. For example, if we add the float `0.001` to a variable `var` 1000 times using a `for` loop, the variable's value after the loop evaluates to `1.0000000000000007`, rather than exactly 1. This is because the binary representation of the number `0.001` that the computer creates is only a high-precision approximation, and the error quickly becomes visible after only a small number of mathematical operations. In your code, if our goal is to check if `var` is equal to 1, you probably won't get the outcome you expect. Instead, we should check if `var` is _extremely close_ to 1, using something like `if abs(var - 1.0) < 1E-8:`. This type of comparison is also implemented in external libraries, including `math` (eg. `math.isclose()`).

- **String (`str`):** an ordered collection of characters (eg. `"this is a string"`). Strings are the fundamental type for storing text data, including letters, words, phrases, and sentences, as well as sequencing reads, sequence alignment information (eg. CIGAR strings), and file paths.
  - Example declaration: `var = "blue"`
  - Characters in a string can be retrieved with an index (eg. `my_string[0]` returns the first character in the string).
  - Substrings can be retrieved by _slicing_ (eg. `my_string[0:3]` returns the first three characters in the string).
  - Strings can be _concatenated_ by adding them (eg. `'a' + 'b'` returns `'ab'`).
  - In Python, strings can be declared using either single quotes (`'blue'`) or double quotes (`"blue"`). For example, if we want to store the sentence "It's a wonderful life!" as a string, we can enclose the string in double quotes to avoid problems with the apostrophe.
  - If you need to use a character in a string that messes with the string declaration (eg. both single and double quotes in a single string), you can _escape_ the problematic character by preceding it with a backslash `\`.
  
- **List (`list`):** an ordered collection of items of any type (eg. `[0, 1, 2, 3]`, `[0, 1.0, "red", True]`).
