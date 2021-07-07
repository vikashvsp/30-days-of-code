n=int(input())
numb=bin(n)
maximum=0
current =0
for i in numb:
    if i=='1':
        current+=1
    else: 
        maximum=max(maximum,current)
        current=0
print(max(maximum,current))