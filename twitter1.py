import urllib
import twurl # We use this to properly format the Twitter URL for access

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    
    # URL Augment function uses TWURL to preformat our URL for API call
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '2'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    
    data = connection.read() # The body of our data
    print data[:250]
    headers = connection.info().dict # The headers
    # print headers
    print 'Remaining', headers['x-rate-limit-remaining']
