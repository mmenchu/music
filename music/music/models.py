from django.db import models
import datetime
import json

class FeedArtistLookup(models.Model):
    url         = models.CharField(max_length=512)
    fetched_on  = models.DateTimeField()
    response    = models.TextField()
    spotify_uri = models.CharField(max_length=256)

    @classmethod
    def havent_fetched_in_24hrs(cls, spotify_uri):
        query = cls.objects.filter(spotify_uri=spotify_uri).order_by('-fetched_on')
        if query.count() == 0:
            return True
        else:
            last_fetch = query[0].fetched_on.replace(tzinfo=None)
            return (datetime.datetime.now() - last_fetch).days > 1

    @classmethod
    def extract_spotify_uris(cls):
        unique_terms = FeedArtistSearch.objects.values_list('term', flat=True).distinct()
        spotify_uris = []
        for term in unique_terms:
            resp = FeedArtistSearch.get_fetches_for_term(term)[0].response
            for artist in json.loads(resp)['artists']:
                print "%s: %s" % (artist['href'], artist['name'])
                spotify_uris.append(artist['href'])
        return spotify_uris

    class Meta:
        app_label = 'music'

class FeedArtistSearch(models.Model):
    """
    curl "http://ws.spotify.com/search/1/artist.json?q=paganini"
    """
    url         = models.CharField(max_length=512)
    fetched_on  = models.DateTimeField()
    response    = models.TextField()
    term        = models.CharField(max_length=64)

    @classmethod
    def get_fetches_for_term(cls, term):
        return cls.objects.filter(term=term)

    @classmethod
    def havent_fetched_in_24hrs(cls, term):
        query = cls.objects.filter(term=term).order_by('-fetched_on')
        if query.count() == 0:
            return True
        else:
            last_fetch = query[0].fetched_on.replace(tzinfo=None)
            return (datetime.datetime.now() - last_fetch).days > 1
        
    class Meta:
        app_label = 'music'

class FeedArtistTerm(models.Model):
    artist_types = ((0, 'violinist'), (1, 'cellist'), (2, 'pianist'))
    term    = models.CharField(max_length=64)
    type    = models.IntegerField(choices=artist_types)

    class Meta:
        app_label = 'music'
