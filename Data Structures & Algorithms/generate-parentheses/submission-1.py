class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(open, close, path):
            if len(path)== 2*n:
                res.append(path)
            if open < n:
                helper(open+1, close, path+"(")
            if close < open:
                helper(open, close+1, path+")")
        helper(0,0,"")

                    
                      
                
      
        return res
            


        