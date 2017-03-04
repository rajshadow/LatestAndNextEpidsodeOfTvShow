# LatestAndNextEpidsodeOfTvShow
Python wrapper around the tvdb_api (https://github.com/dbr/tvdb_api) to get the latest and next episode of a given TV-Show

USAGE:
Simple call the def get_details() with the TV-show name whose latest and next episode you would like to know:
```
info_string = get_deatils('Legion')
print info_string
```

Output will look like:
```
Legion:
Latest Episode: S01E04-Chapter 4 airdate:March 01, 2017
Next Episode on: March 08, 2017
```

In case the user wants to know the latest and next episode details of multiple tv shows, there is parallel version get_details_parallel() to make requests to the tvdb in parallel. The fuction expects an array of tvShows.

Example usage:
```
tvShows = ['Legion','The Expanse', 'The Flash (2014)', 'Brooklyn Nine Nine', 'Modern Family', 
                 'The Walking Dead', 'DC\'s Legends of Tomorrow', 'Supernatural']
    
get_details_parallel(tvShows)
```

Output will look as follows:
```
Legion:
Latest Episode: S01E04-Chapter 4 airdate:March 01, 2017
Next Episode on: March 08, 2017
The Expanse:
Latest Episode: S02E06-Paradigm Shift airdate:March 01, 2017
Next Episode on: March 08, 2017
The Flash (2014):
Latest Episode: S03E14-Attack on Central City (2) airdate:February 28, 2017
Next Episode on: March 07, 2017
Brooklyn Nine Nine:
Latest Episode: S04E12-The Fugitive (2) airdate:January 01, 2017
Next Episode on: April 11, 2017
Modern Family:
Latest Episode: S08E15-Finding Fizbo airdate:March 01, 2017
Next Episode on: March 08, 2017
The Walking Dead:
Latest Episode: S07E11-Hostiles and Calamities airdate:February 26, 2017
Next Episode on: March 05, 2017
DC's Legends of Tomorrow:
Latest Episode: S02E12-Camelot/3000 airdate:February 21, 2017
Next Episode on: March 07, 2017
Supernatural:
Latest Episode: S12E14-The Raid airdate:March 02, 2017
Next Episode on: March 09, 2017
```

