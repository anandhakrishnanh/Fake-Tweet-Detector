# Fake-Tweet-Detector
This is to create a script using which we can detect fake twitter posts and check if the user mentioned in the post actually tweeted the text in the image or not.



1. We rescale the image to be analyzed (1.png) by 200% (to 2.png)
$ convert -resize 200% /home/aking/Downloads/1.png /home/aking/Downloads/2.png

-------------------------------------------------------------------------------------
2. We take our image to be analized and run an OCR called tesseract on it to detect the username and the tweet to be analyzed

install tesseract

$ pip install pillow 
$ pip install pytesseract

Next we run the tesseract on 2.png using 

$tesseract (file_path) stdout 
and store the entire details to tweets.txt

----------------------------------
3. Now we need to find out the username to be evaluated and the tweet to be checked from tweets.txt 

We run the code getidandtweet.py 

$ python getidandtweet.py 

This will store the userid into id.txt and the tweet into tweet.txt


 ----------------------------------
4. We get tweets given the name in id.txt of the user using https://github.com/gitlaura/get_tweets

You need to get your Twitter API Credentials by creating a new app at developer.twitter.com.

This script uses Tweepy. If you don't have Tweepy installed you need to run this command on the terminal first:

$ sudo pip install tweepy

Now you're ready to clone and use the get_tweets script.

$ git clone https://github.com/gitlaura/get_tweets.git
$ cd get_tweets

Enter the appropriate keys from your Twitter app in lines 11-15 of get_tweets.py using any text editor.

Finally you can run the script by entering one Twitter username at the command line:

$ python get_tweets.py [twitter_username]

We store the tweets from the user in all.csv


---------------------------------------------------------

5. Next we need to comapare if the text in tweet.txt coinsides in the all.csv. For that we run the program compare.py

$python comapre.py

-------------------------------------------------------------

All the codes are run using a shell script called fake.sh 
1. Make sure the image you are going to analyze is called 1.png 
2. Make sure that the path of the file is changed in the code 
3. I have used my Twitter credentials but you may use your own if required.
4. Give proper permission for the script using 

$ chmod +x fake.sh 

then run 

$./fake.sh





