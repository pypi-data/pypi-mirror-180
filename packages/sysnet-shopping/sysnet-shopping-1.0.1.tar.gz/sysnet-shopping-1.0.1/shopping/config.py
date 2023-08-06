import os

ELK_URL = os.getenv('ELK_URL', 'elk_address')
ELK_USERNAME = os.getenv('ELK_USERNAME', 'elk_username')
ELK_PASSWORD = os.getenv('ELK_PASSWORD', 'elk_passwd')
ELK_CERTS_DIR = os.getenv('ELK_CERTS_DIR', '')
ELK_CERTS_CA = ''
if ELK_CERTS_DIR != '':
    ELK_CERTS_CA = os.path.join(ELK_CERTS_DIR, 'ca', 'ca.pem')
ELK_VERIFY_CERTS = os.getenv("ELK_VERIFY_CERTS", 'False').lower() in ('true', '1', 't')

TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', 'abc')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', 'def')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', 'ghi')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'jkl')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', 'brum')

RUIAN_API = os.getenv("RUIAN_API", "aaa")
RUIAN_HOST = os.getenv("RUIAN_HOST", "bbb")


class ShopingError(Exception):
    pass

