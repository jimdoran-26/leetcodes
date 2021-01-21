class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        
        for i in range(len(nums)):
            #print(i)
            try:
                runningSum.append(nums[i]+runningSum[i-1])
            except:
                runningSum.append(nums[i])
                
        return runningSum

a = Solution()
print(a.runningSum([1,2,3,4]))
print(a.runningSum([3,4,6,16,17]))
