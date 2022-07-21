# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# - Twitter() Initializes your twitter object.
# - void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# - List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# - void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# - void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Example 1:
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Constraints:
# - 1 <= userId, followerId, followeeId <= 500
# - 0 <= tweetId <= 104
# - All the tweets have unique IDs. (RL: later tweet doesn't mean it has a larger ID)
# - At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

# getNewsFeed:
# get the latest post for every person followed
# heapify the list -- maxheap
# pop max and add the next latest post by that person to the heap
# once res has 10 posts or out of tweets return
# O(f + 10 log f) => O(f)? f being # of followers, worst case all posts from one person, so push * pop 10times


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # user1: (user2, user3)
        self.tweets = defaultdict(list) # user1:[(1,5),(2,4),(3,2)] (cnt, id)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        res = []
        maxHeap = []

        for follow in self.follows[userId]:
            if follow in self.tweets: #if person followed even has any tweets
                last_idx = len(self.tweets[follow]) - 1
                count, tweet_id = self.tweets[follow][last_idx]
                maxHeap.append((count,tweet_id, follow, last_idx-1))  # [ -count, last_msg_id , user_id, next_msg_id]
        #heapify to get maxHeap
        # at this point, maxHeap has one tweet from everyone I follow with at least 1 tweet
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            count, tweet_id, user_id, next_idx = heapq.heappop(maxHeap)
            res.append(tweet_id)
            if next_idx >= 0: #if valid index, add that to the maxHeap
                next_count, next_msg = self.tweets[user_id][next_idx]
                heapq.heappush(maxHeap,(next_count,next_msg, user_id, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# passes but probs shouldnt, this getNewsFeed would be crazy slow in actual twitter
# this also assumes that tweetId is synonymous with when it's posted, but isnt the case

#     def __init__(self):
#         self.users = defaultdict(set)
#         self.tweets = []

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self.tweets.append((tweetId,userId))
#         # print(self.tweets)

#     def getNewsFeed(self, userId: int) -> List[int]:
#         res = []
#         for tweet, user in self.tweets[::-1]:
#             if len(res) == 10: break
#             if user in self.users[userId] or user == userId:
#                 res.append(tweet)

#         return res


#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.users[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         followingList = self.users[followerId]
#         if followeeId in followingList:
#             followingList.remove(followeeId)

