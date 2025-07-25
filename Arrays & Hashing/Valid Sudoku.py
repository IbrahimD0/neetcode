class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Understanding: we are trying to see if current filled board makes a fild sudoko
                        ie: unique row,col and square numbers
        Edge Cases: empty board

        Apporach:
                do a nested loop and have a way to check each square

        Time Complexitiy: O(n*m)
        Space Complexitiy: O(n)

        """

        squares = [[set() for _ in range(3)] for _ in range(3)]
       
        rows = [set() for _ in range(9)]
       
        cols = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3)][(j//3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3)][(j//3)].add(board[i][j])
           

        return True