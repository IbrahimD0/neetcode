class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        """
        Understanding: we want to find if there is a duplicate number
        Edge cases: empty list

        Apporaches:
        1: create a set and compare len
        2: create a set and check if num in set
        3: two for loops to see if we come to the same number

        Time complexity: O(n)
        Space Complexity: O(n)

        Time taken: 1:51

        """

        s = set(nums)
        return len(s) != len(nums)