import os
import logging

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', None)
API_ENDPOINT = 'https://api.telegram.org/bot{}/'
API_URL = API_ENDPOINT.format(BOT_TOKEN)

WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')
WEBHOOK_PORT = os.getenv('WEBHOOK_PORT', 8888)

SCREENSHOT_WIDTH = os.getenv('SCREENSHOT_WIDTH', 1920)
SCREENSHOT_HEIGHT = os.getenv('SCREENSHOT_HEIGHT', 1200)
SCREENSHOT_PATH = os.getenv('SCREENSHOT_PATH', os.path.join(os.getcwd(), 'screenshots'))

LOG_LEVEL = logging.WARNING
if os.getenv('DEBUG', False):
    LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL)
