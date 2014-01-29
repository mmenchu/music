# Music

## Description

  Music is a personal experiment aimed towards a better discovery avenue for classical and baroque music on Spotify.

  The traditional music discovery avenues really don't work for these music genres: Machine Learning algorithms
don't have enough data to do their learning because most people don't listen to classical/baroque; Marketing emails
only drive traffic to the very few deals the service was able to sign; Social Music discovery just brings us back to
why the learning algorithms don't work; And searching for recordings of known works pretty much returns the same old
stuff regardless of what new jewels there may be.
 
  I'm very fond of Paganini's 24 Caprices for violin. Published in 1819, they've been recorded by most of the most
prominent violinists since; I grew up listening to those of Heifetz, Midori and Itzhak Perlman. They're fine recordings,
but new ones have popup up since, some by already-established soloists, others by younger upcoming musicians.
Spotify does not have them all - Alexander Markov's for one - but it does have a few, and despite having them whenever
I search for "Paganini Caprices" almost half the results smell like the old status quo. For example the recordings of 
Ilya Gringolts and Leonidas Kavakos are nowhere to be found on search results despite being currently available on the service.
This isn't an issue of quality; Gringolts plays Caprice No. 5 in jaw-dropping 1:53, much much faster than Heifetz himself, 
and that Kavakos nails No. 24 with the stamina of a bull like no other. 

![alt tag](https://raw.github.com/mmenchu/music/master/readme/spotify_1.png "")

A violin student studying/researching the Paganini Caprices has no way of finding "the fastest recording of No. 5"
or a "transcription of the Caprices for a quartet". This in an era of Google, Pinterest and the Cloud. 

Discovery is also harder due to the fact composers and performers get treated pretty much the same way. 
Maxim Vengerov is according to Spotify similar to "Johann Strauss II"; Gil Shaham comes to mind more easily if you ask me. 

![alt tag](https://raw.github.com/mmenchu/music/master/readme/spotify_2.png "")

## Content

Run the following scrapers in music/music/feed_fetchers/ to populate the DB.
1. Curl Wikipedia lists of classical violinists/pianists/cellists/... We'll look these guys up on Spotify 
```
./find_musicians.sh  
```
2. Hit Spotify's Search (list of an artist's Albums) and Lookup (Album details) APIs 
```
python artist_search.py
python artist_lookup.py 
```
3. Create individual Album entries
```
python import_musicians.py
```
Should have this many after a little while (violinists/cellists/pianists only)
```
music=# select count(*) from  music_album;
 count
-------
  8633
(1 row)
```

## Next Steps - 1/28/2014

* Detailed info about the tracks in each album
* Non-trivial linking between tracks. For example a recording of Rachmaninov's Variation on La Folia should
  be related to a recording of Corelli's La Folia for Violin & Piano.

