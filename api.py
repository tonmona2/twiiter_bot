from flask import Flask, render_template
import tweepy, time, sys
from time import sleep
from random import randint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
from flask import jsonify
from flask import request
import os

app = Flask(__name__, template_folder="mytemplate")

# Authentication
try:
	t_consumerkey=os.environ['TW_CONSUMERKEY']
	t_secretkey=os.environ['TW_SECRETKEY']
	access_tokenkey=os.environ['TW_ACCESS_TOKENKEY']
	access_tokensecret=os.environ['TW_TOKENSECRET']
except KeyError: 
	print("You need to set the environment variables: TW_CONSUMERKEY, TW_SECRETKEY, TW_ACCESS_TOKENKEY, TW_TOKENSECRET")
	sys.exit(1)


auth = tweepy.OAuthHandler(t_consumerkey, t_secretkey)
auth.set_access_token(access_tokenkey, access_tokensecret)

api = tweepy.API(auth)


@app.route('/respond-to-links/')
def respond_article():
	args = request.args
	article_links_array = args.getlist('article_links')
	macro_link = args['resonse']
	
	search_result_article = []

	for article in article_links_array:
		search_result_article.append(api.search(article))
	
	for tweets_a in search_result_article:
		for t in tweets_a:
			handle = "@" + t.user.screen_name
			m_a = handle + " " + macro_link
			all_tweets_text.append(m_a)
			s = api.update_status(m_a)
			time.sleep(50)


            
@app.route('/hashtag-tweets/')
def get_hashtag_tweets():
	search_result_hashtag = []
	hashtags_array = args.getlist('hashtags')
	for hashtag in hashtags_array:
		search_result_hashtag.append(api.search('#'+hashtag))
	all_tweets_text = []

	for tweets in search_result_hashtag:
		for tweet in tweets:
			handle = "@" + tweet.author.screen_name
			m = handle + " " + tweet.text
			all_tweets_text.append(m)
			time.sleep(50)

	
	return jsonify({"tweets": all_tweets_text})
    
   

if(__name__) == '__main__':
    app.run(debug=True)
