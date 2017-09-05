import argparse
import asyncio
import discord
from discord.ext import commands
import logging
import random
import wikipedia

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


@client.command()
async def roll(dice : str):
    logging.info('Received Dice Roll Request')
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to in NdN!')
        return
    if limit > 0:
        result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
        logging.info('Roll... %s' % result)
    else:
        result = 'You may not roll a d%d' % limit

    await client.say(result)


@client.command()
async def random_wiki(pages=1):
    logging.info('Received Random Wikipedia Page Request: %d' % pages)
    if pages > 5:
        await client.say('I am not going to spam the channel')
    else:
        articles = []
        logging.info('Requesting %s pages' % pages)
        results = wikipedia.random(pages)
        if type(results) is str:
            logging.info('Got a single page')
            articles = [wikipedia.page(title=results)]
        elif type(results) is dict:
            logging.info('Got multiple articles')
            for result in results:
                articles.append(wikipedia.page(title=result))

        messages = []
        for article in articles:
            messages.append('%s: %s' % (article.title, article.url))
            logging.info('Sending the following wiki-page: %s' % message)




client.run(parser.parse_args().token)
