class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1,idx2 = 0, len(numbers) - 1
        while idx1 < idx2:
            s = numbers[idx1] + numbers[idx2]
            if s < target:
                idx1+=1
            elif s > target:
                idx2-=1
            else:
                 return [idx1+1,idx2+1] 