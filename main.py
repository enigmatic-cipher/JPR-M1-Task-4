"""
Given n as input, print the following pattern.
Input = 8
Output: MNOMNOMN
"""

n = 8
p1 = "M"
p2 = "N"
p3 = "O"
st = ""
index = 0
for i in range(1,n+1):
  st = st + p1
  st = st + p2
  st = st + p3
  index = index + 1
print(st)
