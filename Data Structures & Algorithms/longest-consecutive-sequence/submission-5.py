class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set()
        longest = 0
        for i in range(len(nums)):
            setnums.add(nums[i])
        for j in setnums:
            if j - 1 not in setnums:
                length = 1
                while j + length in setnums:
                    length += 1
                if length > longest:
                    longest = length
        return longest
