#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        list1=list(a)
        list2=list(b)
        list1.sort()
        list2.sort()
        
        str1=str(list1)
        str2=str(list2)
        if (len(a)==len(b)):
            if (str1==str2):
                return True
            else:
                return False
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
