class Solution(object):
    nums1 = [25, 29, 10, 6]
    nums2 = [17, 11, 5, 1, 1, 24, 11, 1, 27]
    #TODO
    def xorAllNums(self, nums1, nums2):
        output = 0
        n = nums1[0]
        m = nums2[0]
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums2 == len_nums1 or (len_nums1 and (not (len_nums1 & (len_nums1 - 1)))) and (
                len_nums2 and (not (len_nums2 & (len_nums2 - 1)))):
            return 0
        nums1_xor_nums2 = []
        if len_nums2>len_nums1:
             for j in nums2:
                nums1_xor_nums2.append(int(bin(n),2)^int(bin(j),2))
             for a in nums1_xor_nums2:
                output^=int(bin(a),2)
        else:
            for j in nums1:
                nums1_xor_nums2.append(int(bin(m), 2) ^ int(bin(j), 2))
            for a in nums1_xor_nums2:
                output ^= int(bin(a), 2)


        return output
    print(xorAllNums(None,nums1,nums2))