import tvdb_api
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_date_obj(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def get_readable_date(date_string):
    return get_date_obj(date_string).strftime("%B %d, %Y")

def prefix_withzero(num):
    if num >= 10:
        return str(num)
    return '0' + str(num)

def get_last_in_season(tvShowName, season, t):
    epi = 1
    while 1:
        try:
            episode = t[tvShowName][season][epi]
        except tvdb_api.tvdb_episodenotfound:
            return epi - 1
        epi += 1

def get_previous_episode(tvShowName, season, episode, t):
    if(episode > 1):
        return season, episode - 1
    if(season > 1):
        return season - 1, get_last_in_season(tvShowName, season - 1, t)
    return 0, 0

def get_latest_episode(tvShowName, t):
    season = 1
    epi = 1
    latest_episode = 0
    latest_season = 0
    today = datetime.today()
    while 1:
        try:
            episode = t[tvShowName][season][epi]
        except tvdb_api.tvdb_episodenotfound:
            #print "Episode {} not found in season {}".format(epi, season)
            latest_season = season
            season += 1
            latest_episode = epi - 1
            epi = 1
            continue
        except tvdb_api.tvdb_seasonnotfound:
            #print "Season {} not found. Episode searched was {}".format(season, epi)
            return latest_season, latest_episode, 'Unknown'
        airdateString = episode['firstaired']
        if airdateString is not None:
            if today < get_date_obj(airdateString):
                season, epi = get_previous_episode(tvShowName, season, epi, t)
                return season, epi, airdateString
        epi += 1

def get_details(tvShowName):
    t = tvdb_api.Tvdb()
    season, episode, nextDateString = get_latest_episode(tvShowName, t)
    episode_details = t[tvShowName][season][episode]
    S = prefix_withzero(season)
    E = prefix_withzero(episode)
    airdateString = get_readable_date(episode_details['firstaired'])
    if nextDateString != 'Unknown':
        nextDateString = get_readable_date(nextDateString)
    details_string = "{}:\nLatest Episode: S{}E{}-{} airdate:{}\nNext Episode on: {}".format(tvShowName, S, E, episode_details['episodename'], airdateString, nextDateString)
    return details_string

def wait_for_futures(futures):
    for future in futures:
        print future.result()

def get_details_parallel(tvShows):
    pool = ThreadPoolExecutor(len(tvShows))
    futures = []

    for tvShowName in tvShows:
        futures.append(pool.submit(get_details, tvShowName))

    wait_for_futures(futures)
