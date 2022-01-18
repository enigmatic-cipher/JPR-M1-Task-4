"""
Given n as input, print the following pattern.
Input = 4
Output: MNOM
"""

n = 4
p1 = "M"
p2 = "N"
p3 = "O"
st = ""
for i in range(1,n+1):
  if(i%1!=0):
    st = st + p1
  elif(i%2==0):
    st = st + p2
  elif(i%3==0):
    st = st + p3
print(st)
