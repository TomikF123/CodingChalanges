class Solution(object):
    celsius = 36.50
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [Kelvin,Fahrenheit]
    print(convertTemperature(None,celsius))