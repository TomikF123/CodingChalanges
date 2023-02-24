
import math


class Solution(object):
    import math
    nums = [1,3,3,3]

    def numIdenticalPairs(self, nums):
        output = 0
        helpDict = dict.fromkeys(nums, 0)


        for n in nums:
            helpDict[n] += 1
        for key in helpDict:
            try:
                output+= (math.factorial(helpDict.get(key) ) ) /(2*( math.factorial(helpDict.get(key)-2 ) ) )
            except:
                None

        return int(output)


    print(numIdenticalPairs(None,nums))