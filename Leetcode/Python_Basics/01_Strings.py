

# str.find(str, beg=0, end=len(string))
# It determines if string str occurs in string, or in a substring of string if starting index beg and ending index end are given.
str1 = "this is string example....wow!!!"
str2 = "exam"

print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)

# str.endswith(suffix[, start[, end]])
# It returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.
str = "this is string example....wow!!!"

suffix = "wow!!!"
print str.endswith(suffix)
print str.endswith(suffix,20)

suffix = "is"
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

# str.startswith(str, beg=0,end=len(string));
# The method startswith() checks whether string starts with str, optionally restricting the matching with the given indices start and end.

str = "this is string example....wow!!!"
print str.startswith( 'this' )
print str.startswith( 'is', 2, 4 )
print str.startswith( 'this', 2, 4 )

# str.replace(old, new[, max])
# The method replace() returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.

str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

# str.split(str="", num=string.count(str)).
# The method split() returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.

str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str.split( )
print str.split(' ', 1 )

# ------------- STRING FUNCTIONS --------------------------
#
# split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
#
# join(seq)
# Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
#
# len(string)
# Returns the length of the string
#
# strip([chars])
# Performs both lstrip() and rstrip() on string.
#
# ----------------------------------------------------------
#
# find(str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
#
# rfind(str, beg=0,end=len(string))
# Same as find(), but search backwards in string.
#
# count(str, beg= 0,end=len(string))
# Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given
#
# index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.
#
# max(str)
# Returns the max alphabetical character from the string str.
#
# min(str)
# Returns the min alphabetical character from the string str.
#
# replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.
#
# ----------------------------------------------------------

