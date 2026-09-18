class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def helper(digits, path):
            if not digits:
                print(path)
                res.append(path)
                return
            for d in digitToChar[digits[0]]:
                path+=d

                helper(digits[1:],path)
                path = path[:-1]
            
        path = ""
        if not digits: return res
        for d in digitToChar[digits[0]]:
            path+=d
            print(path)
            helper(digits[1:],path)
            path = path[:-1]

        return res

        