import decimal


class Solution(object):
    nums = [256,2,312,8,5,256,4]



    def singleNumber(self, nums): # TODO
        m = nums[0]
        for n in nums[1:]:

            temp = m
            m = int(bin(m),2) ^ int(bin(n), 2)
            print(m , "m")
            print(temp)






        """
        :type nums: List[int]
        :rtype: int
        """




    print(singleNumber(None,nums)," result ")