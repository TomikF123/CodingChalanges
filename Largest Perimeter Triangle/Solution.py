class Solution(object):
        nums = [2,1,2]

        def largestPerimeter(self, nums):

            nums = sorted(nums, reverse=True)
            print(nums)
            left = 0
            middle = 1
            right = 2
            len_nums = len(nums)
            while right != len_nums:
                if nums[right] + nums[middle] > nums[left]:
                    return nums[right] + nums[middle] + nums[left]
                else:
                    print(nums[left], nums[middle], nums[right], "?")
                    left += 1
                    middle += 1
                    right += 1
            return 0
        arr = [1,3,2]
        arr.sort(reverse=True)
        print(arr)



