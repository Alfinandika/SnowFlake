from tweppy_streamer import TwitterStreamer
from ANN import classify 


hash_tag_list = ["jokowi"]
fetched_tweets_filename = "tweets.json"

twitter_streamer = TwitterStreamer()
twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

