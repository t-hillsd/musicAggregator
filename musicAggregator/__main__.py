from collections import deque

import praw
from loguru import logger

from musicAggregator.config import Config

config = Config.config()


def read_subreddits_list():
    subs = []
    for (user, multireddit) in config.MULTIREDDITS:
        subs += [x.display_name for x in r.multireddit(user, multireddit).subreddits]
    return "+".join(subs)


def is_music_link(submission):
    for base_url in config.WANTED_URLS:
        if base_url in submission.url:
            return True


def get_wanted_posts(r, subs_string):
    seen_recently = deque(maxlen=1000)

    for submission in r.subreddit(subs_string).stream.submissions(skip_existing=False):  # TODO
        if is_music_link(submission) and submission.url not in seen_recently:
            seen_recently.append(submission.url)
            yield submission


def run(r):
    for s in get_wanted_posts(r, read_subreddits_list()):
        s.crosspost(subreddit=config.TARGET_SUBREDDIT)
        logger.debug([s.title, s.url])


if __name__ == "__main__":
    r = praw.Reddit(
        client_id=config.REDDIT_ID,
        client_secret=config.REDDIT_SECRET,
        user_agent=config.USER_AGENT,
        username=config.REDDIT_USER,
        password=config.REDDIT_PASS,
    )

    with logger.catch():
        run(r)
