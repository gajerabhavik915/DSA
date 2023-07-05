import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        res = []  #[[3,1], [2,2], [1,3]]
        dict1 = {}  # 1:3 , 2:2, 3:1
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        for key, val in dict1.items():
            if len(res) < k:
                heapq.heappush(res, [val, key])
                # print(res)
            else:
                heapq.heappushpop(res, [val,key])
                # print(res)

        

        return [key for val, key in res]
