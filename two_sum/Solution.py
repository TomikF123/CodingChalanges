class Solution(object):
    nums = [3,3]
    target = 6

    def twoSum(self,nums, target):
        for f in nums:
            nums.index(f) ==0
            if (target - f) in nums:
                return(nums.index(f),nums.index((target - f) ))
                break


    print(twoSum(None,nums,target))


