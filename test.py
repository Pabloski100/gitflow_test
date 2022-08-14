
import json

def top_retweeted():
    
    tweet_list = []
    max_tweet = []

    with open("./farmers-protest-tweets-2021-03-5.json") as file:

        for line in file:
            data = json.loads(line)
            tweet_list.append(data)

    for i in range(10):
        tweet_i = max(tweet_list, key=lambda x: int(x["retweetCount"]))
        tweet_list.remove(tweet_i)
        max_tweet.append(tweet_i)

    return max_tweet

def top_users():
    pass

def top_days():
    pass

def top_hashtags():
    pass

if __name__ == "__main__":
    print("Main")
    # Llamar funciones aqui