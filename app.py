import json, tweepy, os, time, random, datetime
from os import environ
# tweepy documentation: http://docs.tweepy.org/en/latest/

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

def lambda_handler(event, context):
    # TODO implement
    tweet_quote()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

current_date = datetime.datetime.now()

quotes = [
    'You miss 100% of the shots you don\'t take - Wayne Gretzky - Michael Scott',
    'The greatest wealth is to live content with little - Plato',
    'Great minds discuss ideas. Average minds discuss events. Small minds discuss people. - Eleanor Roosevelt',
    'There is no greater agony than bearing an untold story inside you - May Angelou',
    'Could a greater miracle take place than for us to look through each other\'s eyes for an instant? - Henry David Thoreau',
    'One of the greatest diseases is to be nobody to anybody - Mother Teresa',
    'The greatest way to live with honor in this world is to be what we pretend to be - Socrate',
    'No one ever injured their eyesight by looking on the bright side',
    'Luck is just when preparation meets opportunity',
    'The more aware you are of your stressful thoughts and feelings, the more you can reframe how you process them - Karl Staib',
    'Ever tried. Ever failed. No matter. Try again. Fail again. Fail BETTER.',
    'We tell people to follow their dreams, but you can only dream of what you can imagine - Trevor Noah',
    'The rich invest in time, the poor invest in money. - Warren Buffet',
    'The more you learn, the more you earn. - Warren Buffet',
    'Everything negative - pressure, challenges - is all an opportunity for me to rise. - Kobe Bryant',
    'You have to see failure as the beginning and the middle, but never entertain it as an end - Jessica Herrin',
    'If we tried to think of a good idea, we would not have been able to think of a good idea. You just have to find the solution for a problem in your own life. - Brian Chesky',
    'If you are not willing to downgrade your lifestyle for a year to have a lifestyle you want forever, you care too much about what other people think. - Jim Carrey',
]

# twitter doesn't allow tweets of exact duplicate text so this appends the date to ensure every tweet is unique
def tweet_quote():
    api.update_status(str(current_date) + ' // ' + random.choice(quotes))





