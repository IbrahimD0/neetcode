class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
            Understanding: Find the increaseing order of numbers in the nums


            apporach: have a set
                look if current num is not findable in set since we want the smallest of the consecitve sequence

            

            Important: make sure ur loopping through the set only otherwise it will have some edge cases that dont pass

            Time: O(n)
            spac: O(n)

        """

        s = set(nums)
        final = 0
        i = 0
        for i in s:
 
            if (i-1) not in s:
                j = 0
              
                while i+j in s:
                    
                    j += 1
                
                final = max(final, j)
           
        return final 
