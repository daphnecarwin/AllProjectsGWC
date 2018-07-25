import json
import matplotlib.pyplot as plt

tweets = open("tweets.json", "r")
tweetData = json.load(tweets)
tweets.close()

print("The first tweet is: ", tweetData[0], "\n\n")

print("THe text of the frist tweet is: ", tweetData[0] ["text"], "\n\n")

for tweets range(len(tweetData)):
    print("Tweet text: ", tweetData[tweets]["text"], "\n")

for tweets in tweetData:
    print("Tweet timestamp: ", tweetData["created_at"], "\n")
