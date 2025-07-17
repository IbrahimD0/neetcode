class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Understanding: We want to return k numbers sorted by occurances
            Edge cases: numbers have the same occurance
                        empty list
            
            apporach: 
            1: use heapque and append by occurances and then pop k times
            2: use an array and store occrances by their index
               then go from highest occurance to lowest

            13 min

            Time complexitY: O(n)
            Space Complexity: O(n)

        """
        n = len(nums)
        count = [[] for i in range(n+1)] 

        d = {}

        for i in nums:
            d[i] = d.get(i,0) + 1
        for x,y in d.items():
           
            count[y].append(x)
        ans = []
        for i in range(n,-1,-1):
            for j in count[i]:
                ans.append(j)

                if len(ans) == k:
                    return ans
        return ans