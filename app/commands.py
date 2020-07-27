from urllib.parse import urlparse

from .screenshot import get_screenshot

def help_msg(message):
    response = {'chat_id': message['chat']['id']}
    result = ["Hey, %s!" % message["from"].get("first_name"),
              "\rI can accept only these commands:"]

    for command in CMD:
        result.append(command)

    response['text'] = "\n\t".join(result)
    return response


def screenshot_msg(message):
    response = {'chat_id': message['chat']['id']}

    parsedUrl = urlparse(message['text'])
    if not parsedUrl.schema and not parseUrl.netloc:
        response['text'] = 'Invalid url'
    else:
        response['photo'] = get_screenshot(message['text'], message['chat']['id'])

    return response


def not_found_msg(message):
    return {
        'chat_id': message['chat']['id'],
        'text': 'Command not found',
    }


cmd = {
    'help': help_msg,
}
