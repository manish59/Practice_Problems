'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.'''
class Solution:
    def maxSubArray(self, nums):
        max_sum=0
        i=1
        max_index=None
        while(i<=len(nums)):
            print(nums[:i],sum(nums[:i]))
            i=i+1
array=[-2,1,-3,4,-1,2,1,-5,4]
Solution().maxSubArray(array)