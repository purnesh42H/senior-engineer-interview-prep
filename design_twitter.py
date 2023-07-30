'''
api/public methods:
1. post(user_id, tweet_id) -> always with new tweet_id
2. follow(follower_user_id, followee_user_id)
3. unfollow(follower_user_id, followee_user_id)
4. get_news_feed(user_id) -> get_most_recent_tweets(user_id)

data structures:
tweet_map => userid -> all tweets -> deque
follower_map => follower_id -> all follwees (set)

'''

from collections import deque, defaultdict
from heapq import heapify, heappop
import unittest

class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(deque)
        self.follower_map = defaultdict(set)
        self.followee_map = defaultdict(set)
        self.timer = 0

    def post(self, userId: int, tweetId: int):
        self.timer += 1
        self.tweet_map[userId].appendleft((tweetId, self.timer))

    def get_news_feed(self, userId: int):
        max_heap = [(-timer, tweet_id) for (tweet_id, timer) in self.tweet_map[userId]]

        for followee in self.followee_map[userId]:
            if followee in self.tweet_map:
                max_heap.extend([(-timer, tweet_id)for (tweet_id, timer) in self.tweet_map[followee]])
        
        heapify(max_heap)

        top_10 = []

        while max_heap and len(top_10) < 10:
            _, tweet_id = heappop(max_heap)
            top_10.append(tweet_id)
    
        return top_10

    def follow(self, followerId: int, followeeId: int):
        self.follower_map[followeeId].add(followerId)
        self.followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followeeId in self.follower_map:
            self.follower_map[followeeId].remove(followerId)
        if followerId in self.followee_map:
            self.followee_map[followerId].remove(followeeId)

class TwitterTest(unittest.TestCase):

    def test_post(self):
        twitter = Twitter()

        twitter.post(1, 1)
        twitter.post(1, 2)
        twitter.post(2, 3)
        twitter.post(3, 4)
        twitter.post(1, 5)

        self.assertListEqual([(5, 5), (2, 2), (1, 1)], list(twitter.tweet_map[1]))
        self.assertListEqual([(3, 3)], list(twitter.tweet_map[2]))
        self.assertListEqual([(4, 4)], list(twitter.tweet_map[3]))

    def test_follow(self):
        twitter = Twitter()

        twitter.follow(3, 1)
        twitter.follow(2, 1)
        twitter.follow(1, 3)
        twitter.follow(2, 4)

        self.assertSetEqual(set([3, 2]), twitter.follower_map[1])
        self.assertSetEqual(set([]), twitter.follower_map[2])
        self.assertSetEqual(set([2]), twitter.follower_map[4])
        self.assertSetEqual(set([1]), twitter.follower_map[3])

    def test_unfollow(self):
        twitter = Twitter()

        twitter.follow(3, 1)
        twitter.follow(2, 1)
        twitter.follow(1, 3)
        twitter.follow(2, 4)

        self.assertSetEqual(set([3, 2]), twitter.follower_map[1])
        self.assertSetEqual(set([]), twitter.follower_map[2])
        self.assertSetEqual(set([2]), twitter.follower_map[4])
        self.assertSetEqual(set([1]), twitter.follower_map[3])

        twitter.unfollow(3, 1)
        self.assertSetEqual(set([2]), twitter.follower_map[1])

    def test_most_recent_tweets(self):
        twitter = Twitter()

        twitter.follow(2, 1)
        twitter.post(1, 1)
        twitter.post(1, 2)
        twitter.post(2, 3)

        self.assertListEqual([3, 2, 1], twitter.get_news_feed(2))

if __name__ == "__main__":
    unittest.main()

