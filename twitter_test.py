import twitter
import time
from pprint import *
import random
import datetime
api = twitter.Api(consumer_key='sbMTGzp9V3RDd4avWHznjbFBU',
                  consumer_secret='AWBzfhNzdtGxnleshYNK1TgFleMIvuCSxk6e5PaAzlMDJtF30N',
                  access_token_key='1113972196320337920-ff8568yz75KKTwi1tk0GTP4eorRAt8',
                  access_token_secret='QVK6LgIhDWOmqIWkfT9TikeVsJfX7ilXhSKpFLuulR5L2')

MAX_FRIENDS = 5000
KEYWORD = "メモの魔力"
EXTRA_INTERVAL_IN_SEC = 5*60 # 5 min
MIN_INTERVAL_IN_SEC = 10*60 # 10 min
NUM_OF_TWEET_TO_PROCESS_PER_QUERY = 5

def main():
    # check if # of friends reaches max
    friends = api.GetFriendIDs(count=1000)
    if len(friends)+NUM_OF_TWEET_TO_PROCESS_PER_QUERY >= MAX_FRIENDS:
        # Remove some friend
        for i in range(NUM_OF_TWEET_TO_PROCESS_PER_QUERY):
            friendId = friends[-i]
            api.DestoryFriendship(user_id=friendId)

    # search with keyword
    result = api.GetSearch(term=KEYWORD)

    # find a tweet whose user haven't been followed
    count = 0
    followed = set()
    for tweet in result:
        if count >= NUM_OF_TWEET_TO_PROCESS_PER_QUERY:
            break
        tweetDict = tweet.AsDict()
        print(datetime.datetime.now())
        print("Following", tweetDict['user']['name'])
        userId = tweetDict['user']['id']
        if userId in followed:
            continue
        followed.add(followed)
        count += 1
        print("ID:", userId)
        api.CreateFriendship(user_id=userId)
        time.sleep(MIN_INTERVAL_IN_SEC+random.random()*EXTRA_INTERVAL_IN_SEC)

while True:
    main()
