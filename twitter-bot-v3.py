"""

This code is partly based on Molly White's excellent tutorial at:
http://blog.mollywhite.net/twitter-bots-pt2/ and
https://github.com/molly/twitterbot_framework/blob/master/bot.py

"""

import time, tweepy, random

from keys import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

count = 0

with open ('a-liners.txt', 'r+') as tweetfile: # Reads the file of Anne's quotations
    buff = tweetfile.readlines() # Turns the whole file into a variable called 'buff'

while count < 100:  # Will run 100 times
    line = random.choice(buff) # takes a random line from buff and calls it 'line'
    line = line.strip(r'\n') # Strips any empty line.

    # If the text is fewer than 140 characters this bit runs
    if len(line)<=140 and len(line)>0:
        api.update_status(status=line) # Tweets the Tweet
        print ("Tweeting " + str(len(line)) + " characters") # Tells us what is happening
        print(line)
        count += 1
        time.sleep(14400) # Sleeps for a few hours

    # Otherwise this bit runs    
    else:
        api.update_status(status=line)
        print ("Tweeting 140 characters, truncated from " + str(len(line)) + " characters")
        line = line[:140]
        count += 1
        time.sleep(14400) # Sleeps for a few hours
        continue
    
print ("\nFinished.")



