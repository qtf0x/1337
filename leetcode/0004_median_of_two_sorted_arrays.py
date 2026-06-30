"""
@author  Aster Marias <aster@bitangent.org>
@date    10/29/2025

@brief   Given two sorted arrays nums1 and nums2 of size m and n respectively,
         return the median of the two sorted arrays. The overall run time
         complexity should be O(log (m+n)).
@details <https://leetcode.com/problems/median-of-two-sorted-arrays/description/>
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mn = len(nums1) + len(nums2)

        i, j, k = 0, 0, 0
        while k < mn / 2 - 1:
            if i < len(nums1) - 1 and nums1[i] < nums2[j]:
                i += 1
            elif j < len(nums2) - 1:
                j += 1
            k += 1

        first, second = nums1[i], nums2[j]
        if mn % 2:
            return min(first, second)
        else:
            return (first + second) / 2
