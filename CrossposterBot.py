import time
import praw

USERNAME = "username"
PASSWORD = "password"
SUBMISSION_LIMIT = 10

subreddits = ['the', 'subreddits', 'that', 'youwant', 'toxpost', 'from']
targetSubreddit = 'subredditWhereYouWantToPostThings'
alreadyDone = set()

r = praw.Reddit("Multi-subreddit link aggregator and crossposter")
r.login(USERNAME, PASSWORD)

while True:
    try:
        for subreddit in [r.get_subreddit(subredditName) for subredditName in subreddits]:
            for submission in subreddit.get_new(limit = SUBMISSION_LIMIT):
                if (submission.id not in alreadyDone):
                    alreadyDone.add(submission.id)
                    print "Submitting", submission.url
                    r.submit(targetSubreddit, submission.title + '[X-POST r\/' + subreddit + ']', url = submission.url)
        time.sleep(600)