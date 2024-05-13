from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import json, os, string, sys, threading, logging, time, re, random
import openai

# OpenAI API key
aienv = os.getenv('OPENAI_KEY')
if aienv == None:
  openai.api_key = "sk-diliplokesh-NXd9an6KauGsy84KSNfXT3BlbkFJ9rKXy7DdLjQ7NWUHMaqw"
else:
  openai.api_key = aienv
print(aienv)

# Telegram bot key
tgenv = os.getenv('TELEGRAM_KEY')
if tgenv == None:
  tgkey = "7006737577:AAEDoGJOZefgHvfklwMEZ5qbdDzEkY5JRsA"
else:
  tgkey = tgenv
print(tgenv)

# Lots of console output
debug = True

# User session timeout
timstart = 300
tim = 1

# Defaults
user = ""
running = False
cache = None
qcache = None
chat_log = None
botname = 'Harshit Ethic'
username = 'harshitethic_bot'
# Max chat log length (A token is about 4 letters and max tokens is 2048)
max = int(3000)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


##################
# Command handlers
##################
def start(bot, update):
  """Send a message when the command /start is issued."""
  global chat_log
  global qcache
  global cache
  global tim
  global botname
  global username
  left = str(tim)
  if tim == 1:
    chat_log = None
    cache = None
    qcache = None
    botname = 'Harshit Ethic'
    username = 'harshitethic_bot'
    update.message.reply_text('Hi')
    return
  else:
    update.message.reply_text('I am currently talking to someone else. Can you please wait ' + left + ' seconds?')
    return


def help(bot, update):
  """Send a message when the command /help is issued."""
  update.message.reply_text('[/reset] resets the conversation,\n [/retry] retries the last output,\n [/username name] sets your name to the bot, default is "Human",\n [/botname name] sets the bots character name, default is "AI"')


def reset(bot, update):
  """Send a message when the command /reset is issued."""
  global chat_log
  global cache
  global qcache
  global tim
  global botname
  global username
  left = str(tim)
  if user == update.message.from_user.id:
    chat_log = None
    cache = None
    qcache = None
    botname = 'Harshit Ethic'
    username = 'harshitethic_bot'
    update.message.reply_text('Bot has been reset, send a message!')
    return
  if tim == 1:
    chat_log = None
    cache = None
    qcache = None
    botname = 'Harshit Ethic'
    username = 'harshitethic_bot'
    update.message.reply_text('Bot has been reset, send a message!')
    return
  else:
    update.message.reply_text('I am currently talking to someone else. Can you please wait ' + left + ' seconds?')
    return


def retry(bot, update):
  """Send a message when the command /retry is issued."""
  global chat_log
  global cache
  global qcache
  global tim
  global botname
  global username
  left = str(tim)
  if user == update.message.from_user.id:
    new = True
    comput = threading.Thread(target=wait, args=(bot, update, botname, username, new,))
    comput.start()
    return
  if tim == 1:
    chat_log = None
    cache = None
    qcache = None
    botname = 'Harshit Ethic'
    username = 'h
