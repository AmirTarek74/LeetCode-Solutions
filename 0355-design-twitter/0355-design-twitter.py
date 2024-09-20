class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap =defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        self.tweetmap[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followmap[userId].add(userId)
        
        for follow_id in self.followmap[userId]:
            if follow_id in self.tweetmap:
                idx = len(self.tweetmap[follow_id])-1
                count, tweet_id = self.tweetmap[follow_id][idx]
                heapq.heappush(minHeap,[count, tweet_id, follow_id, idx-1])
        
        while minHeap and len(res)<10:
            
            count, tweet_id, follow_id, idx = heapq.heappop(minHeap)
            res.append(tweet_id)
            if idx>=0:
                count, tweet_id = self.tweetmap[follow_id][idx]
                heapq.heappush(minHeap,[count, tweet_id, follow_id, idx-1])
        
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)