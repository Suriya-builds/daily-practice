# Running Sum of 1d Array (Easy)
# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List, Optional

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0          # a number to start from
        result = [ ]       # an empty list
        for m in nums:
            total = total + m
            result.append(total)# save the current total into result (Step 3!)
        return result