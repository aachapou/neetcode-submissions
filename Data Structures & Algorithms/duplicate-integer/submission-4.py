class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr =[0]* len(nums)
        count =0
        for i in range(len(nums)):
            arr[i] =nums[i]
        for i in range(len(nums)):

            for k in range(len(nums)):
                if(nums[i]==arr[k] and k != i):
                    return True
                
        return False
