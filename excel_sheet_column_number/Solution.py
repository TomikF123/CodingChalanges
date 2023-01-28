import math

ColumnNumber = 708
columnStr  = math.floor(ColumnNumber/26)
columnStr2 = ColumnNumber%26

print(columnStr)
print(columnStr2)

for i in range(columnStr):
