from missvend.sample_config import Config


class Development(Config):
    OWNER_ID = 611024837  # my telegram ID
    OWNER_USERNAME = "john_s_n_i"  # my telegram username
    API_KEY = "2135069792:AAFiwkwHzd6KakbnE-znWa1UYUXZrgar67w"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://yzwgsujuwuyttn:679bd9c13e143767db9bbb85e58fd5992320e15b7808d9617d7eb949b9f1f657@ec2-52-72-155-37.compute-1.amazonaws.com:5432/d5s5asrar6ftra'  # sample db credentials
    MESSAGE_DUMP = '' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    KICK_STICKER =''
    OWNER_USERNAME = "YOUR USERNAME HERE"
    TELETHON_HASH = '9fce6e4f4bddfbc6ae768cbf109eadcc'  # for purge stuffs
    TELETHON_ID = '7336626'

    # RECOMMENDED
    GBAN_LOGS = ''
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = '8443'
    URL = 'https://miss-vend.herokuapp.com/'

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = [611024837]  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = [611024837]  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = [611024837]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [611024837]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SPAMMERS = ''
    DONATION_LINK = 'pearldrift.com'  # EG, paypal
    CERT_PATH = ''
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    SW_API = ''
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAIHsl5nbqXdDTmpG2HFDNhnwvE5kFbWAAI9AQAC3pTNLzeTCUmnhTneGAQ'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = '' # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = '' # Get one from https://timezonedb.com/register
    WALL_API = ''
    LASTFM_API_KEY = ''
    LYDIA_API = ''
    API_OPENWEATHER = ''
