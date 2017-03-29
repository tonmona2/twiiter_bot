from flask import Flask, render_template
import tweepy, time, sys
from time import sleep
from random import randint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
from flask import jsonify
from flask import request

app = Flask(__name__, template_folder="mytemplate")

# Authentication
t_consumerkey= 'ONoYgdpRdkIj592dVQJi52Qsg'
t_secretkey= 'hn9y9Y7SBK5tiHWMVUKn6PRbUBUANjUX1aXcD9vwrpoTBFp8FJ'
access_tokenkey='846743565904564224-We0haZK8x9XomN18ITn9cSxqlYwouX5'
access_tokensecret='ValzlTvpS0Gq2SJAksUvvfyxm9N3a5o8dhSLJJrZzS6Ex'



auth = tweepy.OAuthHandler(t_consumerkey, t_secretkey)
auth.set_access_token(access_tokenkey, access_tokensecret)

api = tweepy.API(auth)


@app.route('/twitter/')
def Go_bots():
	args = request.args
	article_links_array = args.getlist('article_links')
	hashtags_array = args.getlist('hashtags')
	macro_link = args['macro_link']
	tweet_text = args['tweet_text']
	
	
	search_result_article = []
	search_result_hashtag = []
	for article in article_links_array:
		search_result_article.append(api.search(article))
	
	for hashtag in hashtags_array:
		search_result_hashtag.append(api.search('#'+hashtag))
	all_tweets_text = []
	
	for tweets_a in search_result_article:
		for t in tweets_a:
		handle = "@" + t.user.screen_name
		m_a = handle + " " + macro_link
		all_tweets_text.append(m_a)
		s = api.update_status(m_a)
#		nap = randint(1, 60)
#		time.sleep(100)
	
	for tweets in search_result_hashtag:
		for tweet in tweets:
			handle = "@" + tweet.author.screen_name
			m = handle + " " + macro_link
			all_tweets_text.append(m)
	##		s = api.update_status(m)
	#		nap = randint(1, 60)
	#		time.sleep(100)

### Streaming part commented

	# name = 'bakerk200'

	# class StdOutListener(StreamListener):
		# search_result2 = api.search(name)
		
		# for t in search_result2:
			# if(t.user.screen_name is name):
				# handle2 = "@" + t.user.screen_name
				# m2 = handle2 + " " + "good"
				#####s2 = api.update_status(m2)
				# nap = randint(1, 60)
				# time.sleep(nap)

	# l = StdOutListener()
	# stream = Stream(auth, l)
	# print(search_result_article)
	# print(search_result_hashtag)
	
	
	
	return jsonify({"tweets": all_tweets_text})
    
   

if(__name__) == '__main__':
    app.run(debug=True)
