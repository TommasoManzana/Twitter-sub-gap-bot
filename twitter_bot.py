import urllib.request
import json
import tweepy
import time

#TWITTER API KEYS
CONSUMER_KEY = 'my_consumer_key'
CONSUMER_SECRET = 'my_consumer_secret_key'
ACCESS_KEY = 'my_access_key'
ACCESS_SECRET = 'my_access_secret_key'

#YTB API KEY
ytbkey = "my_youtube_key"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#arbitrary amount of subs for the first check
i = 50000

def get_data(i):
    pewid = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
    tsid = "UCq-Fj5jknLsUf-MWSy4_brA"
    #get data from youtube
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+pewid+"&key="+ytbkey).read()
    pewsubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    data2 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+tsid+"&key="+ytbkey).read()
    tssubs = json.loads(data2)["items"][0]["statistics"]["subscriberCount"]
    
    subgap = int(pewsubs) - int(tssubs)
    
    if (subgap < i):
        tweet_subgap(subgap, i, pewsubs, tssubs)
        #if it tweeted go for the next milestone, old milestone minus arbitrary amount
        i = i - 5000
        print("I tweeted!")
        
    return i
    
def tweet_subgap(subgap, i, pewsubs, tssubs):
    api.update_status('ಠ_ಠ Sub count bot here ಠ_ಠ\nThe sub gap is below ' + '{:,d}'.format(i) + '! (' + '{:,d}'.format(subgap) + ' subs)\n@pewdiepie has ' + '{:,d}'.format(int(pewsubs)) + ' subscribers\n@TSeries has ' + '{:,d}'.format(int(tssubs)) + ' subscribers')

while True:
    i = get_data(i)
    #check every 10 minutes
    time.sleep(600)