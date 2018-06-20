
t=int(input())
for i in range(t):
    k=int(input())
    string=""
    for line in range(k):
        l="".join(input().split())
        for number in l:
            if number=="1" or number=="0":
                string+=number
    print(int(string,base=2))
