class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False]* len(s)
        words = set(i for i in wordDict)
        idx = []
        if s[0] in words:
            arr[0] = True
            idx.append(0)
        for i in range(1, len(s)):
            if s[:i+1] in words:
                arr[i] = True
                idx.append(i)
                continue
            for d in idx:
                if s[d+1:i+1] in words: 
                    arr[i] = True
                    idx.append(i)
                    break
            

        return arr[len(s)-1]

        