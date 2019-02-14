#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "aLGCFxN214ojBfOdrZz2K6n0T"
consumer_secret = "IrCnFawYC2HsYwesiM8gyzNQ7HDMYA45QQCF9K4g7arbqF3ppf"
access_key = "1298808518-WzlYMPICgEeOUXtvsYyAIXeSr2zt8Dir7F8eI4y"
access_secret = "LaF6taoqOdG3TpVw5EaJW5DQ4zMoA756LNsGbW0p7Bw8e"

#method to get a user's last tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 10

	#get tweets
	tweets_for_csv = []
	tweets_for_csv.append(["username", "tweet.id", "tweet created at", "tweet"])
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

	#write to a new csv file from the array of tweets
	outfile = "all.csv"
	print "writing to " + outfile
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

f=open("id.txt","r")
userid=f.read()
#userid="KimKardashian"
print(userid)
get_tweets(userid)
f.close()


