import tweepy, random, time

ACCESS_TOKEN = 'Your Access Token Key Here'
ACCESS_TOKEN_SECRET = 'Your Access Token Secret Key Here'
API_KEY = 'Your API Key Here'
API_SECRET_KEY = 'Your Api Secret Key Here'

#setting up the api
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

substring = 'mycanada'

#create list of articles 
articles = []
file = open("articles.txt")
for line in file:
	articles.append(line.rstrip())

#retrieve the first tweet's id to pass into the while loop's mention_timeline 
first_tweet = api.mentions_timeline(count='1')
last_seen_id = first_tweet[0].id
check = False 

while True: 
	if check:
		#read the file containing the latest tweet id
		with open("id_file.text") as f:
			last_seen_id = f.readline().rstrip()
	  
	try: 
		mentions = api.mentions_timeline(last_seen_id)

		#update last_seen_id and check if it exists
		last_seen_id = mentions[0].id #mentions[0] is the last tweet retrieved in mentions_timeline(last_seen_id)
		if last_seen_id: #if this exists, then somebody tweeted in the 15 seconds, if not, nobody tweeted so no need to check
			counter = 0
			for mention in mentions:
				if substring in mention.text.lower():
					article = random.choice(articles)
					api.update_status("Here's todays article. \n" + article, mention.id, True)
					counter+=1
			print("Replied to " + str(counter) + " tweet(s)")		
	except:
		print("No new tweets contain the specified hashtag")

	with open("id_file.text", "w") as f:
		f.write(str(last_seen_id))

	check = True
	time.sleep(15)