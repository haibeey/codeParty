def getKMin(lis,k):
    assert k<len(lis)
    return lis[k-1]

def getKMax(lis,k):
    assert k<len(lis)
    return lis[len(lis)-k]

t=int(input())
for i in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    lis=[int(i) for i in input().split()]
    lis.sort()
    print(getKMin(lis,k),getKMax(lis,k))

