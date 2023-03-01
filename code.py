class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        m=0
        for i in range(n-1):
            m=max(m,abs(nums[i]-nums[i+1]))
        return m
'''
Time complexity:
best: O(N)
wrost: O(NlogN)
Space complexity:
O(1)    
'''
