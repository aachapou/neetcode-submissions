class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            hash_map[n] = i

        for i, n in enumerate(nums):
            y = target - n

            if y in hash_map and hash_map[y] != i:

                return[i, hash_map[y]]
        
        return []
