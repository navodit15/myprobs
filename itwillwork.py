def test(arr):

    #n=int (input())
    arr=list(map(int,input().split( )))
    days=0
    l=len(arr)
    k=arr[0]
    i=0
    while k<l:
    
        k+=arr[i]
        i+=k
        days=days+1
    print(days)
T=int(input())
for i in range(0,T):
    n=int(input())
    test(n)
