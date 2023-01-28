class Solution(object):
    s = "MCMXCVII"

    def romanToInt(self, s):
        numbers = []
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000, }

        s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        for item in s:
            numbers.append(roman_dict[item])

        return sum(numbers)

    print(romanToInt(None,s))
                
            