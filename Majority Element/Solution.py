class Solution(object):
    nums = [2,2,1,1,1,2,2]
    def majorityElement(self, nums):
        output = 0
        numss = sorted(nums[:])
        output = int(numss[len(nums)//2])
        return output
        """
        :type nums: List[int]
        :rtype: int
        """
    print(majorityElement(None,nums))


