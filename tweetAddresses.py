import googlemaps
import tweepy
from datetime import datetime

 
### set up the address file ### 
Write_file = open("Tweet_Addresses.txt",'w' )

### set up the API keys ###
consumer_key ='Your Twitter Consumer Key'
consumer_secret ='Twitter Consumer Secret Key'
access_token_key ='Twitter Access Token Key '
access_token_secret ='Twitter Access Token Secret'
googleKey ='Your Google Maps Key'

### set the desired hashtag and earliest date to look up ###
search_words ='#'+'Desired Hashtag'
date_since ='yyyy-mm-dd'



### Setup access to tweepy API ###
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

#locate all the tweets with the wanted hashtag
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(1000)

### uses GoogleMaps API to translate Geolocation to readable address ###
def findAddress(longa,lang):
    address =''
    gmaps = googlemaps.Client(key=googleKey) 
    x=0
    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((longa, lang))
    for item in reverse_geocode_result:
        for keys, value in item.items(): 
            if keys == 'formatted_address':
                address = value
                x=1
                break 
        if x==1:
            break
    if address != '':
        Write_file.write(address+"\n")

### traverse tweets with wanted hashtag and gets the geolocation ###
for tweet in tweets:
    location = tweet.place
    try:
        location.bounding_box
    except AttributeError:
        continue
    boundbox=location.bounding_box
    coord = boundbox.coordinates
    loc1 = coord[0][0]
    loc2 = coord[0][1]
    loc3 = coord[0][2]
    loc4 = coord[0][3]
    longatitude = (loc1[1]+loc2[1]+loc3[1]+loc4[1])/4
    lagitude =(loc1[0]+loc2[0]+loc3[0]+loc4[0])/4
    findAddress(round(longatitude, 6),round(lagitude,6))




Write_file.close()