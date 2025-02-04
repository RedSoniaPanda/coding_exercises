[Problem Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

# Constraints

 - 0 <= s.length <= 5 * 104
 - s consists of English letters, digits, symbols and spaces.

# Intuition

 - if a letter's not unique, then stop the string collection, collect the length and compare with max length to see if it's the longest substring
 - substring is continuous, so pwke is not a valid substring of pwwke
 - window size will be variable, because it depends on the uniqueness of the input string
 - _if input is an empty string, just return 0_
 - _if input is size 1 string, return 1_
 - for char in str -> outer loop
 - Input is not continuous - be careful of boundaries w/window size
 - I know that if I start from the beginning and find the first dupe character, then I've found the first max length
   - Save index of the first dupe character
   - Set the new start point at that index
   - start the next check at the first dupe char
 - USE THE INDEX TO CALCULATE THE SIZE OF THE SUBSTRING!!!!