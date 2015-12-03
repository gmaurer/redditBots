import praw
import re
import string


r = praw.Reddit(user_agent='Test Script by /u/test_b0t_69')

alreadyChecked = []
newX = ""

def railFenceEncrypt(submissions):
	print submissions
	#do rail encrypt on input


def removeLetters(submissions):
	
	for comment in submissions:
	#r.get_subreddit('bmw').get_comments(limit = 2):
		rletter = ['a','e','i','o','u',"'",'.',',']
		x = comment.body
		newX = x
		print newX
		for b in range(len(rletter)):
			
			newX = string.replace(newX,rletter[b],'')
		
		newX = string.replace(newX," ","")
		print newX
		



def logOn(user,passw):
	r.login(user , passw , disable_warning=True)




def getKarma(user1):
	user = r.get_redditor(user1)
	print user.link_karma
	print user.comment_karma




def findSub():
	submissions = r.get_subreddit('bmw').get_comments(limit=2)




	removeLetters(submissions)



logOn('test_bot_69','testing1234')
findSub()



