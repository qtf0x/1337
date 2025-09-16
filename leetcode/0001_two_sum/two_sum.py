"""
@author  Aster Marias <aster@bitangent.org>
@date    09/15/2025

@brief   Given an array of integers `nums` and an integer `target`, return
         indices of the two numbers such that they add up to `target`. You
         may assume that each input would have exactly one solution, and you
         may not use the same element twice. You can return the answer in any
         order.
@details <https://leetcode.com/problems/two-sum/description/>
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, seen[complement]]
            seen[num] = i
