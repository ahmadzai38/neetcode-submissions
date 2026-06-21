class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1
        while top <= bot:
            midrow = (top + bot)//2
            if target < matrix[midrow][0]:
                bot = midrow -1
            elif target > matrix[midrow][-1]:
                top = midrow+1
            else:
                break
        if not (top<= bot):
            return False
        midrow = (top+bot)//2
        l , r = 0 , len(matrix[midrow])-1
        while l<=r:
            mid = (l+r)//2
            if target < matrix[midrow][mid]:
                r = mid -1
            
            elif target> matrix[midrow][mid]:
                l = mid+1
            
            else:
                return True
        return False
        

