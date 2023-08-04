'''
Given a string s, find the length of the longest 
substring without repeating characters. 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

 '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max_count = 0
        for i in range(len(s)):
            l = []
            for j in range(i,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                else:
                    break
            if max_count < len(l):
                max_count = len(l)
        return max_count
