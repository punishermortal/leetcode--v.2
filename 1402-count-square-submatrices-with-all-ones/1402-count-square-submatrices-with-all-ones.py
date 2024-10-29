class Solution:
    def countSquares(self, g: List[List[int]]) -> int:
        return sum(starmap(f:=cache(lambda i,j:i*j*g[i][j] and 1+min(f(i,j-1),f(i-1,j-1),f(i-1,j)) or g[i][j]),product(range(len(g)),range(len(g[0])))))