# Count the number of characters in each word
from typing import List, Dict


def get_word_character_count(word: str) -> dict[str, int]:
    charac_cnt = {}
    for charac in word:
        if charac not in charac_cnt.keys():
            charac_cnt[charac] = 1
        else:
            charac_cnt[charac] += 1
    return charac_cnt


def word_count(w: List[str]) -> Dict[str, int]:
    word_cnt = {}
    for word in w:
        if word not in word_cnt.keys():
            word_cnt[word] = 1
        else:
            word_cnt[word] += 1
    return word_cnt


def do_add_word_list_to_final(
    all_words: List[List[str]],
    new_words: List[str]
) -> bool:
    for w in all_words:
        w_word_cnt = word_count(w)
        new_words_cnt = word_count(new_words)
        if w_word_cnt == new_words_cnt:
            return False
    return True


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        words_checked = []
        word_index = 0
        for word in strs:
            charac_cnt = get_word_character_count(word)
            iter_list = []
            iter_index = 0
            for iter_word in strs:
                if word not in iter_list:
                    iter_list.append(word)
                if iter_index != word_index and len(word) == len(iter_word):
                    iter_letter_cnt = get_word_character_count(iter_word)
                    if iter_letter_cnt == charac_cnt:
                        iter_list.append(iter_word)
                iter_index += 1
            words_checked.append(word)
            if do_add_word_list_to_final(anagrams, iter_list):
                anagrams.append(sorted(iter_list))
            word_index += 1
        return anagrams


def main(test_input: List[str]) -> None:
    pass


if __name__ == "__main__":
    # Expected and input
    # test_inputs = [([["bat"],["nat","tan"],["ate","eat","tea"]], ["eat","tea","tan","ate","nat","bat"])]
    # for test in test_inputs:
    #     main(test)
    # test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # sol = Solution()
    # print(sol.groupAnagrams(test_input))
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    sol = Solution()
    output = sol.groupAnagrams(test_input)
    print(expected_output)

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