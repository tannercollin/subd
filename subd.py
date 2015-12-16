from time import sleep
from instapush import App
import praw

# Set up Instapush
apisecret = open('apisecret.txt').read().strip()
app = App('566f99bea4c48aba38ea4fe7', apisecret)

# Set up Praw
r = praw.Reddit(user_agent='Just something to alert me of new submissions. Github:tannercollin')
subreddit = r.get_subreddit('bapcsalescanada')

def get_titles( subreddit ):
    try:
        submissions = subreddit.get_new(limit=5)
    except:
        print "Error getting submissions."
        return []
    titles = []
    try:
        for post in submissions:
            titles.append(post.title.encode('ascii', errors='ignore'))
    except:
        print "Error parsing titles"
    return titles

previous = []
while not previous:
    previous = get_titles(subreddit)
    sleep(10)

while True:
    current = get_titles(subreddit)
    if not current:
        continue
    for title in list(set(current) - set(previous)):
        print title
        app.notify(event_name='newpost', trackers={'title': title})
    previous = current
    sleep(10)
