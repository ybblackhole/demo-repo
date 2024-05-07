import sys
def Tim(A,a,k,x):
  
  l,r=0,a-1

  if A[0][0] > x:
    l, r = 0, -1
  elif A[0][a-1] < x:
    l, r = a, a-1

  while(l<=r):
    m=int(l+(r-l)/2)
    if A[0][m]==x :
      l,r=m+1,m
      break
    elif A[0][m]<x:  l=m+1
    else: r=m-1

  result=[]
  i,j=l,r

  while(len(result)<k):
    if i > a-1 :
      result.append(A[0][j])
      j=j-1
    elif j < 0:
      result.append(A[0][i])
      i=i+1
    elif abs(A[0][j]-x) <= abs(A[0][i]-x):
      result.append(A[0][j])
      j=j-1
    else:
      result.append(A[0][i])
      i=i+1

  return result

A=[]
a=int(sys.stdin.readline())
A.append([int(x) for x in sys.stdin.readline().split()])
k,x=map(int,sys.stdin.readline().split())
m=[]
m=Tim(A,a,k,x)
m.sort()
for i in range (len(m)):
  print(m[i],end=" ")