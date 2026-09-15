class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.stack = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.stack.append((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 0
        self.users[userId].add(userId)
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] in self.users[userId]:
                res.append(self.stack[i][1])
                count+=1
                if count == 10: break
        return res
                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].add(followeeId)
        else : self.users[followerId] = {followeeId} 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
        
