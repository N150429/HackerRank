#concatenation of arrays using numpy
import numpy
N,M,P = map(int,input().split())
L1=numpy.array([input().split() for i in range(N)],int)
L2=numpy.array([input().split() for k in range(M)],int)
print(L1)
print(numpy.concatenate((L1,L2),axis=0))


output:
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
4 3
[[1 2]
 [1 2]
 [1 2]
 [1 2]]
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [4 3]]
#with using vstack and array

from numpy import array
from numpy import vstack
N,M,P = map(int,input().split())
L1=array([input().split() for i in range(N)],int)
L2=array([input().split() for k in range(M)],int)
print(vstack((L1,L2)))

output:
1 2 2
1 2
3 4
5 4
[[1 2]
 [3 4]
 [5 4]]
