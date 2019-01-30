# https://www.programiz.com/python-programming/methods/built-in
# https://www.programiz.com/python-programming/examples/ascii-character


# Python abs() 	returns absolute value of a number
# Python all() 	returns true when all elements in iterable is true
# Python any() 	Checks if any Element of an Iterable is True
# Python ascii() 	Returns String Containing Printable Representation
# Python bin() 	converts integer to binary string
# Python bool() 	Coverts a Value to Boolean
# Python bytearray() 	returns array of given byte size
# Python bytes() 	returns immutable bytes object
# Python callable() 	Checks if the Object is Callable
# Python chr() 	Returns a Character (a string) from an Integer
# Python classmethod() 	returns class method for given function
# Python compile() 	Returns a Python code object
# Python complex() 	Creates a Complex Number
# Python delattr() 	Deletes Attribute From the Object
# Python dict() 	Creates a Dictionary
# Python dir() 	Tries to Return Attributes of Object
# Python divmod() 	Returns a Tuple of Quotient and Remainder
# Python enumerate() 	Returns an Enumerate Object
# Python eval() 	Runs Python Code Within Program
# Python exec() 	Executes Dynamically Created Program
# Python filter() 	constructs iterator from elements which are true
# Python float() 	returns floating point number from number, string
# Python format() 	returns formatted representation of a value
# Python frozenset() 	returns immutable frozenset object
# Python getattr() 	returns value of named attribute of an object
# Python globals() 	returns dictionary of current global symbol table
# Python hasattr() 	returns whether object has named attribute
# Python hash() 	returns hash value of an object
# Python help() 	Invokes the built-in Help System
# Python hex() 	Converts to Integer to Hexadecimal
# Python id() 	Returns Identify of an Object
# Python input() 	reads and returns a line of string
# Python int() 	returns integer from a number or string
# Python isinstance() 	Checks if a Object is an Instance of Class
# Python issubclass() 	Checks if a Object is Subclass of a Class
# Python iter() 	returns iterator for an object
# Python len() 	Returns Length of an Object
# Python list() Function 	creates list in Python
# Python locals() 	returns dictionary of current local symbol table
# Python map() 	Applies Function and Returns a List
# Python max() 	returns largest element
# Python memoryview() 	returns memory view of an argument
# Python min() 	returns smallest element
# Python next() 	Retrieves Next Element from Iterator
# Python object() 	Creates a Featureless Object
# Python oct() 	converts integer to octal
# Python open() 	Returns a File object
# Python ord() 	returns Unicode code point for Unicode character
# Python pow() 	returns x to the power of y
# Python print() 	Prints the Given Object
# Python property() 	returns a property attribute
# Python range() 	return sequence of integers between start and stop
# Python repr() 	returns printable representation of an object
# Python reversed() 	returns reversed iterator of a sequence
# Python round() 	rounds a floating point number to ndigits places.
# Python set() 	returns a Python set
# Python setattr() 	sets value of an attribute of object
# Python slice() 	creates a slice object specified by range()
# Python sorted() 	returns sorted list from a given iterable
# Python staticmethod() 	creates static method from a function
# Python str() 	returns informal representation of an object
# Python sum() 	Add items of an Iterable
# Python super() 	Allow you to Refer Parent Class by super
# Python tuple() Function 	Creates a Tuple
# Python type() 	Returns Type of an Object
# Python vars() 	Returns __dict__ attribute of a class
# Python zip() 	Returns an Iterator of Tuples
# Python __import__() 	Advanced Function Called by import

# --------------------------------------------------------------------------

# https://www.programiz.com/python-programming/examples/ascii-character

# Here we have used ord() function to convert a character to an integer (ASCII value). This function actually returns the Unicode code point of that character.
#
# Unicode is also an encoding technique that provides a unique number to a character. While ASCII only encodes 128 characters, current Unicode has more than 100,000 characters from hundreds of scripts.
#
# Your turn: Modify the code above to get character from the ASCII value using the chr() function as shown below.
#
# >>> chr(65)
# 'A'
# >>> chr(120)
# 'x'
# >>> chr(ord('S') + 1)
# 'T'
#
# Here, ord() and chr() are built-in functions. Visit here to know more about built-in functions in Python.



# https://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
# >>> chr(ord('a') + 3)
# 'd'
# >>>
#
# In Python 2, there is also the unichr function, returning the Unicode character whose ordinal is the unichr argument:
#
# >>> unichr(97)
# u'a'
# >>> unichr(1234)
# u'\u04d2'