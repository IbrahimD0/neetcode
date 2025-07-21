class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            Understanding: we want to be able to fit in the new interval and if it causes some other intervals to merge then to merge those

            Apporach: 
                add the new ineterval in the correct sorted place

                do merge interval leetcode


                Merge interavl: 
                 append current interval 
                 if next interval intersect then merge those two
            Note: if numbers equal we merge
        """
        idx = float('inf')
        for i, (x,y) in enumerate(intervals):
           
            if newInterval[0] <= x:
                idx = i
                break
        if idx == float('inf'):
            intervals.append(newInterval)
        else:
            intervals.insert(idx, newInterval)
        
        #merge sort
        """
        (1,3), (2,5)
        3,2


             4,8
             3,8  6,7
             3,8
             3,10

        """
        stack = []
        for x,y in intervals:

            if stack:
                if stack[-1][-1] >= x:
                    prev_x,prev_y = stack.pop()
                    stack.append([prev_x,max(y,prev_y)])
                else:
                    stack.append([x,y])
            else:
                stack.append([x,y])
        return stack
       


                
            
            
