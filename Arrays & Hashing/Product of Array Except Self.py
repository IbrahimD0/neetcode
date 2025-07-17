class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            understanding: we have an array and we want to find the prefix and suffix of each element and multiple them
                to get the product without self


            Apporach: 
                Create a prefix array of product of all elements before current
                Create a suffix array of products strating from the end

                ex: [1,2,3,4]
                prefix [1,1,2,6] *  suffix [24,12,4,1]
                res = [24, 12, 8, 6]

            we can optimize

        """

        n = len(nums)

        ans = [1]*n

        end = n-1
        pre,suf = 1,1
        for i in range(n):
            ans[i] *= pre
            ans[end] *= suf

            suf *= nums[end]
            pre *= nums[i]
            end -= 1
            print(ans)

        
        return ans