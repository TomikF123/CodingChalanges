
class Solution(object):
    columnTitle = "ZY"
    def titleToNumber(self, columnNumber):
        output = 0
        """
        :type columnNumber: int
        :rtype: str
        """

        out =[]
        for n in columnNumber :
            out.append(ord(n.lower())-96)

        out.reverse()

        for i,n in enumerate(out):
            output +=(26**i)*n
        return output

