class Solution(object):
    rowIndex=1

    def getRow(self, rowIndex):
        rowIndexes = rowIndex + 1

        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        START_NUMBER =1
        END_NUMBER = START_NUMBER
        output = []
        while len(output) != rowIndexes:
            for rows in range(rowIndexes):
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
        return output[rowIndex]

    print(getRow(None,rowIndex))