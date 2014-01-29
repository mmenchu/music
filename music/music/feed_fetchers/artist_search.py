import urllib
import super_scraper
import time

import os, sys
sys.path.insert(0,'../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
from music.models import *

class ArtistSearch():

    @staticmethod
    def search(full_name):
        encoded_full_name = urllib.urlencode({'name':full_name}).split('=')[1]
        url = "http://ws.spotify.com/search/1/artist.json?q=%s" % encoded_full_name
        response = super_scraper.SuperScraper("", url).scrape()
        print response
        time.sleep(3)
        return response, url

    @staticmethod
    def fetch(full_name):
        if FeedArtistSearch.havent_fetched_in_24hrs(full_name):
            print "Fetching search for %s" % full_name
            resp, url = ArtistSearch.search(full_name)
            print "Saving response to DB"
            entry = FeedArtistSearch()
            entry.url = url
            entry.fetched_on = datetime.datetime.now()
            entry.response = resp
            entry.term = full_name
            entry.save()
        else:
            print "Skipping fetch search for %s. Existing fetch on DB is not older than 24hrs" % full_name

if __name__ == '__main__':
    for artist in FeedArtistTerm.objects.all():
        try:
            ArtistSearch.fetch(artist.term)
        except:
            print ">> Check out %s" % artist.term
