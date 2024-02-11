import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6231854988:AAFeocYwK1rUB9e4cTF03U8OeQgwI9o9lNE")

    APP_ID = int(os.environ.get("APP_ID", 22855766))

    API_HASH = os.environ.get("API_HASH", "7d0193262ccfa7dc7eae7fb6917cf3db")
