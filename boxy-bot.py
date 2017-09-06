import argparse
import asyncio
import discord
from discord.ext import commands
import logging
import random
import time
import wikipedia
# Testing Git
bot_description = 'Our awesome Box Boy\'s Discord bot.'

parser = argparse.ArgumentParser(description=bot_description)
parser.add_argument('--log', help='The destination of your log file.')
parser.add_argument('--token', help='Discord Bot Token.')

client = commands.Bot(command_prefix='!', description=bot_description)
logging.basicConfig(filename=parser.parse_args().log, level=logging.DEBUG)


@client.event
async def on_ready():
    """On ready command.

    Triggers when we successfully connect to the server.
    """
    logging.info('Logged in as')
    logging.info(client.user.name)
    logging.info(client.user.bot)


@client.command(description='Roll some die.')
async def roll(dice : str):
    """Rolls a dice!

    A simple command to handle rolling the dice.

    Args:
        dice: A string in the format 'NdN' specifying the number of die you want
              to roll, and the number of sides you want that die to have.
    """
    logging.info('Received Dice Roll Request')
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to in be NdN! (e.g. 1d6)')
        return

    if limit > 0:
        result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
        logging.info('Roll... %s' % result)
    else:
        result = 'You may not roll a d%d' % limit

    await client.say(result)


@client.command(description='Gets a random wikipedia page.')
async def random_wiki():
    """Finds a random wikipedia page.

    This randomly selects a wikipedia page and prints the title and url to
    discord, in the channel the user requested.
    """
    logging.info('Received Random Wikipedia Page Request: %d' % pages)
    results = wikipedia.random()
    if type(results) is str:
        logging.info('Got a wikipedia page')
        wiki_pages = wikipedia.page(title=results)

    await client.say('%s: %s' % (wiki_pages.title, wiki_pages.url))


@client.command(description='Tight.', pass_context=True)
async def tight(ctx):
    """Tight.

    tight.
    """
    logging.info('Tight.')
    await client.send_typing(ctx.message.channel)
    time.sleep(0.5)
    await client.say('Tight.')



client.run(parser.parse_args().token)
