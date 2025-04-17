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
    