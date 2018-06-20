def reverseWord(word):
    word=[word[i] for i in range(len(word)-1,-1,-1)]
    return "".join(word)
n=int(input().strip())
for cc in range(n):
    sentence=input().split()
    sentence=[sentence[i] for i in range(len(sentence)-1,-1,-1)]
    sentence=[reverseWord(i) for i in sentence]
    print(*sentence)


