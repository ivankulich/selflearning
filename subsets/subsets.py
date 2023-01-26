"""
Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

https://leetcode.com/problems/subsets/description/
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = list(set(nums))
        result = []
        for i in range(2**len(lst), 2**(len(lst) + 1)):
            mask = bin(i)[3:]
            result.append([lst[j] for j in range(len(lst)) if mask[j] == '1'])
        return result

if __name__ == "__main__":
    #lst = [int(i) for i in input().split()]
    lst = [1, 2, 3, 3, 3, 6, 456]
    print(Solution().subsets(lst))