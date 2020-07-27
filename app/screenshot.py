import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app.settings import SCREENSHOT_WIDTH, SCREENSHOT_HEIGHT


def get_screenshot(url, chat_id):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1920, total_height)
    driver.get(url)

    time.sleep(2)

    full_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(SCREENSHOT_WIDTH, full_height if full_height > 0 else SCREENSHOT_HEIGHT)

    time.sleep(2)

    file = os.path.join(SCREENSHOT_PATH, (chat_id + '{}').format('.png'))
    driver.save_screenshot(file)
    driver.quit()

    return file
