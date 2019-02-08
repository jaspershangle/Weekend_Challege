# Weekend Algorithm 

# Write a function that reverses a string without affecting special caracters
# "!!aPples_Ar3__Gr8!"
# "!!rG3rA_sel__pPa!

# Rules
# No built in methods

# Challenge
# Do this in Ruby
import re

def reverse_string_special(input_string):
    input_list = list(input_string)
    left = 0
    right = len(input_list) - 1 
    regex = '[a-zA-Z0-9]'
    while left < right:
        if bool(re.match(regex, input_list[left])) == False:
            left += 1
        elif bool(re.match(regex, input_list[right])) == False:
            right -= 1
        else:
            input_list[left], input_list[right] = input_list[right], input_list[left]
            left += 1
            right -= 1
    return "".join(input_list)

print(reverse_string_special('!!aPples_Ar3__Gr8!'))