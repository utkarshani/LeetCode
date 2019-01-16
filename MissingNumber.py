#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#Example 1:
#Input: [3,0,1]
#Output: 2

#Example 2:
#Input: [9,6,4,2,3,5,7,0,1]
#Output: 8

#Note:
#Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

#Runtime: 52 ms
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #converting the list into set
        #Set is an unordered collection of unique items
        num_set = set(nums)
        #get the length of the set
        n = len(nums) + 1
        #since the list starts from 0 to n and range starts from 0 to n-1 we did n = (len + 1)
        for number in range(n):
            if number not in num_set:
                return number

            
