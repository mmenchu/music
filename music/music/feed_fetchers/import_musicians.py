"""
find_musicians.sh | python import_violinist.py [musician_type]   to run this
"""
import urllib
import super_scraper

import os, sys
sys.path.insert(0,'../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
from music.models import *

class ImportMusicians():

    @staticmethod
    def run(full_name, musician_type):
        if FeedArtistTerm.objects.filter(term=full_name).count() > 0:
            print "%s already exists" % full_name
            return False
        print "Creating record for %s" % full_name
        new_violinist = FeedArtistTerm()
        new_violinist.type = musician_type
        new_violinist.term = full_name
        new_violinist.save()
        return True

if __name__ == '__main__':
    musician_type = sys.argv[1]
    for full_name in sys.stdin.readlines():
        ImportMusicians.run(full_name.strip(), musician_type)
