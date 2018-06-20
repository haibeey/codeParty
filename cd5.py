def calculateTime(string):
    s=string[1:]
    ans=0
    for i in s:
        if i=="L":
            ans+=12
        elif i=="S":
            ans+=5
        else:
            ans+=int(i)
    return ans
n=int(input())
for bus in range(n):
    a=input().split()
    b=input().split()

    a=calculateTime(a)
    b=calculateTime(b)

    if a>b:
        print("A")
    elif b>a:
        print("B")
    else:
        print("both bus reached  at same time")

    
