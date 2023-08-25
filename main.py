import json
import time
import requests
import tweepy
import credentials

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET


def get_quote():
    response = requests.get("https://api.gurbaninow.com/v2/shabad/random")
    json_data = json.loads(response.text)



#test, delete later
    quote1 = ""
    line = json_data['shabad'][-1]
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





    line = json_data['shabad'][0]

    quote = line['line']['gurmukhi']['unicode']
    quote += '\n'
#    quote += line['line']['translation']['punjabi']['default']['unicode']
#    quote += '\n'
    quote += line['line']['translation']['english']['default']

#    for line in json_data['shabad']:
#
#        quote += line['line']['gurmukhi']['unicode']
#        quote += '\n'
#        #quote += line['line']['translation']['punjabi']['default']['unicode']
#        #quote += '\n'
#        quote += line['line']['translation']['english']['default']
#        quote += '\n'
    listOfWords = ["Mehla", "Salok", "Jee", "Pauree", "Shalok", "Mehl", "By The Grace Of The True Guru", "Ashtapadee"]


    if any(word in quote for word in listOfWords):
        quote1 = ""
        line = json_data['shabad'][-1]
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




    quote += '\n'
    quote += json_data['shabadinfo']['writer']['english']
    quote += ': '
    quote += str(json_data['shabadinfo']['pageno'])

#    json_data['shabad'][0]['line']['gurmukhi']['unicode']

    return quote


def tweet_quote():
    interval = 60*60

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

#    quote = "ਨਾਨਕ ਜਨ ਹਰਿ ਕਥਾ ਸੁਣਿ ਤ੍ਰਿਪਤੇ ਜਪਿ ਹਰਿ ਹਰਿ ਹਰਿ ਹੋਵੰਤੀ ॥੨॥੨॥੮॥ \n"
#    quote +="The Supreme guru says, those who have understood the almighty and chant the name, Har Har, themselves become like the almighty \n"
#    quote += "ਸ੍ਰੀ ਗੁਰੂ ਜੀ ਕਹਤੇ ਹੈਂ: ਸੇ ਜਨ ਹਰੀ ਕੀ ਕਥਾ ਸੁਨ ਕੇ ਤ੍ਰਿਪਤ ਹੂਏ ਹੈਂ ਔ ਹਰੀ ਹਰਿ ਨਾਮ ਕੋ ਜਪ ਕੇ ਬ੍ਰਿਤੀ ਹਰੀ ਰੂਪ ਹੀ ਹੋ ਗਈ ਹੈ॥੨॥੨॥੮॥"
#    test_tweet = quote
#    api.update_status(test_tweet)

    while True:
        try:
            quote = get_quote()
            print('Sending Tweet')
            print('\n')
            print(quote)
            test_tweet = quote
            api.update_status(test_tweet)
            time.sleep(interval)
        except tweepy.errors.TweepyException as e:
            print("length over")


if __name__ == "__main__":
    tweet_quote()
