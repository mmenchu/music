from django.contrib import admin
from music.models import *

class FeedArtistSearchAdmin(admin.ModelAdmin):
    search_fields = ['response', 'fetched_on', 'term']
    list_display = ('fetched_on', 'term')
    pass
admin.site.register(FeedArtistSearch, FeedArtistSearchAdmin)

class FeedArtistTermAdmin(admin.ModelAdmin):
    search_fields = ['term']
    list_display = ('term', 'type')
    pass
admin.site.register(FeedArtistTerm, FeedArtistTermAdmin)
