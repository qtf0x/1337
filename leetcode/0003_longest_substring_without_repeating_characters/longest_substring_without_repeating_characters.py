"""
@author  Aster Marias <aster@bitangent.org>
@date    10/28/2025

@brief   Given a string s, find the length of the longest without duplicate
         characters.
@details <https://leetcode.com/problems/add-two-numbers/description/>
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # only need ASCII characters 32(' ') through 126 => 95 chars
        # each byte is a Boolean for if current window contains that char
        chars = bytearray(95)
        curr_len = 0
        max_len = 0

        i = 0
        # move second pointer from start to end
        for j in range(len(s)):
            # move first pointer forward until no repeat chars
            while chars[ord(s[j]) - 32]:
                chars[ord(s[i]) - 32] = 0
                curr_len -= 1
                i += 1

            # add next char and mark it in array
            chars[ord(s[j]) - 32] = 1
            curr_len += 1

            max_len = max(max_len, curr_len)

        return max_len
