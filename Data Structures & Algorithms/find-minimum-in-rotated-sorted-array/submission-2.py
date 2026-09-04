class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search is needed since it is O(log n) runtime
        # How do I change the middle area for binary search since it needs that point

        # I need two pointers and a mid value that determine the bounds for the search, the middle should be positionally (right // 2)

        final = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:

            # First check if the array is sorted entirely
            if nums[left] < nums[right]:
                final = min(final, nums[left])
                break

            mid = (right + left) // 2
            final = min(final, nums[mid])

            # If this is true it means the the min element will be in the right part
            if nums[left] <= nums[mid]:
                left = mid + 1
                mid = (right + left) // 2
            
            # If it gets to this, the min element must be in the left part then
            else:
                right = mid - 1
                mid = (right + left) // 2
        
        return final

            