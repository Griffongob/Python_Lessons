import math
##########################################
#         Numbers - Basics               #
##########################################

# Fact_01 - There are many types of numbers

# Example - Integer

integer_one = 10
print integer_one
print type(integer_one)

# Example - Float
float_one = 231.43
print float_one
print type(float_one)

# Example - Long
big_number_one = 946563903756392048565840284659302845593756978354948565948369475658573956483846584654856430240234822304824825723423014324692383402304748727641298923482234627234239823982394827348230934392436945234853279423804972342323984238743742543932602347947290413857492337689942303874672423764287398249238467392823874234
print big_number_one
print type(big_number_one)

# Exampe
float_two = 45.209380219310283123120238018308947983475693426984543687324699804798543897652387534208457956982307587698347432653478998439476354903457348763498342598757834579045834709245942709128037436470982378239403128234723401238371879872450895867087408758974270942472389238704723842398047239462378
print float_two
print type(float_two)

# We'll get back to the challenge of floats later

# Fact_02 - You can use numbers to do MATH! =)

print 1+1           #       Addition
print 10/2          #       Division
print 2*3           #       Multiplication
print 7%2           #       Modulus
print 10**2         #       Exponent
print abs(10.7)     #       Absolute Value
print math.sqrt(100)#       Square Root

# Fact_03 - Sometimes Python gives you results you do not expect
print 3/2 # ==> What do you expect will happen?
print 3.0/2.0 #==> Now what do you expect will happen?
print 3.0//2.0 # (floor divison)
print 4.0 * 2 #==> What do you expect will happen?
print 4.0 / 2 #==> What do you expect will happen?