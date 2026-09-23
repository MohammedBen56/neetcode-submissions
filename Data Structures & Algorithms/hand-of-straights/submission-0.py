class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0: return False
        dic = Counter(hand)
        for i in range(len(hand)):
            if i%groupSize ==0: minn = min(dic.keys())
            if minn in dic:
                dic[minn]-=1
            else: return False
            if dic[minn] <=0: dic.pop(minn)
            minn+=1
        return True

