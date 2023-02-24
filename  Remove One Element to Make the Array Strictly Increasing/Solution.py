class Solution(object):
    nums = [541,783,433,744]
    def canBeIncreasing(self, nums): #TODO
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp= []
        temp2 = 0
        temp3 = 0
        if len(nums) ==2:
            return True
        for n in range(len(nums)-1):
            if not nums[n]<nums[n+1]:
                temp.append(nums[n])
                temp2=nums[abs(n-1)]
                temp3 = nums[n+1]
                print(temp, temp2)
            if len(temp) > 1:
                return False
            if len(temp) ==1:
                if nums[n]<temp2 and nums[n]<temp3 or nums[n]<=temp2 and nums[n]<temp[0]:
                    print(nums[n],temp2)
                    return False







        return True
    print(canBeIncreasing(None,nums))

