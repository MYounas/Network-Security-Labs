from copy import deepcopy


a=[[1,6],2,3]
# a=[1,2,3]

b=deepcopy(a)

a[0]=0

print(b)
