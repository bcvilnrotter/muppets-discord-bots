# import modules
import os, argparse, random
import discord
from datetime import datetime, timezone
from discord.ext import commands
from dotenv import load_dotenv

# argument parser
arg_desc = '''\
Python Discord Bot code for bunsen-bot
--------------------------------------
'''

# initialize argparse argument
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc)

# add the argument to include TOKEN file location for beeker-bot
parser.add_argument('--token', dest='token', help='path to where the bot TOKEN is found for bunsen-bot')

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

# initialize client variable
bunsen_client = discord.Bot()

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

@bunsen_client.event
async def on_message(message):
    
    # log the message content
    log('  author: ' + str(message.author) + ' ; content: '+ message.content)

    # check if the content of the message contains an @ to beaker-bot
    if str(message.author) == 'beaker-bot#8957':
        
        # check if beaker-bot responds with 'Meep!'
        if 'Meep!' in message.content:

            # give bunsen-bots response
            await message.reply('He says hello and wishes you are doing well!')
        
        elif 'Mee-moop?' in message.content:

            # give bunsen-bots response
            await message.reply('He gives you his greetings, and asks how you are doing?')

# function to ready the bot
@bunsen_client.event
async def on_ready():
    
    # print a statment that the bot is ready to be awoken
    log('Bot awoken!')

# awaken the bot
bunsen_client.run(token)