import tweepy
import json
import datetime


with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth)

last_tweet = None
username = 'your username '
startDate = datetime.datetime(2010, 1, 1, 0, 0, 0)
endDate = datetime.datetime(2020, 5, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if endDate > tweet.created_at > startDate:
        tweets.append(tweet.id)

while tmpTweets[-1].created_at > startDate and tmpTweets[-1] != last_tweet:
    last_tweet = tmpTweets[-1]
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id=tmpTweets[-1].id)
    for tweet in tmpTweets:
        if endDate > tweet.created_at > startDate:
            print(tweet.id)
            if tweet.id not in tweets:
                tweets.append(tweet.id)


for tweet in tweets:
    print("Encountered "+str(id))
    api.destroy_status(str(id))
    print("Deleted "+str(id))
