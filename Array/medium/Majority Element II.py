
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = None
        element2 = None
        count1 = 0
        count2 = 0
        leng = len(nums)//3
        
        for i in nums:
            if i == element1:
                count1 += 1
            elif i == element2:
                count2 += 1
            elif count1 == 0:
                element1 = i
                count1 += 1
            elif count2 == 0:
                element2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in [element1, element2] if nums.count(n) > leng]
        


