class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Understanding: we want to find if two nmbers in nums can give us the target value

        Approach:
        1: use two nested loops and see if two numbers add to that target value if so return their idx
        2: use a hashmap and store the the difference of traget and current value with the current idx
            when a new value comes we check if we seen its difference, if so we return current idx and the diff idx

        Time complexity: O(n), we loop through nums array
        Space complexity: O(n), we store each num and idx in dict

        time: 3min 
        """

        d = {}

        for i,c in enumerate(nums):
            diff = target - c
            if diff in d:
                return [d[diff],i]
            d[c] = i
        