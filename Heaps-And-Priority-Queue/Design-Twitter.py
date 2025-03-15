class Twitter:

    class User:
        def __init__(self):
            self.following = set()
            self.posts = []

    def __init__(self):
        self.users = {}
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.users:
            self.users[userId] = self.User()

        post = (-self.timestamp, tweetId)
        self.users[userId].posts.append(post)

        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        
        if userId not in self.users:
            self.users[userId] = self.User()

        min_heap = []
        heapq.heapify(min_heap)

        for post in self.users[userId].posts: #push user's own posts in the min_heap
            heapq.heappush(min_heap, post)

        for followingId in self.users[userId].following: #for every person the user follows
            
            if followingId not in self.users:
                self.users[followingId] = self.User()

            followingUser = self.users[followingId]
            for post in followingUser.posts:
                heapq.heappush(min_heap, post)

        feed = []
        while min_heap and len(feed) < 10:
            post = heapq.heappop(min_heap)
            feed.append(post[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users:
            self.users[followerId] = self.User()

        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.users:
            self.users[followerId].following.discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
