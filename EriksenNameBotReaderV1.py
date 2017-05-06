import praw
import pdb
import re
import os
import datetime

#Creates reddit instance
reddit = praw.Reddit('CoysEriksenReaderBot')

#subreddit = reddit.subreddit("learnpython")

#Have this code run befor? if not then create an empty list
if not os.path.isfile("posts_read_and_pm.txt"):
	posts_read_and_pm = []
#if yes then load the list of posts we have replied to
else:
	#Read the file into a list and remove any empty values
	with open("posts_read_and_pm.txt", "r") as f:
		posts_read_and_pm = f.read()
		posts_read_and_pm = posts_read_and_pm.split("\n")
		posts_read_and_pm = list(filter(None, posts_read_and_pm))

#Get the top 5 values from our subreddit
subreddit = reddit.subreddit("coys")

comment = ""
commentUser = ""
searchword = "eriksen"
searchmisspelledWord = "erikson"

for submission in subreddit.hot(limit=5):
	
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():


		if word in comment.body.lower():
			#print("\n" + submission.title + "\n")

			commentUser = comment.author
			#print(commentUser)

			#print("Comment: ", comment.body)
			ifCheck = submission.id + "/" + comment.id
			#If we have not replied to this post before
			if ifCheck not in posts_read_and_pm:

				#Do a case insensitive search
				if re.search(searchword, comment.body, re.IGNORECASE):
					text = str(comment.body)
					user = str(commentUser)
					#Tiden er forkert, så det skal ses på
					date = str(datetime.datetime.fromtimestamp(comment.created))

					#Reply to post
					postMessage = "**" + user + "**\n\n" + text + "\n\n*" + date + "*" + "\n\n[Permalink](https://www.reddit.com/r/coys/comments/" + submission.id + "/" + submission.title + "/" + comment.id + ")"
					
					reddit.redditor('Zenkou').message(submission.title, postMessage)
					#Store the current id into our list
					posts_read_and_pm.append(submission.id + "/" + comment.id)

			#Write our updated list back to the file
			with open("posts_read_and_pm.txt", "w") as f:
				for post_id in posts_read_and_pm:
					f.write(post_id + "\n")

		elif searchmisspelledWord in comment.body.lower():

			commentUser = comment.author


			ifCheck = submission.id + "/" + comment.id
			#If we have not replied to this post before
			if ifCheck not in posts_read_and_pm:

				#Do a case insensitive search
				if re.search(word, comment.body, re.IGNORECASE):
					text = str(comment.body)
					user = str(commentUser)
					#Tiden er forkert, så det skal ses på
					date = str(datetime.datetime.fromtimestamp(comment.created))

					#Reply to post
					postMessage = "**" + user + "**\n\n" + text + "\n\n*" + date + "*" + "\n\n[Permalink](https://www.reddit.com/r/coys/comments/" + submission.id + "/" + submission.title + "/" + comment.id + ")"
					
					reddit.redditor('Zenkou').message(submission.title, postMessage)
					#Store the current id into our list
					posts_read_and_pm.append(submission.id + "/" + comment.id)

			#Write our updated list back to the file
			with open("posts_read_and_pm.txt", "w") as f:
				for post_id in posts_read_and_pm:
					f.write(post_id + "\n")
			#print("Comment: ", comment.body)
	

