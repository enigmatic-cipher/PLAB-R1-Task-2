"""
Given a list of size n as input. Create a new list containing all elements from input list except zero.
Print this new list along with its size.
Input-> [1,0,0,22]
Output-> 
New list size:2 
1 
22
"""

ls = [1,0,0,22]
ln = len(ls)
nw_ls = []
index = 0
for i in range(0,ln):
  e = ls[i]
  if (e==0):
    pass
  else:
    nw_ls += [e]
    index += 1
print(nw_ls)
print(f"New list size: {index}")
