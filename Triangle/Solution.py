class Solution(object):
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    def minimumTotal(self, triangle):
        path_sum = triangle[0][0]
        index =0
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for rows in range(len(triangle)-1):
            path_sum += min(triangle[rows+1][index:index+2])
            if triangle[rows+1][index+1] < triangle[rows+1][index]:
                index+=1
        return path_sum
    print(minimumTotal(None,triangle))
