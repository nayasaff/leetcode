from collections import defaultdict

"""
If interviews are concatenation of n time, 
for i in range(n) :
    for n in nums :
        result.append(n)
Which will be O(n*k) => O(n)       
"""
def concatenation_of_array(nums : list[int]) -> list[int] :
    length = len(nums)
    result = []
    for i in range(len(nums)) :
        result.insert(i, nums[i])
        result.insert(i + length, nums[i])
    return result



"""
Alternative use set instead of dict. 
set is unique items {item1, item2, item3} while dict is key value pair {key1: value1, key2: value2}
in memory set uses less than dict.
"""
def contains_duplication(nums : list[int]) -> bool :
    hash_map = {}

    for n in nums : 
        if hash_map.get(n) :
            return True

        hash_map[n] = True

    return False

"""
Alternative sort two strings o(nlogn) and compare two strings. space is o(1)
"""
def valid_anagram(s : str, t : str) -> bool :
    if len(s) != len(t) :
        return False

    hash_map = {}

    for i in range(len(s)) :
        hash_map[s[i]] = hash_map.get(s[i], 0) + 1
        hash_map[t[i]] = hash_map.get(t[i], 0) - 1

    for value in hash_map.values() :
        if value != 0 :
            return False

    return True


def two_sum(nums : list[int], target : int) -> list[int] :
    hash_map = {}

    for i in range(len(nums)) : 

        remaining =  target - nums[i]

        if hash_map.get(remaining) is not None :
            return [hash_map.get(remaining), i]

        hash_map[nums[i]] = i


"""
time complexity o (n* m) where m is minimum length of string
"""
def longest_common_prefix(strs : list[str]) -> str :

    if(len(strs) == 0 ) : return ''

    prefix : str = ''
    first_element = strs[0]

    for i in range(len(first_element)) : 
        for s in strs :
            if len(s) <= i :
                return prefix

            if first_element[i] != s[i] :
                return prefix

        prefix += first_element[i]

    return prefix


def group_anagrams(strs: list[str]) -> list[list[str]]:

    hash_set = {}
    result : list[list[str]] = []

    for s in strs :

        sorted_str =  "".join(sorted(s)) 

        if hash_set.get(sorted_str ) is not None : 

            hash_set[sorted_str].append(s)
        else : 
            hash_set[sorted_str] = [s]

    
    for val in hash_set.values() : 
        result.append(val)

    return result

        
