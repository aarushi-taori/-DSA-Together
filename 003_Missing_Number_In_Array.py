#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        natural=0
        sum1=0
        diff=0
        for i in range(1,n+1):
            natural+=i
        for j in range(0,len(array)):
            sum1+=array[j]
        diff=natural-sum1
        return diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
