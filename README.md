# Music Aggregator Reddit Bot

## Installation

1. Install python 3.8+.
2. Install [Poetry](https://python-poetry.org/docs/#installation/)
3. `cd` into the project directory and run `poetry install` to install dependencies.
4. Create a config file based on the example in the project root folder at `instance/config.json`
5. From the project root, run `poetry run python -m musicAggregator`.

## Limitations

All the bot's submissions will end up in spam if the bot is a low karma account. They can be manually approved by a moderator.

## Example config

```json
{
    "VERSION": "0.1",
    "REDDIT_ID": "YOUR_DEETS",
    "REDDIT_SECRET": "YOUR_DEETS",
    "REDDIT_USER": "YOUR_DEETS",
    "REDDIT_PASS": "YOUR_DEETS",
    "MULTIREDDITS": [
        ["awesomeautism", "another_100_music"],
        ["awesomeautism", "100_music"],
        ["awesomeautism", "yet_again_another_100_music"],
        ["awesomeautism", "yet_another_100_music"]
    ],
    "TARGET_SUBREDDIT": "BotTestingGround13",
    "WANTED_URLS": [
        "youtu.be",
        "v.redd.it",
        "soundcloud.com",
        "m.soundcloud.com",
        "youtube.com",
        "bandcamp.com",
        "open.spotify.com"
    ]
}
```