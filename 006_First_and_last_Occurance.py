#User function Template for python3
def find(arr,n,x):
    # code here
    l1=[]
    count=0
    flag=0
    for i in range(0,n):
        if (arr[i]==x):
            l1.append(i)
            count+=1
            flag+=1
 
    if (flag>0):
        return l1[0],l1[count-1]
    else:
        return -1,-1
    
#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends
