class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        c = 0
        for n in nset:
            if (n - 1) not in nset:
                l = 1
                while (n+l)in nset:
                    l+=1
                c = max(l,c)
        return c 