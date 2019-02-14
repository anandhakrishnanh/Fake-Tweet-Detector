#!/bin/bash

#We resize the image by 200% (1.png to 200% 2.png)
convert -resize 200% /home/aking/Downloads/4.png /home/aking/Downloads/5.png

#first we get the text from the image using ocr and store it into gettweet.csv
tesseract /home/aking/Downloads/5.png stdout > tweets.txt

#now we take the gettweet.csv and get the text and id store it to file id.csv and tweet.csv
python getidandtweet.py

#now to get all the tweets from the user in id.txt created by getidandtweet.py
python get_tweets.py

#now we need to compare the tweets in all.csv and tweet.txt and check if there is any tweet.txt in all.csv
python compare.py

