class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = []
        l = len(board)
        w = len(board[0])
        used = set()
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    idx.append((i,j))
        if not idx: return False
        def helper(path, cur, word, used):
            next= [(cur[0]+1,cur[1]), (cur[0]-1, cur[1]), (cur[0],cur[1]+1), (cur[0], cur[1]-1)]
            for n in next:

                if n[0] <l and n[0]>=0 and n[1]>=0 and n[1]<w and board[n[0]][n[1]]==word[0] and n not in used:
                    if not word[1:]: return True
                    path.append(n)
                    used.add(n)
                    res= helper(path,n, word[1:],used)
                    path.pop()
                    used.remove(n)
                    if res: return True
            return False

        for i in idx:
            if not word[1:]: return True
            used.add(i)
            res= helper([i],i, word[1:],used)
            used.remove(i)
            if res: return True
        return False