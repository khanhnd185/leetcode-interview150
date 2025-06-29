class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Validate row
        for row in board:
            nums = []
            for n in row:
                if n==".": continue
                n = int(n)
                if n>9 or n<0 or n in nums: return False
                nums.append(n)
    
        # Validate col
        for c in range(len(board[0])):
            nums = []
            for row in board:
                n = row[c]
                if n==".": continue
                n = int(n)
                if n>9 or n<0 or n in nums: return False
                nums.append(n)
        
        # Validate sub-box
        for col in [0,3,6]:
            for row in [0,3,6]:
                nums=[]
                for c in range(3):
                    for r in range(3):
                        n = board[col+c][row+r]
                        if n==".": continue
                        n = int(n)
                        if n>9 or n<0 or n in nums: return False
                        nums.append(n)
        return True