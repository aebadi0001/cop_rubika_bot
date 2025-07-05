from rubpy import Client, Update
from bot.config import TOKEN
import os, importlib

def load_plugins():
    base = os.path.join(os.path.dirname(__file__), 'plugins')
    modules = []
    for fn in os.listdir(base):
        if fn.endswith('.py') and fn != '__init__.py':
            name = fn[:-3]
            mod = importlib.import_module(f'bot.plugins.{name}')
            if hasattr(mod, 'handle'):
                modules.append(mod)
    return modules

def main():
    client = Client(TOKEN)
    plugins = load_plugins()

    @client.on_update
    def dispatcher(update: Update):
        for plugin in plugins:
            try:
                plugin.handle(client, update)
            except Exception as e:
                print(f"[{plugin.__name__}] error:", e)

    print("Bot started.")
    client.run_polling()

if __name__ == '__main__':
    main()
