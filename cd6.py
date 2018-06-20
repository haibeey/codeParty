from collections import Counter
import sys

n=int(input())
for cc in range(n):
    word=input().strip()
    counter=Counter([i for i in word])
    size=-sys.maxsize;alphabeth=None
    for _alphabeth in counter:
        if counter[_alphabeth]>size:
            alphabeth=_alphabeth
            size=counter[_alphabeth]
        elif counter[_alphabeth]==size:
            alphabeth=None
    print(alphabeth)
    
    
    
