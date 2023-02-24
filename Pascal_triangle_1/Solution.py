class Solution(object):
    n = 10
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        START_NUMBER =1
        END_NUMBER = START_NUMBER
        output = []
        while len(output) != numRows:
            for rows in range(numRows):
                row = []
                for nums in range(rows+1):
                    if nums == 0:
                        row.append(START_NUMBER)

                    if nums == rows:
                        if rows == 0:
                            break
                    else:
                        try:
                            number_to_append = output[rows - 1][nums] + output[rows - 1][nums + 1]
                        except:
                            number_to_append = output[rows - 1][nums]

                        row.append(number_to_append)

                output.append(row)
        return output

