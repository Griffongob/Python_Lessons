################################################
#          What We've Seen About Strings       #
################################################

# Fact_01: Python Represents a String using double quotes
print "Hello World"

# Fact_02: You don't need to declare a string variable
variable = "Hello World"
print variable

# Fact_03: You can concatenate two separate strings together usign the '+'
variable_one = "This is just the beginning "
variable_two = "of the journey to learning programming"

variable_three = variable_one + variable_two
print variable_three

# Fact_04: You can escape certain characters
print "This is\n and example of escaping \r\""

################################################
#                TELL ME MORE!!!               #
################################################

# Fact_05: Strings have indices

statement = "EXCitEment"
print statement[0]
print statement[4]
print statement[6:]

# Fact_06: Python has convenience methods that every string can access
print statement.index("X")

# Careful with .index, it ony returns the first instance of a character
print statement.index("E")

# .rindex will start searching from right to left
print statement.rindex("t")

print statement[:statement.index("m")]

# Replace is a powerful methods

print statement.replace("ment", "ful")
print statement.replace("h", "test")

example = "If,this,is,broke,up"
print statement.split(",")

# Uppercase / Lowercase

print statement.uppercase()
print statement.lowercase()

# You can easily remove leading and trailing spaces
spaced_statement = "             this is to the point                "
print spaced_statement.lstrip()
print spaced_statement.rstrip()
print spaced_statement.strip()
