import pandas
df=pandas.read_csv('all.csv')
print(df['tweet'][0:])
f=open('tweet.txt',"r")
tweet=f.read()
print(tweet)
df=str(df)
if tweet in df:
	print("Tweet Confirmed")
