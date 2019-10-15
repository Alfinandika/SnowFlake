from threading import Thread


def streamAndClassify():
    from tweppy_streamer import TwitterStreamer

    hash_tag_list = ["openbo"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

def restApi():
    import rest
    from app import app
    if __name__ == "__main__":
        app.run()


print("SNOWFLAKE 1.0")
Thread(target = streamAndClassify).start() 
Thread(target = restApi).start()

