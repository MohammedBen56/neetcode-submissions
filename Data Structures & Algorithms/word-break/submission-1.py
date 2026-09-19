class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        idx = []
        if s[0] in words:
            idx.append(0)
        for i in range(1, len(s)):
            if s[:i+1] in words:
                idx.append(i)
                continue
            for d in idx:
                if s[d+1:i+1] in words: 
                    idx.append(i)
                    break
            

        return (len(s)-1) in idx

        