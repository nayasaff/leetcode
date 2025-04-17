import pytest
from strings.medium.solution import *

def test_lengthOfLongestSubstring() :

    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3

def test_myAtoi() :

    assert myAtoi("42") == 42
    assert myAtoi("   -42") == -42
    assert myAtoi("1337c0d3") == 1337
    assert myAtoi("words and 987") == 0
    assert myAtoi("0_1") == 0
    assert myAtoi("-91283472332") == -2147483648
    assert myAtoi("+-12") == 0


