n=int(input())
for cc in range(n):
    word=input().strip()
    #ord() get the ascii value of a charcater
    number=sum(ord(i) for i in word)
    if not number&1:#checks if a number is even
        print("ENTER")
    else:
        print("SORRY")
        
    
