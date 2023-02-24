class Solution(object):
    nums = [5,0,1,2,3,4]
    def buildArray(self, nums):
        output= []
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i,_ in enumerate(nums):
            numberToAppend =nums[nums[i]]
            output.append(numberToAppend)
        return output
    print(buildArray(None,nums))
