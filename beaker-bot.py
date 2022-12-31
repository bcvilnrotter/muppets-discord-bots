# import modules
import os, argparse, random
import discord
from dotenv import load_dotenv

# argument parser
arg_desc = '''\
Python Discord Bot code for beaker-bot
--------------------------------------
'''

# initialize argparse argument
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc)

# add the argument to included TOKEN file location
parser.add_argument('-t', '--token', dest='token', help='path to where the bots TOKEN is found')

# parse the arguments
args = parser.parse_args()

# check if a token path isn't provided
if not args.token:

    # print that the script is ending
    print("script ending, no token provided:")

    # exit the script
    exit()

# honestly, I have no idea
load_dotenv()

# initialize client variable
client = discord.Bot()

# open the provided token file path
with open(args.token, "r") as f:

    # initialize token
    token = f.readline()

@client.event
async def on_ready():
    print("Meep! {0.user}".format(client))

# run the client
client.run(token)
