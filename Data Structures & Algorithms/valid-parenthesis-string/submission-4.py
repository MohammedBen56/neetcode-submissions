class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        start = []
        for i,c in enumerate(s):
            if c == '(': left.append(i)
            elif c == '*': start.append(i)
            else:
                if left: left.pop()
                elif start: start.pop()
                else: return False
        while left and start:
            print(left)
            print(start)
            if left[-1]<start[-1]: 
                left.pop()
                start.pop()
            else: return False
        if left and not start: return False
        return True

        
        