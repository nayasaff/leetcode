"""
Reverse int and check it is same as original input
1. Store remainder in revered_int 
2. Keep adding new remainder
"""

def isPalindrome( x: int) -> bool:
    if x < 0 :
        return False
    
    reversed_int = 0
    copied_int = x
    while x != 0 :

        remainder = x % 10

        reversed_int = reversed_int * 10 + remainder

        x = int(x / 10)
    
    return reversed_int == copied_int