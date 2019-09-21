#The is all about the ratio of positive, negative, zeros in the list
#
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(arr)
m=0
p=0
z=0
for i in arr:
    if(i<0):    #checks for negative
        m=m+1
    elif(i>0):    #checks for positive
        p=p+1
    else:       #checks for zero
        z=z+1
print('{:6f}'.format(m/len(arr))) #count of negative  divides by lengthe of the array
print('{:f}'.format(p/len(arr))) #count of positive  divides by lengthe of the array
print('{:f}'.format(z/len(arr))) #count of zoros  divides by lengthe of the array



output:
6
-4 3 -9 0 4 1 
[-4, 3, -9, 0, 4, 1]

0.333333
0.500000
0.166667
