from dotenv import load_dotenv 
import os
from threading import Thread
import logging
import asyncio
from subprocess import Popen


# local import
from bot import startBot
from src.app import run_flask_app

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Thread function to run Flask app in a separate thread in production
def flask_thread(func):
    thread = Thread(target=func)
    print('Start Separate Thread from Bot')
    thread.start()

if __name__ == '__main__':
    load_dotenv('./.env')
    
    if os.getenv('ENV') == 'prod':
        print('prod environment, running bot and flask app')
        flask_thread(func=run_flask_app)
        startBot(os.getenv('DISCORD_TOKEN'))
    elif os.getenv('ENV') == 'dev':
        print('dev environment, running flask app only')
        run_flask_app()
    else:
        # default to dev environment
        print('No ENV set, defaulting to dev environment')
        print('dev environment, running flask app only')
        run_flask_app()