import json
import time
import requests
import tweepy
import credentials

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret_key,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

quote1 = ''
def get_quote():
    response = requests.get("https://api.gurbaninow.com/v2/shabad/random")
    json_data = json.loads(response.text)

    quote1 = ""
    line = json_data['shabad'][1]
    quote1 += line['line']['gurmukhi']['unicode']
    quote1 += '\n'
    #quote += line['line']['translation']['punjabi']['default']['unicode']
    #quote += '\n'
    quote1 += line['line']['translation']['english']['default']
    quote1 += '\n'

    quote1 += json_data['shabadinfo']['writer']['english']
    quote1 += ': '
    quote1 += str(json_data['shabadinfo']['pageno'])
    return quote1

compquote = 'ੴ'
quote1 = ''

def tweet_quote():
    interval = 60*60
    
    while True:
        try:
            while compquote not in quote1:
                quote = get_quote()
                break
            print('Sending Tweet')
            print('\n')
            print(quote)
            test_tweet = quote
            response = client.create_tweet(text=test_tweet)
            print(response)
            time.sleep(interval)
        except tweepy.errors.TweepyException as e:
            print("length over")



if __name__ == "__main__":
    tweet_quote()
