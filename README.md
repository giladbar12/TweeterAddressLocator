# TweeterAddressLocator
The program allows the user to get the addresses from which tweets with a specific hashtag, given they are geotagged, were tweeted.  The program allows you to initialize a desired hastag and the earliest date the desired tweets can be posted. The program fetches the desired tweets using the Tweepy API. The program then accesses the geolocation (latitude and longitude) of the tweets which were geotagged and then utilizes the Google Maps API to translate the geolocation to a readable formatted Address.
