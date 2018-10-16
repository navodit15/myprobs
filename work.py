### ONLY_WORKING_COMBINATION ###
a=[]
days=0
a=list(map(int,input().split( )))
t=0
l=len(a)
sum=0
k=a[0]+(l-1)
l=a[0]
while t<k:
    t=l*2
    l=l*2
    days+=1
print(days)
