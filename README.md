# Tweeter Bot API
## INSTALL

Make sure you have python 2.7 or 3.5 installed
Install `tweepy` and `flask`


## Running the REST server

Set the following enviroment variables from your tweeter dev accont:
`TW_CONSUMERKEY`, `TW_SECRETKEY`, `TW_ACCESS_TOKENKEY`, `TW_TOKENSECRET`

from the command line run:
```
python api.py
```


## Using the REST API

There are two main functionality of the bot:
1. Search tweets for a specific link and reply to it with a specific text
2. Give the list of all tweets of a specific hashtag given


### 1. Responding to links:
url: /respond-to-links

parameters:

    article_links: links to search for (multiple can be given)
    response: the text to respond with
    
example: goto `localhost:5000/respond-to-links?article_links=fakenews.example.com&article_links=fakenews.example.org&response="Your link is a fake news site!"`

### 2. Get all tweets with hashtag
url: /hashtag-tweets

parameters:

    hashtags: list of hashtags to search for (multiple can be given)
    
example: goto `localhost:5000/hashtag-tweets?hashtags=fakenews&hashtags=fake_news`
