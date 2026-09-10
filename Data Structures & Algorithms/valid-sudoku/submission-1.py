class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       #unique hashset through the entire grid 
       #unique hashset for every different column to check duplicates
       #O(1)

       #hashset for 3*3 grid too
       #Overall- O(9^2)

       #map each indexes through the submatrix of row and col which will give 0,1,2
       #then divide those sub matrix index like 012,345,678 with 3 to find where exactly the matrix lies eg [4,4] then gets divided by 3 gives [1,1]

       #key- row/3,col/3 val-hashset and check duplicate and if any return false else return true

       cols= collections.defaultdict(set) #key-column no, val-another set represent all particular values in columns
       rows= collections.defaultdict(set)
       squares= collections.defaultdict(set) #key=(r/3,c/3)

       for r in range(9):  
            for c in range(9):
                if board[r][c]==".": #checking empty space with dot
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])    
       return True 



        
       


        

        