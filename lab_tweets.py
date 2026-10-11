# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.

import json
import matplotlib.pyplot as plt


tweets = []
for year in range(2009, 2019):
    filename = 'master_' + str(year) + '.json'
    with open(filename) as f:
        tweets += json.load(f)
print(len(tweets))

#print(tweets[0]['text'])


phrases = ['wall', 'America', 'MAGA', 'Trump', 'Obama', 'Mexico', 'Russia', 'Fake News']

percents = []
for phrase in phrases:
    count = 0
    for tweet in tweets:
        if 'full_text' in tweet:
            message = tweet['full_text']
        else:
            message = tweet['text']
        if phrase.lower() in message.lower():
            count += 1
    for tweet in tweets:
        percent = 100 * count / len(tweets)
    percents.append(percent)
    #print(phrase, count, percent)

print('| phrase            | percent of tweets |')
print('| ----------------- | ----------------- |')
for i in range(len(phrases)):
    phrase = phrases[i].lower().rjust(17)
    percent = format(percents[i], '05.2f').ljust(17)
    print('|', phrase, '|' , percent,'|')


plt.bar(phrases, percents)
plt.xlabel('Phrase')
plt.ylabel('Percent of Tweets')
plt.title('Percent of Tweets from 2009-2018 Containing Each Phrase')
plt.savefig('tweets.png')
