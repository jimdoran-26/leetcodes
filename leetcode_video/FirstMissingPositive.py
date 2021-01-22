class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        #print(N)
        
        temp = [False]*N
        #print(temp)
        
        for i in nums:
            if 1<= i <= N:
                temp[i-1]=True
        
        for i in range(N):
            if temp[i] == False:
                return i+1
        
        return N+1

a = Solution()
print(a.firstMissingPositive([1,2,3,4]))
print(a.firstMissingPositive([7,8,9,11,12]))
print(a.firstMissingPositive([3,4,-1,1]))
