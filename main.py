from threading import Thread


def streamAndClassify():
    from tweppy_streamer import TwitterStreamer

    hash_tag_list = ["openbo"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

def restApi():
    print("contoh aja seh")

Thread(target = streamAndClassify).start() 
Thread(target = restApi).start() 
