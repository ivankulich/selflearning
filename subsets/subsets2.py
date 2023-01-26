from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = list(set(nums))
        result = [[]]
        for i in range(len(nums)):
            for j in range(len(result)):
                tmp = result[j].copy()
                tmp.append(nums[i])
                result.append(tmp)
        return result

if __name__ == "__main__":
    #lst = [int(i) for i in input().split()]
    lst = [1, 2, 3, 3, 3]
    print(Solution().subsets(lst))