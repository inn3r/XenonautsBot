import praw
import time

bot = praw.Reddit('XenonautsBot')
subreddit = bot.subreddit('test')
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    if 'summon xenonauts' in text.lower():
        message = "Sagiri is a lovely maiden"
        comment.reply(message)
        time.sleep(45)
