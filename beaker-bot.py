# import modules
import os, argparse, random
import discord
from datetime import datetime, timezone
from discord.ext import commands
from dotenv import load_dotenv

# argument parser
arg_desc = '''\
Python Discord Bot code for beaker-bot
--------------------------------------
'''

# initialize argparse argument
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc)

# add the argument to include TOKEN file location for beeker-bot
parser.add_argument('--token', dest='token', help='path to where the bot TOKEN is found for beaker_bot')

# parse the arguments
args = parser.parse_args()

# check if a token path isn't provided
if args.token is None:

    # print that the script is ending
    print("script ending, all tokens not provided:")

    # exit the script
    exit()

# function for reading TOKEN files
def read_token(token_path):

    # open the provided token file path
    with open(token_path, "r") as f:

        # initialize token
        token = f.readline()
    
    # return the TOKEN value
    return token

load_dotenv()

# initialize list of responses to @ messages
responses = [
    '<@1058656154928025620> Meep!',
    '<@1058656154928025620> Mee-moop?'
]

# initialize client variable
beaker_client = discord.Bot()

# collect the token for beaker-bot
token = read_token(args.token)

# initialize the logging function
def log(message, type='info'):

    # get the current time
    now = datetime.now(timezone.utc)

    # combine the string for the log entry
    entry = str(now) + " [" + str(type) + "] " + str(message)

    # print the log entry to console
    print(entry)

@beaker_client.event
async def on_message(message):
    
    # log the message content
    log('  author: ' + str(message.author) + ' ; content: '+ message.content)

    # check if the content of the message contains an @ to beaker-bot
    if '<@1058619141042483240>' in message.content:
        
        # randomly choose a response from the list of responses
        response = random.choice(responses)

        # relay the response to the discord server
        await message.reply(response)

# function to ready the bot
@beaker_client.event
async def on_ready():
    
    # print a statment that the bot is ready to be awoken
    log('Bot awoken!')

# awaken the bot
beaker_client.run(token)