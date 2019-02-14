f=open("tweets.txt","r")
d=f.read()
id=[]
tweet=[]
end=0
for i in range(len(d)):
	if d[i]=='@':
		start=i+1
		for j in range(i,len(d)):
			if(d[j]=='\n'):
				end=j
				break
print(start,end)
id=d[start:end]
print("ID:"+id)

start=end+2
for i in range(start,len(d)):
	if (d[i]=='\n' and d[i+1]=='\n'):
		end=i
		break
print(start,end)
tweet=d[start:end]
print("Tweet: "+tweet)

f1=open("id.txt","w")
f1.write(id)
f2=open("tweet.txt","w")
f2.write(tweet)

f.close()
f1.close()
f2.close()



