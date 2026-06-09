class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)        
        res = []
        for key in c:
            if c[key] > len(nums) // 3:
                res.append(key)
        return res