# nums=[1,2,3,4]
# result=map(lambda x:x*2,nums)
# print(list(result))

# a=[1,2,3]
# b=[4,5,6]

# result=map(lambda x,y:x+y,a,b)
# print(list(result))

# num=[1,2,3,4]
# result=filter(lambda x:x%2==0,num)

# word=["apple","","banan","","cherry"]
# nonempty=filter(lambda x:x!="",word)
# print(list(nonempty))

# num=[1,2,3,4,5]
# Squared_evens=map(lambda x:x**2, filter(lambda x:x%2==0,num))
# print(list(Squared_evens))

from functools import reduce
num=[1,2,3,4]
result=reduce(lambda x,y:x+y,num)
print(result)

