from collections import defaultdict
import heapq
from typing import List

class Twitter:
    """
    U - Understand the Problem
    ----------------------------------
    Problem:
    - Implement a simplified Twitter with three main functionalities:
        1. postTweet(userId, tweetId): Post a new tweet.
        2. getNewsFeed(userId): Retrieve the 10 most recent tweet IDs in the user's news feed.
        3. follow(followerId, followeeId): The follower follows the followee.
        4. unfollow(followerId, followeeId): The follower unfollows the followee.

    - Tweets must be ordered from most recent to oldest.
    - Each user follows themselves by default.

    Edge Cases:
    - Multiple tweets by the same user.
    - User following/unfollowing themselves.
    - User with no followers or no tweets.
    - Retrieving news feed with less than 10 tweets.

    M - Match
    ----------------------------------
    - Data Structures:
        - Dictionary for tweet storage (userId -> [tweets])
        - Dictionary for followers (userId -> set of followeeIds)
        - MinHeap to track the top 10 tweets in the news feed.

    - Algorithm Patterns:
        - MinHeap for maintaining top 10 tweets.
        - HashMap for storing user data and follower/followee relationships.

    P - Plan
    ----------------------------------
    - postTweet(userId, tweetId):
        1. Append the tweet to the user's tweet list with a timestamp for ordering.

    - getNewsFeed(userId):
        1. Create a MinHeap.
        2. Add the most recent tweet of each followed user.
        3. Extract top 10 tweets in chronological order.

    - follow(followerId, followeeId):
        1. Add the followee to the follower's set.

    - unfollow(followerId, followeeId):
        1. Remove the followee from the follower's set.

    I - Implement
    ----------------------------------
    """

    def __init__(self):
        self.count = 0  # Global timestamp counter to maintain chronological order
        self.tweetMap = defaultdict(list)  # userId -> list of (count, tweetId)
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        - Adds a tweet to the tweetMap for the user.
        - Decrements the count to maintain reverse chronological order.
        """
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1  # Decrement to maintain order

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        - Retrieves the top 10 most recent tweets in the user's news feed.
        - Includes tweets from the user and the users they follow.
        - Maintains a min-heap to ensure the top 10 tweets are retrieved.
        """
        minHeap = []
        res = []

        # Ensure user follows themselves
        self.followMap[userId].add(userId)

        # Add the latest tweet of each followed user to the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and len(self.tweetMap[followeeId]) > 0:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        # Extract the top 10 tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        - Adds followeeId to followerId's follow list.
        - Ensures a user follows themselves by default.
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        - Removes followeeId from followerId's follow list.
        - Ensures a user cannot unfollow themselves.
        """
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)

    """
    R - Review
    ----------------------------------
    - The implementation uses a min-heap to efficiently maintain the top 10 tweets in O(N log 10) time.
    - Ensures O(1) complexity for postTweet and follow/unfollow operations.
    - Handles edge cases such as self-following and non-existent users.

    E - Evaluate
    ----------------------------------
    Time Complexity:
    - postTweet: O(1)
    - getNewsFeed: O(N log 10) → N being the number of tweets in the user's feed
    - follow/unfollow: O(1)

    Space Complexity:
    - O(N + F), where N is the number of tweets and F is the number of followers.
    """
