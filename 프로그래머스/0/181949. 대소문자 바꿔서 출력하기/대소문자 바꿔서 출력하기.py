str = input()
answer=''
for i in str:
    if i.islower():
        i=i.upper()
        answer+=i    
    else:
        i=i.lower()
        answer+=i   
print(answer)