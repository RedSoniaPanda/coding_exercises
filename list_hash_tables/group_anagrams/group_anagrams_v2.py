# I want to use Jason's solution and create my own as well
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_anagrams = defaultdict(list)  # Default dict allows for me to set the ascii as a key
        for word in strs:
            key = [0] * 26  # Create a list of 0's, representing 26 letters in the alphabet
            # Iterate through the characters
            for char in word:
                # get the ascii version of the character in the word
                key[ord(char) - ord("a")] += 1
            final_anagrams[tuple(key)].append(word)
        all_anagrams = [sorted(anagram) for anagram in final_anagrams.values()]
        return all_anagrams


if __name__ == "__main__":
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    sol = Solution()
    output = sol.groupAnagrams(test_input)

    cnt = 0
    for expected in expected_output:
        is_in_expected = False
        for actual in output:
            if expected == actual:
                is_in_expected = True
                break
        if is_in_expected:
            cnt += 1
    if cnt == len(expected_output):
        print("Success")
    else:
        print("Fail")
