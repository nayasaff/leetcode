def lengthOfLongestSubstring( s):
    queue = []
    longestSubstring = 0
    for index in range(0, len(s)) :
        if s[index] in queue :
            while(queue[0] != s[index]) :
                queue.pop(0)
            queue.pop(0)

        queue.append(s[index])

        if len(queue) > longestSubstring :
            longestSubstring = len(queue)

    return longestSubstring

def myAtoi(s) :
    result = ""
    for i in s :
        
        if i == " "  and len(result) == 0:
            continue

        elif (i == "-" or i == "+") and len(result) == 0 :
            result += i
        elif i in "0123456789" :
            result += i
        else :
            break
    
    if len(result) == 0 or result == "-" or result == "+" :
        return 0
    
    sign = None
    if result[0] in "+-" :
        sign = result[0]

        result = result[1:]
    result = - int(result) if sign == "-" else int(result)

    MIN_INT, MAX_INT = -2**31 ,(2**31) - 1

    if result > MAX_INT :
        return MAX_INT

    if result < MIN_INT :
        return MIN_INT

    return result    
"""
1. Initialize two pointers left and right
2. Two scenarios palindrome is odd (aba) or even (baab)
3. Scenario odd : Iterate pointers around b and store longest palindrome
4. Scenario even : Pointer a first a character, pointer at second b character and iterate ponters to store longest palindrome
Time complexity : O(N^2)
"""
def longestPalindromeSubstring(self, s):

        right_pointer = 0
        left_pointer = 0
        longest_palindrome = s[0]
        for i in range(0, len(s)) :
            left_pointer = i -1
            right_pointer = i +1

            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]  :
                new_length = (right_pointer - left_pointer) +1
                if(new_length > len(longest_palindrome)) :
                    longest_palindrome = s[left_pointer : right_pointer +1]   
                left_pointer -=1
                right_pointer +=1

            left_pointer = i
            right_pointer = i + 1
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]  :
                new_length = (right_pointer - left_pointer) +1
                if(new_length > len(longest_palindrome)) :
                    longest_palindrome = s[left_pointer : right_pointer +1]

                
                left_pointer -=1
                right_pointer +=1

        return longest_palindrome