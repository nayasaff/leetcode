
from solution import *


def test_concatenation_of_array() :
    nums = [1, 2, 3]
    result = concatenation_of_array(nums)
    assert result == [1, 2, 3, 1, 2, 3]

    nums2 = [1,3,2,1]
    result2 = concatenation_of_array(nums2)
    assert result2 == [1,3,2,1,1,3,2,1]

def test_contains_duplication() :
    nums = [1, 2, 3, 3]
    result = contains_duplication(nums)
    assert result == True

    nums2 = [1, 2, 3, 4]
    result2 = contains_duplication(nums2)
    assert result2 == False

def test_valid_anagram() :
    s = "anagram"
    t = "nagaram"
    result = valid_anagram(s, t)
    assert result == True

    s2 = "rat"
    t2 = "car"
    result2 = valid_anagram(s2, t2)
    assert result2 == False

def test_two_sum() :
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)

    assert result == [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    assert result2 == [1, 2]

    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    assert result3 == [0, 1]

def test_longest_common_prefix() :
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_group_anagrams():
  normalize = lambda groups: sorted(sorted(group) for group in groups)

  result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

  assert normalize(result) == normalize([
      ["eat", "tea", "ate"],
      ["tan", "nat"],
      ["bat"],
  ])

  assert group_anagrams([""]) == [['']]
  assert group_anagrams(["a"]) == [["a"]]




if __name__ == "__main__":
    test_concatenation_of_array()
    test_contains_duplication()
    test_valid_anagram()
    test_two_sum()
    test_longest_common_prefix()
    test_group_anagrams()