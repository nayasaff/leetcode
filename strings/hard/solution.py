from collections import defaultdict
import math


def minWindowSubstring( s, t):
    
    map_dict = defaultdict(int)
    for index in t :
        map_dict[index] += 1

    l = 0
    r = 0
    minimum_substring = ""
    increment_r = True
    while l < len(s) and r < len(s) :

        if map_dict.get(s[r]) is not None:
            map_dict[s[r]] -=1

            for value in map_dict.values():
                if value > 0 :
                    increment_r = False
                    break
        
        if not increment_r :
            substring = s[l : r + 1]
            minimum_substring = substring if substring < minimum_substring or minimum_substring != "" else minimum_substring

            if map_dict.get(s[l]) is not None :
                map_dict[s[l]] += 1
            
            l +=1
        
        if increment_r :
            r+=1


        is_substring_equals = True
        for value in map_dict.values():
            if value > 0 :
                is_substring_equals = False
                break

        if is_substring_equals :
            if map_dict.get(s[l]) is not None :
                map_dict[s[l]] += 1

            substring = s[l : r + 1]
            print("substring ", substring)
            print("map ", map_dict)
            minimum_substring = substring if substring < minimum_substring or minimum_substring != "" else minimum_substring


            l +=1
        else :
            r+=1

    return minimum_substring

print(minWindowSubstring("ADOBECODEBANC", "ABC")) # BANC 

# letterDict to store the frequency of each character in t.
# currLetterDict to keep track of the frequency of characters in the current window of s.
# left pointer to denote the start of the window.
# minLen to store the length of the minimum window found.
# retLeft and retRight to store the starting and ending indices of the minimum window.
# count to keep track of how many characters in the current window match the required frequency in t.
# Populate letterDict with the frequency of each character in t.

# Iterate Through s using the right pointer:

# Add the character at right to the current window.
# Update currLetterDict with the frequency of the current character.
# If the current character's frequency matches its required frequency in t, increment count.
# Shrink the Window from the left:

# When count equals the number of unique characters in t (i.e., the current window contains all characters of t in the required frequency), check if this window is smaller than the previously found minimum window.
# If it is, update minLen, retLeft, and retRight.
# Then, try to shrink the window by moving the left pointer to the right, updating currLetterDict and count accordingly.
# Return the Result:

# If a valid window is found, return the substring using retLeft and retRight.
# If no valid window is found, return an empty string.