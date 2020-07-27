import os
import logging
import tornado.web
import tornado.escape
import requests

from .commands import cmd, not_found_msg, screenshot_msg
from .settings import API_URL


class Handler(tornado.web.RequestHandler):
    def post(self):
        try:
            logging.debug('Got request: {}'.format(self.request.body))
            update = tornado.escape.json_decode(self.request.body)
            message = update['message']
            text = message.get('text')
            if text:
                logging.debug('MESSAGE\t{}\t{}'.format(message['chat']['id'], text))

                if text[0] == '/':
                    command = text[1:].split(" ", 1)[0]
                    response = cmd.get(command, not_found_msg)(message)
                    logging.debug('REPLY{}%s{}%s'.format(message['chat']['id'], response))
                else:
                    response = screenshot_msg(message)

                    if 'text' in response:
                        requests.post(API_URL + 'sendMessage', data=response)
                    elif 'photo' in response:
                        filename = response.pop('photo')
                        with open(filename, 'rb') as photo_content:
                            requests.post(API_URL + 'sendPhoto', data=response, files={'photo': photo_content})
                        os.remove(filename)

        except Exception as e:
            logging.warning(str(e))
