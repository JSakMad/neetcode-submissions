class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap = defaultdict(int)
        final = 0

        for num in nums:

            if not hashmap[num]:
                hashmap[num] = hashmap[num - 1] + hashmap[num + 1] + 1
                hashmap[num - hashmap[num - 1]] = hashmap[num]
                hashmap[num + hashmap[num + 1]] = hashmap[num]
                final = max(final, hashmap[num])

        return final


