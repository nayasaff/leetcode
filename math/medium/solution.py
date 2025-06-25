"""
1. Get last digit of number (Take care of negative)
2. Add remainder to new value 
"""

def reverse( x):

    result = None

    divided_by = 10 if x > 0 else -10
    while x != 0 :
        if(not (x >= -2**31 and x <= 2**31 -1 )) :
            return 0
        remainder = x % divided_by
        print("here")
        if(result is None) :
            result = remainder
        else :
            result = (result * 10) + remainder

        x = int(x / 10)
    return result

print(reverse(-123))