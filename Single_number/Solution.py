import decimal


class Solution(object):
    nums = [2,2,10,4,4]



    def singleNumber(self, nums):
        m = nums[0]
        for n in nums[1:]:

            m = int(bin(m),2) ^ int(bin(n), 2)
        return m




        """
        :type nums: List[int]
        :rtype: int
        """




    print(singleNumber(None,nums))