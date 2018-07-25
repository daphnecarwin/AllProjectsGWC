 import json
from textblob import TextBlob
#from wordcloud import WordCloud
import matplotlib.pyplot as plt


file = open("tweets.json", "r")
tweetData= json.load(file)
file.close()

polarityList = []

#filteredWords[word] = count


for tweets in tweetData:
     textblob = TextBlob(tweet["text"])
     polarityList.append(textBlob.polarity)

plt.hist(polarityList, bins= [-1.0, -.75, -.50, -.25, 0, .25, .50, .75, 1.0])

plt.xlabel("Polarities")
plt.ylabel("Number of tweets")

plt.title("Histogram of Tweet Polarity")
plt.grid(True)
plt.show()
#polarityList =
#subjectivityList =

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("Data/tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)





import json
import TextBlob
import matplotlib.pyplot as plt

# GET JSON DATA
# CREATE SENTIMENT LIST
#GET SENTIMENT DATA
#FOR LOOP
#PRINTOUT POLOARTIY LIST

file = open("tweetsjson, "r")



for tweets in tweetData:
    textblob = TextBlob(tweet["text"])
    polarityList.append(textBlob.polarity)

#print(polaritylist)

plt.xlabl("Polarities")
plt.ylabl("")
plt.title("Histogram of Tweet Polarity")
lpt.axis(-1.0, 1.0,0,100)
plt.grid(True)
plot.show()
