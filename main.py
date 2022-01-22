"""
Given n as input, print the following pattern.
Input = 8
Output: MNOMNOMN
"""

n = 8
pt = "M"
pt2 = "N"
pt3 = "O"
st = ""
for i in range(0,n):
  st += (pt, pt2, pt3)[i%3]
print(st)
