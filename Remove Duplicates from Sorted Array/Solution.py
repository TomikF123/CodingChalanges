import Triangle.Solution


class Solution(object):
    nums= [1,1,2]
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        help_dict = dict.fromkeys(nums)

        l = list(help_dict.keys())
        nums.extend(l)

        print(nums)
        return len(l)

    print(removeDuplicates(None,nums))


