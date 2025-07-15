class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Understanding: we want to find if the two words have the same count of letters
            Edge Cases: two empty strings?
                        Uppercase and lowercase are the same?

            Apporaches:
            1: Have two dicts, one for each word and count the occurances of each letter then compare the two
            2: use an array and find the ascii values and add 1 for s occurances and -1 for t letter occurances

            Time Compleixity: O(n) since we loop through each letter of s/t 
            Space Complexitiy: O(1) since num is constant size

            Time taken to solve: 4:26 including thought process
        """

        num = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            num[ord(s[i]) - ord('a')] += 1
            num[ord(t[i]) - ord('a')] -= 1
        for i in num: 
            if i != 0:
                return False

        return True