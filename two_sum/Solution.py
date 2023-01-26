class Solution(object):
    nums = [4,2,3,5]
    target = 8
    print(nums[nums.index(2):].count(3))
#todo : doesn't work when target is n and there is an n/2 element in the list
    def twoSum(self,nums, target):
        for f in nums:
            if (target - f) in nums and nums[nums.index(f):].count(f)<2:
                return(nums.index(f),nums.index((target - f) ))
                break


    print(twoSum(None,nums,target))


