class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            days_used = 1
            currentWeight = 0
            for wt in weights:
                if currentWeight + wt > mid:
                    days_used += 1
                    currentWeight = 0
                currentWeight += wt
            if days_used <= days:
                    right = mid
            else:
                    left = mid + 1
        return left