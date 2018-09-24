import sys
import os

# To make 'utils' module available here
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from helper_functions.utils import timeit
        
@timeit
def check_anagram(string1, string2):
    '''
        This function will check if string1 is anagram of string2.
        One string is an anagram of another if the second is simply a rearrangement of the first.
        For example, 'heart' and 'earth' are anagrams.

        For demonstration purposes the time complexity of this algorithm is :O(n^2).
        Assume the length of the two strings is equal

        :params string1: First string
        :params string2: Second String
        :return: True if string1 and string2 are anagrams of each other, else False
    '''
    my_list = list(string2)
    pos_ = 0
    check_if_match = True
    while pos_ < len(string1) and check_if_match:
        pos_inner = 0
        found = False
        while pos_inner < len(string2) and not found:
            if string1[pos_] == my_list[pos_inner]:
                found = True
            else:
                pos_inner += 1

        if found:
            my_list[pos_inner] = None
        else:
            check_if_match = False

        pos_ += 1

    return check_if_match

@timeit
def check_anagram_by_count(string1, string2):
    '''
        In order to decide whether two strings are anagrams, we will first count the number of
        times each character occurs. Since there are 26 possible characters, we can use a list of
        26 counters, one for each possible character.

        Time complexity of this method is: O(n)
    '''
    list_one = [0] * 26
    list_two = [0] * 26

    # Calculate the position of the alphabet and increment that index
    # For example, if we have character 'b' then we will increment index 1 (array starts at 0 ;) )
    for i in range(len(string1)):
        pos = ord(string1[i]) - ord('a')
        list_one[pos] += 1

    for i in range(len(string2)):
        pos = ord(string2[i]) - ord('a')
        list_two[pos] += 1

    # Check if both lists contain same number of each characters
    return list_one == list_two

if __name__ == '__main__':
    # slight time difference
    print(check_anagram('heart', 'earth'))
    print(check_anagram_by_count('heart', 'earth'))

    # better time difference
    print(check_anagram('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'))
    print(check_anagram_by_count('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'))