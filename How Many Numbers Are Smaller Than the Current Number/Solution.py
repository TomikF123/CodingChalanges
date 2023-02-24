class Solution(object):
    nums = [1,2,3,4]
    def smallerNumbersThanCurrent(self, nums):
        output = []
        sorted_nums = sorted(nums)
        for n in nums:
            output.append(sorted_nums.index(n))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return output
    print(smallerNumbersThanCurrent(None,nums))