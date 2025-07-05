# پلاگین echo: با دستور /echo متن بعدی را تکرار می‌کند

def handle(client, update):
    msg = update.message
    if msg and getattr(msg, 'text', '').startswith('/echo '):
        text = msg.text[len('/echo '):]
        client.send_message(msg.chat.id, text)
