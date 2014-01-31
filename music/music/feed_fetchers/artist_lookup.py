import urllib
import super_scraper
import time

import os, sys
sys.path.insert(0,'../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
from music.models import *

class ArtistLookup():

    @staticmethod
    def lookup(spotify_uri):
        url = 'http://ws.spotify.com/lookup/1/.json?uri=%s&extras=albumdetail' % spotify_uri
        response = super_scraper.SuperScraper("", url).scrape()
        print response
        time.sleep(3)
        return response, url

    @staticmethod
    def fetch(spotify_uri):
 
        if FeedArtistLookup.havent_fetched_in_48hrs(spotify_uri):
            print "Fetching lookup for %s" % spotify_uri
            resp, url = ArtistLookup.lookup(spotify_uri)
            print "Saving response to DB"
            entry = FeedArtistLookup()
            entry.url = url
            entry.fetched_on = datetime.datetime.now()
            entry.response = resp
            entry.spotify_uri= spotify_uri
            entry.save()
        else:
            print "Skipping fetch lookup for %s. Existing fetch on DB is not older than 24hrs" % spotify_uri

if __name__ == '__main__':
    for spotify_uri in FeedArtistLookup.extract_spotify_uris():
        ArtistLookup.fetch(spotify_uri)
        
