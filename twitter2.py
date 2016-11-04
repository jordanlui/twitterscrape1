import urllib
import twurl
import json

# Retrieves friend list data from twitter

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'



while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '5'} ) # we only grab the latest 5 users
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read() # Body JSON Data
    headers = connection.info().dict # JSON Header data. Includes the x rate limit remaining
    print 'Remaining', headers['x-rate-limit-remaining']
    
    js = json.loads(data) # json  load the body data

    print json.dumps(js, indent=4) # Pretty print with indent 4

    for u in js['users'] :
        print u['screen_name']
        s = u['status']['text']
        print '  ',s[:50] # Print the first 50 characters of each tweet
