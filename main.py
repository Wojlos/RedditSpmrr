import json
import praw
import requests
from praw.models import InlineGif, InlineImage, InlineVideo
# subr = 'lostest'
credentials = 'client_secrets.json'


with open(credentials) as f:
    creds = json.load(f)

with open("subs.txt") as subs:
    lines = subs.readlines()
    sub_list = [line.rstrip() for line in lines]



reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])
 
 
title = 'Teams and wellbeing at work'
selftext = '''
Hi. I'm a researcher from a university in Poznań (Poland), and I'm conducting a study on employee well-being. I'm looking for people who work in different settings (including remote and hybrid). I’d like to invite you to take a short anonymous online survey (only about 9 minutes). It would be really helpful for me, if you could fill it in.

http://ioresearch.amu.edu.pl/index.php/757397?lang=eng {kot}
'''
print("spaming reddit has started...")
print("spamed subreddits:")

leftovers = []
for subr in sub_list:
    print(subr)
    try:
        subreddit = reddit.subreddit(subr)
        gif = InlineImage(path= "zebrakot.gif")
        response = subreddit.submit(title, selftext=selftext, inline_media={"kot":gif})

    except Exception as e: 
        leftovers.append({'sub': subr, "error":e})
with open("leftovers.txt","w") as file:
    for i in leftovers:
        file.write(f'{i["sub"]} - {i["error"]}\n')
