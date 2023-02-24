class Solution(object):
    x = 3
    y = 4
    points = [[2,3]]
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        output = [-1,-1]
        for i, n in enumerate(points):
            if x == points[i][0] or y== points[i][1]:
                temp = abs( x - points[i][0]) + abs(y - points[i][1])
                if output[0]== -1 or temp <output[0]:
                    output[0] = temp
                    output[1] = i
        return output[1]
    x = nearestValidPoint(None,x,y,points)
    print(x)