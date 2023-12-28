def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sum = nums[i]+nums[i+1]
            if sum == target:
                return [i,i+1]
            
twoSum([2,7,3,5,7], 9)