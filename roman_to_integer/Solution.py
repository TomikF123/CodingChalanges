class Solution(object):
    s = "ILV"
    def romanToInt(self, s):
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
        l = len(s)

        for item in s:

            if roman_dict.get(s[l-1]) > roman_dict.get(s[l-2]):
                a =roman_dict.get(s[l-1]) - roman_dict.get(s[l-2])

            else:
                a = roman_dict.get(s[l - 1]) + roman_dict.get(s[l - 2])


        return a





    print(romanToInt(None,s))
                
            