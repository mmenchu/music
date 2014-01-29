curl "http://en.wikipedia.org/wiki/List_of_contemporary_classical_violinists" | grep '<li><a href="' | grep -v "div" | cut -d'/' -f3 | cut -d'"' -f3 | python import_musicians.py 0
curl "http://en.wikipedia.org/wiki/Category:Baroque-violin_players" | grep '<li><a href="' | grep -v "div" | cut -d'/' -f3 | cut -d'"' -f3 | python import_musicians.py 0
curl "http://en.wikipedia.org/wiki/List_of_cellists" | grep '<li><a href="' | grep -v "div" | cut -d'/' -f3 | cut -d'"' -f3 | cut -d'(' -f1 | python import_musicians.py 1
curl "http://en.wikipedia.org/wiki/List_of_classical_pianists" | grep '<li><a href="' | grep -v "div" | cut -d'/' -f3 | cut -d'"' -f3 | cut -d'(' -f1 | python import_musicians.py 2
curl "https://en.wikipedia.org/wiki/Category:Viol_players" | grep '<li><a href="' | grep -v "div" | cut -d'/' -f3 | cut -d'"' -f3 | cut -d'(' -f1 | python import_musicians.py 9
