class Solution(object):
    arr = [1,4,2,5,3]

    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum_arr = 0
        len_arr = len(arr)
        i = 0
        j = 0
        pointer1 = 0
        pointer2 = 1
        p = not len_arr%2
        for n in range(len_arr -p):
            print(sum(arr[i + pointer1: j+  pointer2]))
            i +=1
            j+=2

        return 0
    sumOddLengthSubarrays(None,arr)

