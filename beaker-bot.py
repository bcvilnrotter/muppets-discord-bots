# import modules
import os, argparse, random
import discord
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
    'Meep!',
    'Mee-moop?'
]

# initialize client variable
client = discord.Bot()

# collect the token for beaker-bot
token = read_token(args.token)

@client.event
async def on_message(message):
    if (message.content)[:2] == "<@":
        response = random.choice(responses)
        await message.reply(response)

# function to ready the bot
@client.event
async def on_ready():
    
    # print a statment that the bot is ready to be awoken
    print("Meep!")

# awaken the bot
client.run(token)