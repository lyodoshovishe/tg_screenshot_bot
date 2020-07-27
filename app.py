import logging
import tornado.ioloop
import tornado.web
import requests

from app.handler import Handler
from app.settings import API_URL, WEBHOOK_URL, WEBHOOK_PORT


def make_app():
    return tornado.web.Application([
        (r'/', Handler),
    ])


if __name__ == '__main__':
    set_hook = requests.get(API_URL + 'setWebhook?url={}'.format(WEBHOOK_URL))
    if set_hook.status_code != 200:
        logging.error('Can\'t set hook: {}. Quit.'.format(set_hook.text))
        exit(1)

    app = make_app()
    app.listen(WEBHOOK_PORT)
    tornado.ioloop.IOLoop.current().start()

    logging.info('Bot started at {} port'.format(WEBHOOK_PORT))

