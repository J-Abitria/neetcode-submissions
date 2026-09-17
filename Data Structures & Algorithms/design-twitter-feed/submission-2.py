import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = []
        self.users = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush_max(self.tweets, (self.time, userId, tweetId))
        if userId not in self.users:
            self.users[userId] = dict()
        
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = list()

        tweetsCopy = self.tweets.copy()
        while len(tweetsCopy) > 0 and len(posts) < 10:
            tweet = heapq.heappop_max(tweetsCopy)
            posterId = tweet[1]
            if posterId == userId or posterId in self.users[userId]:
                posts.append(tweet[2])
        
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = dict()
            
        self.users[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            del self.users[followerId][followeeId]
