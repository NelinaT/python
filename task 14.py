
def collatz(n):
    if n%2==0:
        n =n//2 
    else:
        n =3*n + 1 
    return n 
count=1
numy=0
for i in range(1,1000000):
    n=i
    
    count1=0
    while n!=1:
        number=collatz(n)
        
        n=number
        count1+=1

    if count<count1:
        numy=i
        count=count1
print(numy)    