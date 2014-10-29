curl "http://en.wikipedia.org/wiki/List_of_classical_music_composers_by_era" | grep area | cut -d'"' -f8
