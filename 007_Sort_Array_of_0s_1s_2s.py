class Solution:
    def sort012(self,arr,n):
        i=0
        count0=0
        count1=0
        count2=0
        sorted_arr=[]
        
        while(i<n):
            if(arr[i]==0):
                count0+=1
            elif (arr[i]==1):
                count1+=1
            elif(arr[i]==2):
                count2+=1
            i=i+1
        
        j=0
        while(count0>0):
            arr[j]=0
            count0-=1
            j+=1
        while(count1>0):
            arr[j]=1
            count1-=1
            j+=1
        while(count2>0):
            arr[j]=2
            count2-=1
            j+=1
        return arr
        
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
