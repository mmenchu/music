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
or a "transcription of the Caprices for a quartet". This is an era of Google, Pinterest and the Cloud. 

Discovery is also harder due to the fact composers and performers get treated pretty much the same way. 
Maxim Vengerov is according to Spotify similar to "Johann Strauss II"; Gil Shaham comes to mind more easily if you ask me. 

![alt tag](https://raw.github.com/mmenchu/music/master/readme/spotify_2.png "")

## Scrapers

DB Content is scraped via the feed fetchers in music/music/feed_fetchers/
[code]
./find_musicians.sh  # Curls Wikipedia lists of classical musicians

artist_search.py & artist_lookup.py # Curl wrappers to hit the Spotify's "Lookup" and "Search" APIs
[/code]

