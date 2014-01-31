import collections
import urllib
import super_scraper
import json
import pdb
import os, sys
sys.path.insert(0,'../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
from music.models import *

class AlbumExtractor():

    @staticmethod
    def extract(lookup_result):
        try:
            data = json.loads(lookup_result)
        except:
            return False
        artist_name = data['artist']['name']
        for album in data['artist']['albums']:
            album_data = collections.defaultdict(lambda: '*', album['album'])
            album_uri = album_data['href']
            
            if Album.exists(album_uri):
                continue
            else:
                print "Extracting album %s" % album_uri
                new_album = Album()
                new_album.artist_name = artist_name
                new_album.spotify_artist_id = album_data['artist'] if album_data['artist-id'] == '*' else album_data['artist-id']
                new_album.album_name = album_data['name']
                new_album.upc_id = album_data['external-ids'][0]['id'] if (album_data['external-ids'].__class__.__name__ == "dict") else '*'
                new_album.year_released = album_data['released']
                new_album.album_uri = album_data['href']
                try:
                    new_album.save()
                except:
                    print "Unable to save album %s. Title too long?" % album_data
                    continue
                    
                print "Saving album availability"
                av_record = AlbumAvailablity()
                av_record.album = new_album
                av_record.available_in = album_data['availability']['territories'] if album_data['availability'].__class__.__name__ == "dict" else '*'
                av_record.save()
        return True

    @staticmethod
    def run():
        for idx, lookup in enumerate(FeedArtistLookup.objects.all().order_by('-id')):
            AlbumExtractor.extract(lookup.response)

if __name__ == '__main__':
    AlbumExtractor.run()
        
