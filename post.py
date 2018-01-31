import twitter
from credentials import tokens

api = twitter.Api(tokens['consumer_key'], tokens['consumer_secret'],
                  tokens['access_token_key'], tokens['access_token_secret'])
