class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            days_gone = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > m:
                    days_gone += 1
                    current_weight = 0 
                current_weight += w
            if days_gone <= days:
               r = m
            else:
                l = m + 1
        return l