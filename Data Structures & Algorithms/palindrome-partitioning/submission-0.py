class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        def helper(s, path):
            if not s: 
                res.append(list(path))
                return
            
            for j in range(1,len(s)+1):
                    part = s[0:j]
                    if part==part[::-1]:
                        
                        path.append(s[0:j])
                        helper(s[j:],path)
                        path.pop()
                    else: continue
        helper(s, [])
        return res
        