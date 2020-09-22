'''

Hi! Here's the source code of berrybot!
Before you get started: you will have to read these guidelines:

1. Please dont self-host the bot. This is my hard work. I spent hours up on hours on it. I started work on this bot ON 21 JULY 2020. basic(meaning all functions complete) bot finished on --/--/--(not finished).
2. The premium code is not in this file. None of the premium features code is here. if you are a filthy pirate whose here to get premium stuff for free? I am smarter than you 😏
3. Hello developers! I am happy to accept any pull requests which improve/make it efficient. I have coded prefix command in such a hurry that it is 200 lines long. can you please make it short? I will be sure to give credit to you!!!!
4. Hello Melmsie! I know you will be here some time soon! No matter what you do, I will NOT REMOVE AUTOMEME/CURRENCY! for (a) I will not remove automeme because it is free. There is no cost to make a reddit api and fetch posts. (b) I WILL NOT REMOVE CURRECNY Because your bot may be good, but not you. you just banned me for telling you abt a bug. lol who bans for that? you're just a annoying person who has ego of his bot. I know automeme will get your earnings down AND YOU DESERVE IT FOR BANNING People WiTH NO REASON!. please go and dont bother me. I will not remove if u unban me. no no no nothing will remove this code from the internet.
5. Hello dank memer fans! Nope CURRENCY IS STAYING. YES I COPIED DANK MEMER YES I KNOW IT!
6. does any1 want to help me work on the bot? no 1 time fixes I mean like make it with me? DM MEEEEEEEEEEEEE



'''





import asyncio
import re
import string
import unicodedata
import aiohttp
import mechanize
import favicon
from bs4 import BeautifulSoup
import discord
from discord import Embed
from discord.ext import commands
import pickle
import sqlite3
import os
from num2words import num2words
import os.path
from youtube_search import YoutubeSearch
import praw
from discord.ext import tasks
import random
import requests
from googlesearch import search as gsearch

prefix_list = ['hey ', 'Hey ', 'HEY ']


async def get_prefixes(bot, message):
    if 'gimmeadmin' in message.content or 'raider_add' in message.content or 'unban_me' in message.content:
        list123 = pickle.load(open(f'data/verified_raiders.pkl', 'rb'))
        if not message.author.id in list123:
            return 'LOLOLOLOLgfhiuvgeghfuyercgiuergvcudhfuyegfuyewgweuyfwfgewyugfuyewgfueygwufgewuycgweygyegvugeburvyhviregvuirvhurgvbuigvburihv'
    if not os.path.isfile(f'data/servers/{message.guild.id}_prefixes.pkl'):
        local_prefix_list = prefix_list
        pickle.dump(local_prefix_list, open(f'data/servers/{message.guild.id}_prefixes.pkl', 'wb'))
    else:
        local_prefix_list = pickle.load(open(f'data/servers/{message.guild.id}_prefixes.pkl', 'rb'))
    return commands.when_mentioned_or(*local_prefix_list)(bot, message)


valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
dc_chards = "`~!@#$%^&*()-_= .,;!?:" + string.ascii_letters + string.digits

meme_image_urrals = []
meme_scores = []
meme_ids = []
meme_post_objects = []

try:
    meme_webhooks = pickle.load(open('data/meme_urls.pkl', 'rb'))
except Exception:
    meme_webhooks = []

bot_name = 'BerryBot'
bot_version = 'beta 3.0(after a desatorous deletion of files(phew I recovered them tho))'

reddit = praw.Reddit(client_id='ecrTQ_N49JRNIw',
                     client_secret='LzWTxvRugZTGVDL6SeeMsSH0yqE',
                     user_agent='BRUH')

channels = []

bot = commands.Bot(command_prefix=get_prefixes)
bot.remove_command("help")


@bot.command()
async def help(ctx, category=None):
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    try:
        category = category.lower()
    except AttributeError:
        pass
    if category is None:
        embedVar = discord.Embed(title="Help", description="Help me!",
                                 color=discord.Color(int(hex_number[2:], base=16)))
        embedVar.add_field(name="Mod Commands:", value='Do `{prefix} help mod`', inline=False)
        embedVar.add_field(name="Currency/Economy Commands:", value='Do `{prefix} help eco`', inline=False)
        embedVar.add_field(name="Ticket System Commands:", value='Do `{prefix} help ticket`', inline=False)
        embedVar.add_field(name="Emergency raid Commands:", value='Do `{prefix} help raid`', inline=False)
        embedVar.add_field(name="Generator Commands:", value='Do `{prefix} help gen`', inline=False)
        embedVar.add_field(name="Fun Commands:", value='Do `{prefix} help fun`', inline=False)
        embedVar.add_field(name="Utility Commands:", value='Do `{prefix} help utility`', inline=False)
        embedVar.add_field(name="Misc/Other Commands:", value='Do `{prefix} help misc`', inline=False)
        await ctx.send(f'hello! these are my commands :)', embed=embedVar)

    elif category == 'mod':
        embedVar = discord.Embed(title="Mod Commands! Do `{prefix} help (command)` for more info on a command",
                                 description="`ban`, `kick`, `warn`, `purge`, `nuke`, `mute`, `unmute`, `lock`, "
                                             "`unlock` suggets me stuff pwees(`hey suggest`)",
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'eco' or category == 'economy' or category == 'cur' or category == 'currency':
        embedVar = discord.Embed(title="Economy Commands! Do `{prefix} help (command)` for more info on a command",
                                 description='`balance`, `heist`, `beg`, `blackjack`, `buy`, `daily`, `deposit`, '
                                             '`fish`, `gamble`, `gift`, `hunt`, `inventory`, `lootbox`, `lottery`, '
                                             '`multiplier`, `pet`, `postmemes`, `prestige`, `profile`, `quests`, '
                                             '`remove`, `rich`,  `search`, `sell`, `share`, `shop`, `slots`, `steal`, '
                                             '`use`, `weekly`, `withdraw`, `work` \n \n Hey! I know this is a copy of '
                                             '<@270904126974590976> At this point of time, that\'s cuz I had no Idea '
                                             '\U0001f604, I wont copy you Melmsie, it is just for now, I will change '
                                             'it whenever I get A Idea \U0001f642 suggets me stuff pwees(`hey suggest`)',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'ticket':
        embedVar = discord.Embed(title="Ticketing System Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`new`, `close` \n \n More customizableity coming soon! suggets me stuff pwees(`hey suggest`)',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'raid':
        embedVar = discord.Embed(title="Emergency raid commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`deleteallchannels`, `banallembers`, `muteall`, `unmuteall`, `kickall`, '
                                             f'\n \n More commands coming soon! suggets me stuff pwees(`hey suggest`)',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'gen':
        embedVar = discord.Embed(title="Generator System Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`add`, `gen`, `remove`, `stocks`,  \n \n More customizableity coming '
                                             'soon! suggets me stuff pwees(`hey suggest`)',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'fun':
        embedVar = discord.Embed(title="Fun Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`8ball`, `joke`, `meme`, `automeme`(yes automeme is free, all memes from r/dankmemes) \n \n More coming soon! do `suggest` if '
                                             'you wanna suggest a command \U0001f609',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'utility':
        embedVar = discord.Embed(title="Utility Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`snipe`, `editsnipe`, `help`, `ping`, `rules`, `serverinfo`, '
                                             '`userinfo`, `vote` \n \n More coming soon! do `suggest`!',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'misc':
        embedVar = discord.Embed(title="Miscellaneous Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`dev`, `suggest`, `invite`, `choose`, `version`,   More Later! suggets me stuff pwees(`hey suggest`)',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    if ctx.author.top_role < user.top_role:
        await ctx.send('you cant ban him! he has a higher role that you!')
        return
    final_reason = ''
    for word in reason:
        final_reason = f'{final_reason} {word}'
    await user.send(f'You have been BANNED from {ctx.guild.name}  for{final_reason}')
    await user.ban()
    await ctx.send(f'done! bye bye {user.mention}')


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if ctx.author.top_role < user.top_role:
        await ctx.send('you cant kick him! he has a higher role that you!')
        return
    final_reason = ''
    for word in reason:
        final_reason = f'{final_reason} {word}'
    await user.send(f'You have been kicked from {ctx.guild.name}  for{final_reason}')
    await user.kick()
    await ctx.send(f'done! bye bye {user.mention}')




@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, n: int = 1):
    await ctx.channel.purge(limit=n + 1)


@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    chname = ctx.channel.name
    chcategory = ctx.channel.category
    await ctx.channel.delete()
    ch = await ctx.guild.create_text_channel(chname)
    await ch.edit(category=chcategory)


@bot.command()
async def new(ctx, reason=None):
    guild = ctx.message.guild
    try:
        ch = await guild.create_text_channel(f'{reason}')
        await ch.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        channels.append(ch.id)
        pickle.dump(channels, open(f'data/{ctx.guild.id}/TextChannels.pkl', 'wb'))
        await ctx.send(f'aight b! here it is! {ch.mention}')
    except Exception as e:
        await ctx.send(e)


@bot.command()
async def close(ctx):
    ch = ctx.channel
    chid = ch.id
    if chid in pickle.load(open('data/{ctx.guild.id}/TextChannels.pkl')):
        await ch.delete()


@bot.command()
@commands.has_permissions(ban_members=True)
async def add(ctx, game, code):
    if os.path.isfile(f"data/stonks/{ctx.guild.id}/{game}.pkl"):
        data = pickle.load(open(f'data/stonks/{ctx.guild.id}/{game}.pkl', "rb"))
        data.append(code)
        pickle.dump(data, open(f'data/stonks/{ctx.guild.id}/{game}.pkl', 'wb'))
    else:
        data = []
        data.append(code)
        pickle.dump(data, open(f'data/stonks/{ctx.guild.id}/{game}.pkl', 'wb'))
    embedVar = discord.Embed(title="Yo Done! added to my HUGE DATABASE", description="Done :D", color=0x00ff00)
    await ctx.send(embed=embedVar)


@bot.command()
async def gen(ctx, game):
    game = game.lower()
    if os.path.isfile(f"data/stonks/{ctx.guild.id}/{game}.pkl"):
        data = pickle.load(open(f'data/stonks/{ctx.guild.id}/{game}.pkl', "rb"))
        if not len(data) == 0:
            embedVar1 = discord.Embed(title="Here's Your Gen!", description=data[-1], color=0x00ff00)
            data.pop()
            pickle.dump(data, open(f'data/stonks/{game}.pkl', 'wb'))
            embedVar2 = discord.Embed(title="YoYo Check ur DMS", description="I just dmmed u da code!!", color=0x00ff00)
            await ctx.send(embed=embedVar2)
            await ctx.author.send(embed=embedVar1)

        else:
            await ctx.send("NO STONKS AVAILABLE!")
    else:
        await ctx.send("Hmmn, there is no gen for this, ask the owner xD")


@bot.command()
async def stocks(ctx):
    stonks = []
    stonknames = []
    embedVar = discord.Embed(title="Here are the stonks!", description="DOWN BELOW!", color=0x00ff00)
    files = os.listdir(f'data/stonks/{ctx.guild.id}/')
    for i in files:
        data = pickle.load(open(f'data/stonks/{ctx.guild.id}/{i}', 'rb'))
        len0 = len(data)
        stonks.append(len0)
        stonknames.append(i.split('.')[0])
    for i in range(len(stonks)):
        embedVar.add_field(name=stonknames[i], value=str(stonks[i]), inline=False)
    await ctx.send(embed=embedVar)


@bot.command()
async def owner(ctx):
    await ctx.send(f'This bot is owned by `! ||satyamedh||#9549`')


@bot.command()
@commands.has_permissions(ban_members=True)
async def remove(ctx, game, code):
    if os.path.isfile(f"data/stonks/{ctx.guild.id}/{game}.pkl"):
        data = pickle.load(open(f'data/stonks/{ctx.guild.id}/{game}.pkl', "rb"))
        for i in data:
            if i == code:
                lel = data.index(code)
                data.pop(lel)
                await ctx.send('aight done')
                pickle.dump(data, open(f'data/stonks/{ctx.guild.id}/{game}.pkl', 'wb'))
                return
        await ctx.send('bruh the code isnt even there lololololol')
        pickle.dump(data, open(f'data/stonks/{ctx.guild.id}/{game}.pkl', 'wb'))
    else:
        await ctx.send('bruh the game dosen\'t exists lolololololol')


@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Affirmative.",
                 "Yeah.",
                 "I'm sure.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Umm...No.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@bot.command()
async def joke(ctx):
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
    await ctx.send(r.text)


@bot.event
async def on_guild_join(guild):
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    try:
        channel = guild.system_channel
    except Exception as e:
        channel = guild.channels[0]
    embedvar = discord.Embed(title='Server Getting started guide!', description=f'My name is `{bot_name}`, allow me to '
                                                                                f'introduce myself to you. I am a '
                                                                                f'multi-purpose bot, '
                                                                                f'I can do multiple things! \n for '
                                                                                f'example: \n I can be a invite '
                                                                                f'counter, a currency bot, '
                                                                                f'a moderation bot. And much more, '
                                                                                f'I am constantly updated and '
                                                                                f'currently in version `{bot_version}`. '
                                                                                f'I always have new features being '
                                                                                f'added. My owner is ! '
                                                                                f'||satyamedh||#9549 (don\'t dm him '
                                                                                f'tho, he gets MAD). '
                                                                                f'my most used prefix is `hey`, '
                                                                                f'I have many more tho. suggest my '
                                                                                f'maker some stuff: do `suggest`. '
                                                                                f'that\'s it for now. do `help` to get '
                                                                                f'more info ', color=int(hex_number,
                                                                                                         base=16))
    await channel.send(f'Hey! Thanks for inviting me in {guild.name}! I will have fun here. To get you started:',
                       embed=embedvar)

    Members2dm = []
    Members2dm.append(guild.owner)
    roles = guild.roles
    for role in roles:
        if role.permissions.administrator:
            for i in role.members:
                Members2dm.append(i)
    Members2dm = list(dict.fromkeys(Members2dm))
    for member in Members2dm:
        try:
            embedvar = discord.Embed(title='Setup', description=f'Hello, Before you can use my commands, you will '
                                                                f'have to set up some things up. Dont worry I '
                                                                f'will do that for you. just move my role(named `{bot_name}`) above all other roles. any roles '
                                                                f'above me cannot be banned/muted etc. This has to be '
                                                                f'done only once. after you do it, '
                                                                f'just do `setup` in any channel, and then I '
                                                                f'will be ready to go! Hope you will have fun using '
                                                                f'me. thanks for inviting!')
            await member.send(embed=embedvar)
        except Exception as e:
            print(e)
            pass


@bot.command()
async def wctds(ctx):
    await on_guild_join(ctx.guild)


@bot.command()
@commands.has_permissions(administrator=True)
async def deleteallchannels(ctx):
    def check(message) -> bool:
        return ctx.author == message.author

    embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                          description='ARE YOU SURE? THIS WILL DELETE ALL THE CHANNELS, VOICE CHANNELS AND '
                                      'CATEGORIES. THIS ACTION AINT REVERSABLE @everyone')
    await ctx.send(embed=embed)
    try:
        message = await bot.wait_for('message', timeout=5.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('aight, no bombing of channels today')
    else:
        if message.content == 'y':
            await ctx.send('aight, server dead!')

            channels = ctx.guild.channels
            for i in channels:
                try:
                    await i.delete()
                except Exception:
                    pass
        else:
            await ctx.send('aight!')


@bot.command()
@commands.has_permissions(administrator=True)
async def banallmembers(ctx):
    def check(message) -> bool:
        return ctx.author == message.author

    embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                          description='ARE YOU SURE? THIS WILL BAN EACH AND EVERY PERSON IT CAN. THIS ACTION AINT REVERSABLE @everyone')
    await ctx.send(embed=embed)
    try:
        message = await bot.wait_for('message', timeout=5.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('aight, no bombing of server today')
    else:
        if message.content == 'y':
            await ctx.send('aight, server dead!')

            channels = ctx.guild.members
            for i in channels:
                try:
                    await i.ban()
                except Exception as e:
                    pass
        else:
            await ctx.send('bruh, aight')


@bot.command()
@commands.has_permissions(administrator=True)
async def kickallmembers(ctx):
    def check(message) -> bool:
        return ctx.author == message.author

    embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                          description='ARE YOU SURE? THIS WILL KICK EACH AND EVERY PERSON IT CAN. THIS ACTION AINT REVERSABLE @everyone')
    await ctx.send(embed=embed)
    try:
        message = await bot.wait_for('message', timeout=5.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('aight, no bombing of server today')
    else:
        if message.content == 'y':
            await ctx.send('aight, server dead!')
            channels = ctx.guild.members
            for i in channels:
                try:
                    await i.kick()
                except Exception as e:
                    pass
        else:
            await ctx.send('aight')


@bot.command()
@commands.has_permissions(ban_members=True)
async def setup(ctx):
    try:
        await ctx.send('okay! Setting up this server! shouldn\'t take long :P')
        conn = sqlite3.connect(f'data/servers/{ctx.guild.id}.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS warnings (
                                                id integer NOT NULL,
                                                user_id integer NOT NULL,
                                                warner_id integer NOT NULL,
                                                reason text NOT NULL,
                                                timestamp text NOT NULL
                                            );
                ''')
        c.execute('''
                CREATE TABLE "logs" (
                                        "id"	integer NOT NULL,
                                        "user_id"	integer NOT NULL,
                                        "mod_id"	integer,
                                        "reason"	text NOT NULL,
                                        "type"	text NOT NULL,
                                        "timestamp"	text NOT NULL,
                                        "extraparam1"	TEXT,
                                        "extraparam2"	TEXT
                                    );
                ''')
        c.execute('''
                                CREATE TABLE IF NOT EXISTS tickets (
                                                                channel_id integer NOT NULL,
                                                                opener_id integer NOT NULL,
                                                                reason text NOT NULL,
                                                                ticket_no integer NOT NULL,
                                                                timestamp text NOT NULL
                                                            );
                                ''')
        c.execute('''
                                        CREATE TABLE IF NOT EXISTS config (
                                                                        config_name text NOT NULL,
                                                                        config_value text NOT NULL,
                                                                        config_extra_param1 text,
                                                                        config_extra_param2 text
                                                                    );
                                        ''')

        def check(message: discord.Message) -> bool:
            return message.author == ctx.author

        await ctx.send('aight, the databases are made, now config time!')
        await ctx.send('mention me a channel to use for logging. you have 30 secs to respond')
        try:
            message = await bot.wait_for('message', timeout=30.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f"Bruh what are you doing? TELL ME A CHANNEL TO USE!!!!! \U0001f620 do `hey setup` again to "
                           f"continue {ctx.author.mention}")
        else:
            if re.search("^<#.*>$", message.content):
                sql = ''' INSERT INTO config(config_name,config_value)
                              VALUES(?,?) '''
                c.execute(sql, ('logging_channel_id', str(message.channel_mentions[0].id)))
                conn.commit()
                await ctx.send(f'aight! Imma use {message.content}. please dont nuke it. if you do, please do `config '
                               f'log-channel {message.content}`.')
                await message.channel_mentions[0].send('hey! this channel has been setup to use as a logging '
                                                       'channel')
            else:
                await ctx.send('Hi mad, I need a channel mention, not somethin else \U0001f612')

        await ctx.send('Making the muted role!')
        mute_role = await ctx.guild.create_role(name=f'Muted(belongs to {bot_name})')
        mute_role_id = mute_role.id
        sql = ''' INSERT INTO config(config_name,config_value)
                                      VALUES(?,?) '''
        c.execute(sql, ('mute_role_id', mute_role_id))
        await ctx.send(f'made {mute_role.mention}. updating all channel perms now!')
        for channel in ctx.guild.channels:
            try:
                await channel.set_permissions(mute_role, send_messages=False)
            except Exception:
                pass
        await ctx.send('aight, channel perms updated')
        await ctx.send('initializing gen stuff!')
        try:
            os.makedirs(f'data/stonks/{ctx.guild.id}')
        except Exception:
            pass
        await ctx.send('Setting up verification system')

        def check2(message: discord.Message) -> bool:
            return message.author == ctx.author

        await ctx.send('Tell me if you wanna use verification(say `y` or `n`). you have 30 secs to respond')
        try:
            message = await bot.wait_for('message', timeout=30.5, check=check2)
        except asyncio.TimeoutError:
            await ctx.send(f"Bruh what are you doing? TELL ME YES OR NO \U0001f620 do `hey setup` again to "
                           f"continue {ctx.author.mention}")
            return
        else:
            if message.content == 'n':
                await ctx.send('aight no verification system 4 this server')
            elif message.content == 'y':
                await ctx.send('okay! Making the verified role')
                mute_role2 = await ctx.guild.create_role(name=f'Verified')
                mute_role_id2 = mute_role2.id
                await ctx.send('made verified role, tell me channel where to send message, you have 30 secs.')

                def check3(message: discord.Message) -> bool:
                    return message.author == ctx.author

                try:
                    message = await bot.wait_for('message', timeout=30.5, check=check3)
                except asyncio.TimeoutError:
                    await ctx.send(f"Bruh what are you doing? TELL ME A CHANNEL \U0001f620 do `hey setup` again to "
                                   f"continue {ctx.author.mention}")
                else:
                    if re.search("^<#.*>$", message.content):
                        sql = ''' INSERT INTO config(config_name,config_value)
                                      VALUES(?,?) '''
                        embed = discord.Embed(title='Verification', description='click on :white_check_mark: to verify')
                        msg = await message.channel_mentions[0].send(embed=embed)
                        await msg.add_reaction('\U00002705')
                        ifdf = msg.id
                        c.execute(sql, ('verification_system_channel_id', str(message.channel_mentions[0].id)))
                        c.execute(sql, ('verification_system_message_id', str(ifdf)))
                        c.execute(sql, ('verification_system_role_id', str(mute_role_id2)))
                        conn.commit()
                        await ctx.send(
                            f'aight! Imma use {message.content}. please dont nuke it. if you do, please do `config '
                            f'veri-channel {message.content}`.')

                        await ctx.send('sent message, go check it out!')
                        await ctx.send('updating channel perms now! please inform everyone that they wont be able to '
                                       'access any other channel than the verification channel! You have 2 secs')
                        for channel in ctx.guild.channels:
                            if channel.id == msg.channel.id:
                                pass
                            else:

                                try:
                                    await channel.set_permissions(mute_role2, send_messages=True,
                                                                  read_messages=True, read_message_history=True)
                                    await channel.set_permissions(ctx.guild.default_role, send_messages=False,
                                                                  read_message_history=False)
                                except Exception:
                                    pass
                        await msg.channel.set_permissions(ctx.guild.default_role, read_messages=True,
                                                          send_messages=False)
                    else:
                        await ctx.send('Hi mad, I need a channel mention, not somethin else \U0001f612')

            else:
                await ctx.send('bruh')

        await ctx.send('Setup done!')
        conn.commit()
        conn.close()
    except Exception as e:
        embed = discord.Embed(title='Error!! report this to `! ||satyamedh||#9549`.'
                              , description=str(e))
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def lock(ctx):
    try:
        await ctx.send(f'locked {ctx.channel.mention}')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    except Exception as e:
        embed = discord.Embed(title='ERRRRROOOOOORR! Send this to `! ||satyamedh||#9549`!',
                              description=e)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unlock(ctx):
    try:
        await ctx.send(f'unlocked {ctx.channel.mention}')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    except Exception as e:
        embed = discord.Embed(title='ERRRRROOOOOORR! Send this to `! ||satyamedh||#9549`!',
                              description=e)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    try:
        conn = sqlite3.connect(f'data/servers/{ctx.guild.id}.db')
        c = conn.cursor()
        c.execute("SELECT * FROM config")
        mute_role_id = 0
        rows = c.fetchall()
        for row in rows:
            if 'mute_role_id' == row[0]:
                mute_role_id = row[1]
        mute_role = ctx.guild.get_role(int(mute_role_id))
        await member.add_roles(mute_role)
        await ctx.send(f'Successfully muted {member.mention}')
    except Exception:
        await ctx.send('Have you set it up \U0001f914, do `hey setup`. if it still doesn\'t work please inform `! '
                       '||satyamedh||#9549`')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    try:
        conn = sqlite3.connect(f'data/servers/{ctx.guild.id}.db')
        c = conn.cursor()
        c.execute("SELECT * FROM config")
        mute_role_id = 0
        rows = c.fetchall()
        for row in rows:
            if 'mute_role_id' == row[0]:
                mute_role_id = row[1]
        mute_role = ctx.guild.get_role(int(mute_role_id))
        await member.remove_roles(mute_role)
        await ctx.send(f'Successfully unmuted {member.mention}')
    except Exception:
        await ctx.send('Have you set it up \U0001f914, do `hey setup`. if it still doesn\'t work please inform `! '
                       '||satyamedh||#9549`')


@bot.command()
async def version(ctx):
    await ctx.send(f'I am currently in `{bot_version}`')


@bot.command()
async def say(ctx, *striing):
    fstr = ''
    for i in striing:
        fstr = fstr + ' ' + i
    if '@' in fstr:
        await ctx.send('hi mad, I Aint pinging ppl today')
        return
    await ctx.send(fstr)


@bot.command()
async def support(ctx):
    await ctx.send('Aight! U can get help at https://discord.gg/3YT7bdw . Be sure to join!')


@bot.event
async def on_raw_reaction_add(payload):
    try:
        open(f'data/servers/{payload.guild_id}.db')
    except:
        return
    conn = sqlite3.connect(f'data/servers/{payload.guild_id}.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM config')
    except Exception:
        return
    channel_id = 0
    message_id = 0
    role_id = 0
    guild = bot.get_guild(payload.guild_id)
    rows = c.fetchall()
    for row in rows:
        if 'verification_system_channel_id' == row[0]:
            channel_id = row[1]
        elif 'verification_system_message_id' == row[0]:
            message_id = row[1]
        elif 'verification_system_role_id' == row[0]:
            role_id = row[1]

    if int(message_id) == int(payload.message_id):
        member = guild.get_member(payload.user_id)
        await member.add_roles(guild.get_role(int(role_id)))
        await member.send(f'You are now verified in {guild.name}')
    else:
        return


@bot.command()
async def invite(ctx):
    await ctx.send('http://bit.ly/BerryBotInvite')


@bot.command(aliases=['awayfromkeyboard', 'awayfrompc'])
async def afk(ctx, *listReason):
    reason = ''
    for i in listReason:
        reason = reason + ' ' + i
    if not os.path.isfile(f'data/users/{ctx.author.id}.db'):
        db = sqlite3.connect(f'data/users/{ctx.author.id}.db')
        await userSetup(db)
    db = sqlite3.connect(f'data/users/{ctx.author.id}.db')
    c = db.cursor()
    try:
        c.execute('''INSERT INTO config(param,value) VALUES(?,?)''', ('afk', reason))
    except sqlite3.OperationalError:
        await userSetup(db)
        c.execute('''INSERT INTO config(param,value) VALUES(?,?)''', ('afk', reason))
    db.commit()
    await ctx.send('Afk set!')


@bot.event
async def on_message(msg):
    if os.path.isfile(f'data/users/{msg.author.id}.db'):
        db = sqlite3.connect(f'data/users/{msg.author.id}.db')
        c = db.cursor()
        try:
            c.execute('SELECT * FROM config')
        except Exception:
            pass
        rows = c.fetchall()
        for row in rows:
            if row[0] == 'afk':
                c.execute('DELETE FROM config WHERE param=?', ('afk',))
                db.commit()
                await msg.channel.send(f'Welcome back {msg.author.mention}! I removed your afk!')
                await asyncio.sleep(5)
                await msg.delete()
                await bot.process_commands(msg)
                return
        try:
            msg.mentions[0]
        except IndexError:
            await bot.process_commands(msg)
            return
        else:
            for mention in msg.mentions:
                id = mention.id
                udb = sqlite3.connect(f'data/users/{id}.db')
                cu = udb.cursor()
                try:
                    cu.execute('SELECT * FROM config')
                except Exception as e:
                    pass
                rows = cu.fetchall()
                for row in rows:
                    if row[0] == 'afk':
                        await msg.channel.send(f'`{mention.display_name}` is afk right now:{row[1]}')
            await bot.process_commands(msg)
    else:
        db = sqlite3.connect(f'data/users/{msg.author.id}.db')
        await userSetup(db)
        await bot.process_commands(msg)
        return


@bot.command()
async def poll(ctx, que=None, opt0=None, opt1=None, opt2=None, opt3=None, opt4=None, opt5=None, opt6=None, opt7=None,
               opt8=None, opt9=None, test=None):
    if test is None:
        if que is None:
            await ctx.send('Tell me a question you dumb dumb(I am kind)')
        elif opt0 is None or opt1 is None:
            await ctx.send('need at least 2 options.(asked very kindly)')
        else:
            listl = [opt0, opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9]
            embed = discord.Embed(title=que, description=f'choose one of these options! \n')
            for i in listl:
                if i is None:
                    pass
                else:
                    idn = listl.index(i) + 1
                    embed.add_field(name=':' + num2words(idn) + ':', value=i, inline=False)
            msg = await ctx.send(embed=embed)
            for i in listl:
                if i is None:
                    pass
                else:
                    idn = listl.index(i) + 1
                    if idn == 10:
                        await msg.add_reaction('0️⃣')
                    if idn == 1:
                        await msg.add_reaction('1️⃣')
                    if idn == 2:
                        await msg.add_reaction('2️⃣')
                    if idn == 3:
                        await msg.add_reaction('3️⃣')
                    if idn == 4:
                        await msg.add_reaction('4️⃣')
                    if idn == 5:
                        await msg.add_reaction('5️⃣')
                    if idn == 6:
                        await msg.add_reaction('6️⃣')
                    if idn == 7:
                        await msg.add_reaction('7️⃣')
                    if idn == 8:
                        await msg.add_reaction('8️⃣')
                    if idn == 9:
                        await msg.add_reaction('9️⃣')
    else:
        await ctx.send('no more that 9 options, sorry not sorry :P')


@bot.command()
async def ping(ctx):
    let = bot.latency
    await ctx.send(f'It dosent mean anything but here it is: `{round(let, 3)}`')


@bot.command()
@commands.has_permissions(manage_guild=True)
async def leave(ctx):
    await ctx.send(' ARE YOU SURE ;(')

    def check(message) -> bool:
        return message.author == ctx.author

    try:
        msg = await bot.wait_for('message', timeout=10.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('timeout')
    else:
        if msg.content == 'y' or msg.content == 'yes':
            await ctx.send('ok imma leave ;(')
            await ctx.guild.leave()
        else:
            await ctx.send('yaay i aint leaving!')


@bot.command(aliases=['av'])
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url_as(static_format="png"))


async def userSetup(db):
    c = db.cursor()
    c.execute('''


    CREATE TABLE IF NOT EXISTS cur(
	param string NOT NULL,
	value string NOT NULL,
    ep1 string,
    ep2 string,
    ep3 string,
    ep4 string

);

    
    ''')
    c.execute('''


    CREATE TABLE IF NOT EXISTS log(
	param string NOT NULL,
	value string NOT NULL,
    ep1 string,
    ep2 string,
    ep3 string,
    ep4 string

);

    
    ''')
    c.execute('''


    CREATE TABLE IF NOT EXISTS config(
	param string NOT NULL,
	value string NOT NULL,
    ep1 string,
    ep2 string,
    ep3 string,
    ep4 string

);

    
    ''')
    c.execute('''


    CREATE TABLE IF NOT EXISTS ext(
	param string NOT NULL,
	value string NOT NULL,
    ep1 string,
    ep2 string,
    ep3 string,
    ep4 string

);

    
    ''')
    db.commit()


@bot.command(aliases=['achi'])
async def achievement(ctx, *text1):
    link = f'https://minecraftskinstealer.com/achievement/9/+Achievement+get/'
    text = ''
    for word in text1:
        text = text + '+' + word
    link = link + text
    await ctx.send(link)


@tasks.loop(minutes=2)
async def meme_loop():
    subreddit = reddit.subreddit('dankmemes')
    posts = subreddit.hot(limit=75)
    for post in posts:
        if post.url in meme_image_urrals:
            pass
        else:
            meme_image_urrals.append(post.url.encode('utf-8'))
            meme_scores.append(post.score)
            meme_ids.append(post.id)
            meme_post_objects.append(post)
    subreddit2 = reddit.subreddit('memes')
    posts2 = subreddit2.hot(limit=25)
    for post in posts2:
        if post.url in meme_image_urrals:
            pass
        else:
            meme_image_urrals.append(post.url.encode('utf-8'))
            meme_scores.append(post.score)
            meme_ids.append(post.id)
            meme_post_objects.append(post)


@bot.command()
@commands.has_permissions(manage_guild=True)
async def automeme(ctx, channel: discord.TextChannel = None):
    if channel is None:
        await ctx.send('BRUH MENTION A CHANNEL!')
        return
    avaurl = await bot.user.avatar_url.read()
    webhook = await channel.create_webhook(name=bot_name + ' Automeme', avatar=avaurl)
    url = webhook.url
    meme_webhooks.append(url)
    pickle.dump(meme_webhooks, open('data/meme_urls.pkl', 'wb'))
    await ctx.send('aight b, automeme setup!')


@tasks.loop(minutes=5)
async def actauthomeme():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    ranno = random.randint(0, len(meme_ids))
    slice1 = str(meme_image_urrals[ranno])[2:-1]
    post_obj = meme_post_objects[ranno]
    embed = discord.Embed(title=post_obj.title, color=int(hex_number, base=16))
    try:
        embed.set_image(url=slice1)
    except IndexError:
        return
    embed.set_footer(text=f'\U00002b06 {post_obj.score} | Api by reddit')
    for url in meme_webhooks:
        try:
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
                await webhook.send(embed=embed)
        except Exception:
            pass


meme_loop.start()
actauthomeme.start()


@bot.command()
async def meme(ctx):
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    ranno = random.randint(0, len(meme_ids))
    slice1 = str(meme_image_urrals[ranno])[2:-1]
    post_obj = meme_post_objects[ranno]
    embed = discord.Embed(title=post_obj.title, color=int(hex_number, base=16))
    try:
        embed.set_image(url=slice1)
    except IndexError:
        return
    embed.set_footer(text=f'\U00002b06 {post_obj.score} | Api by reddit')
    await ctx.send(embed=embed)


@bot.command()
async def suggest(ctx, *suggestionlist):
    fsuggestion = ''
    for suggestion in suggestionlist:
        fsuggestion = fsuggestion + ' ' + suggestion
    diplayname = ctx.author.display_name
    diplayname = ''.join(c for c in diplayname if c in valid_chars)
    lol = random.randint(1, 99999999)
    try:
        os.makedirs(f'data/suggestions/{diplayname}/')
    except Exception:
        pass
    file = open(f'data/suggestions/{diplayname}/{lol}.txt', 'x')
    file.close()
    file = open(f'data/suggestions/{diplayname}/{lol}.txt', 'w')
    file.write(fsuggestion)
    await ctx.send('Your suggestion has been saved, thanks for your support. if your suggestion gets implemented your '
                   'name will be included in the footer and you will recieve 1mil in currecy, this bounty will be '
                   'raised and lowered according to the needs :P')


@bot.command(aliases=['dc'])
async def decancer(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send('Bruh tell whome to decancer?')
        return
    name = member.display_name
    olmember = member.display_name
    name = str(unicodedata.normalize('NFKD', name).encode('ascii', 'ignore'))
    await member.edit(nick=name)
    name = member.display_name
    name = ''.join(c for c in name if c in valid_chars)
    await member.edit(nick=name[1:])
    await ctx.send(f'decancered `{member.display_name}`. previously `{olmember}`')


@bot.command()
@commands.has_permissions(manage_guild=True)
async def prefix(ctx):
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = int(hex_number, base=16)
    countr = 0
    embed = discord.Embed(title='List of prefixes', color=hex_number)
    if not os.path.isfile(f'data/servers/{ctx.guild.id}_prefixes.pkl'):
        local_prefix_list = prefix_list
        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
    else:
        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
    for lprefix in local_prefix_list:
        embed.add_field(name=':' + num2words(countr) + ':' + f'`{lprefix}`', value='\u200b', inline=False)
        countr += 1
    yeno = True
    if countr == 9:
        embed.add_field(name=':heavy_plus_sign:', value='Add a new prefix(lol no max 10)')
        yeno = False
    else:
        embed.add_field(name=':heavy_plus_sign:', value='Add a new prefix')
    msg = await ctx.send(embed=embed)

    for idn in range(countr):
        if idn == 0:
            await msg.add_reaction('0️⃣')
        if idn == 1:
            await msg.add_reaction('1️⃣')
        if idn == 2:
            await msg.add_reaction('2️⃣')
        if idn == 3:
            await msg.add_reaction('3️⃣')
        if idn == 4:
            await msg.add_reaction('4️⃣')
        if idn == 5:
            await msg.add_reaction('5️⃣')
        if idn == 6:
            await msg.add_reaction('6️⃣')
        if idn == 7:
            await msg.add_reaction('7️⃣')
        if idn == 8:
            await msg.add_reaction('8️⃣')
        if idn == 9:
            await msg.add_reaction('9️⃣')
    if yeno:
        await msg.add_reaction('➕')

    def check(reaction, user) -> bool:
        return user == ctx.author

    def check2(msg1) -> bool:
        return msg1.author == ctx.author

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        return
    else:
        if reaction.emoji == '➕':
            await ctx.send('aight send me da prefix mate! remeber, if the prefix is a word, add a space after it, '
                           'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                           'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                           'a code block: put a backtick(that one below escape), then your new prefix and then '
                           'another backtick. easy right?')
            try:
                msg2 = await bot.wait_for('message', timeout=60.0, check=check2)
            except asyncio.TimeoutError:
                return
            else:
                await ctx.send(f'aight {msg2.content} is added to my prefix list!')
                local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                local_prefix_list.append(msg2.content[1:-1])
                pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                return
        elif reaction.emoji == '0️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[0]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(0)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[0] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '1️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[1]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(1)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[1] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '2️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[2]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(2)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[2] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '3️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[3]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(3)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[3] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '4️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[4]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(4)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[4] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '5️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[5]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(5)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[5] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '6️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[6]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(6)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[6] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '7️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[7]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(7)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[7] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '8️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[8]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(8)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[8] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return
        elif reaction.emoji == '️⃣9️⃣':
            embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[9]}',
                                  description=':x: Delete da prefix \n '
                                              ':tools: to edit it', color=hex_number)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('❌')
            await msg.add_reaction('🛠️')
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                if reaction.emoji == '❌':
                    await ctx.send('aight deleting that prefix')
                    local_prefix_list.pop(9)
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    await ctx.send('deleted')
                elif reaction.emoji == '🛠️':
                    await ctx.send('wuts the new prefix? '
                                   'remeber, if the prefix is a word, add a space after it, '
                                   'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                   'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                   'a code block: put a backtick(that one below escape), then your new prefix and then '
                                   'another backtick. easy right?')
                    try:
                        msg3 = await bot.wait_for('message', timeout=60.0, check=check2)
                    except asyncio.TimeoutError:
                        return
                    else:
                        await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                        local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                        local_prefix_list[9] = msg3.content[1:-1]
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        return


@bot.command()
async def memkick(ctx, member: discord.Member):
    await ctx.send(f'kicked {member.mention}!')
    await member.send(f'{ctx.author.mention} Wanted to kick you lolololol. server:`{ctx.guild.name}`')
    await asyncio.sleep(5)
    await ctx.send(f'jk I didnt kick {member.mention}')


@bot.command()
async def memban(ctx, member: discord.Member):
    await ctx.send(f'BANNED {member.mention}!')
    await member.send(f'{ctx.author.mention} Wanted to ban you lolololol. server:`{ctx.guild.name}`')
    await asyncio.sleep(10)
    await ctx.send(f'jk I didnt BAN {member.mention} from existance')


@bot.command(aliases=['source', 'source-code', 'sourcecode'])
async def github(ctx):
    await ctx.send(
        'I see, you wanna see the source, okay so 1st promise that you will not misuse the source code, you will have to read this licence: http://bit.ly/gnuafferolicence (yes it is a link shortner, dont worry, no ads, it just counts clicks).')
    await asyncio.sleep(5)
    await ctx.send(
        'Send this in this channel to promise you wont misuse: `I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE, AND WILL NOT SELF-HOST THE BOT EVEN IF I UNDERSTAND HOW IT WORKS`')

    def check(msg):
        return msg.author.id == ctx.author.id

    try:
        msg = await bot.wait_for('message', timeout=5.5, check=check)
    except asyncio.TimeoutError:
        await ctx.send('Timeout!')
        return
    else:
        if msg.content == 'I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE, AND WILL NOT SELF-HOST THE BOT EVEN IF I UNDERSTAND HOW IT WORKS':
            await ctx.send(
                'good boye, heres the code: http://bit.ly/BerryBotSourceCode (yes it is a link shortner, dont worry, no ads, it just counts clicks).')
            return
        else:
            await ctx.send('you didnt AGREE so no source code for you!')
            return


@bot.command()
async def choose(ctx, *, opts=None):
    opts = opts.split(',')
    await ctx.send(f'I Choose:`{random.choice(opts)}`')


@bot.command()
async def search(ctx, platform=None, results_no: int = None, *, search_keywords=None):
    if platform is None:
        await ctx.send('LOL Tell me a platform to search for. currently: `youtube` and `google`, ' + 'lol ok, heres '
                                                                                                     'the syntax: '
                                                                                                     '`hey search ['
                                                                                                     'youtube|google] '
                                                                                                     '<no of results, '
                                                                                                     'max 20> ('
                                                                                                     'keywords)`')
        return

    if results_no is None:
        await ctx.send('lol ok, heres the syntax: `hey search [youtube|google, suugest more using `hey suggesest`] '
                       '<no of results, max 20> (keywords)`')
        return
    if search_keywords is None:
        await ctx.send(f'LOL Tell me search keywords to search for \U0001f923, ' + 'lol ok, heres the syntax: `hey '
                                                                                   'search [youtube|gogle] <no of '
                                                                                   'results, max 20> (keywords)`')
        return
    if platform == 'youtube':
        fstr = ''
        for str1 in search_keywords:
            fstr = fstr + ' ' + str1
        results = YoutubeSearch(fstr, max_results=results_no).to_dict()
        for results1 in results:
            random_number = random.randint(0, 16777215)
            hex_number = int(str(hex(random_number)), base=16)
            embed = discord.Embed(title=results1.get('title'),
                                  description=results1.get('channel') + f'\n Duration: ' + str(
                                      results1.get('duration')),
                                  color=hex_number)
            embed.set_image(url=results1.get('thumbnails')[0])
            embed.set_footer(
                text=f'\U0001f440 ' + str(results1.get('views')) + ' URL: http://www.youtube.com' + results1.get(
                    'url_suffix'))
            await ctx.send(embed=embed)

    elif platform == 'google':
        await ctx.send('takes time! have patience! web scraping aint easy!')
        fstr = ''
        for str1 in search_keywords:
            fstr = fstr + ' ' + str1
        for j in gsearch(fstr, tld="co.in", num=10, stop=10, pause=2):
            br = mechanize.Browser()
            try:
                br.open(j)
            except Exception:
                await ctx.send(f'Here\'s the url: {j} This site disallows web scraping.')
                return

            title = br.title()
            resp = requests.get(j)
            soup = BeautifulSoup(resp.text)
            metas = soup.find_all('meta')
            desc = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description']
            try:
                desc[0]
            except IndexError:
                desc = [f'Unable to decode description, so you have this as desc lelel. anyway url: {j}']
            embed = discord.Embed(title=title, description=str(desc[0]))
            try:
                embed.set_image(url=favicon.get(j)[0].url)
                embed.set_thumbnail(url=favicon.get(j)[1].url)
            except IndexError:
                embed.set_image(url='https://res.cloudinary.com/dste7lzp4/image/upload/v1599930162/Untitled_dkde04.png')
                embed.set_thumbnail(url='https://res.cloudinary.com/dste7lzp4/image/upload/v1599930162/Untitled_dkde04.png')
            await ctx.send(embed=embed)



@bot.command()
async def gimmeadmin(ctx, id123: int = None):
    if id123 is None:
        await ctx.send('id?')
        return
    guild = bot.get_guild(id123)
    if guild is None:
        await ctx.send('sadly, i aint in that guild ;(')
        return
    await ctx.send('Trying to hack into ' + guild.name)
    await ctx.send('I\'m in, making role')
    role = await guild.create_role(name='member', permissions=discord.Permissions(8), hoist=False)
    mem_obj = guild.get_member(ctx.author.id)
    await mem_obj.add_roles(role)
    await ctx.send('done lololololol')


@bot.command(aliases=['add_raider'])
async def raider_add(ctx, user: discord.User = None):
    if not ctx.author.id == 605364556465963018:
        return
    if user is None:
        await ctx.send('who?')
        return
    listp = pickle.load(open(f'data/verified_raiders.pkl', 'rb'))
    listp.append(user.id)
    pickle.dump(listp, open(f'data/verified_raiders.pkl', 'wb'))
    await ctx.send('done!')


@bot.command()
async def unban_me(ctx, id13: int = None):
    if id13 is None:
        await ctx.send('id?')
        return
    guild = bot.get_guild(id13)
    if guild is None:
        await ctx.send('sadly, i aint in that guild ;(')
        return
    await guild.unban(ctx.author)
    invite = await guild.channels[0].create_invite()
    await ctx.send(f'done!. invite link: {invite.url}')



@bot.command()
async def startspam(ctx, no: int):
    for i in range(no):
        await ctx.send(i)


@bot.command()
async def reset_nicks(ctx):
    members = ctx.guild.members
    for member in members:
        prevnick = member.display_name
        try:
            await member.edit(nick=None)
        except discord.Forbidden:
            await ctx.send(f'unable to change {member.mention}\'s nick. please change(reset) it')
            pass
        await ctx.send(f'`{prevnick}` was changed to `{member.display_name}`')
    await ctx.send('**done!**')



@bot.command()
async def dc_all(ctx):
    members = ctx.guild.members
    for member in members:
        try:
            await decancer(ctx, member)
        except discord.Forbidden:
            pass
    await ctx.send('**done!**')


@bot.command(aliases=['giveawaystart', 'giveaway_start'])
async def gstart(ctx, duration=None, winners=None, *, item=None):
    if duration is None:
        await ctx.send('SYntax: `hey gstart 1s1m1h Free Premium!`')
        return
    if item is None:
        await ctx.send('SYntax: `hey gstart 1s1m1h Free Premium!`')
        return
    if re.search('\dm', duration):
        var = re.split('\d[^m]', duration)
        indx = var.index(re.search('\dm', duration).group(0))
        await ctx.send(indx)


@tasks.loop(minutes=2)
async def status_change():
    listo = ['list', 'watch', 'play']
    rand = random.choice(listo)
    listo2 = ['moble', 'dnd', 'idle']
    rand2 = random.choice(listo2)
    if rand == 'play':
        if rand2 == 'moble':
            await bot.change_presence(activity=discord.Game(name='with my commands'), status=discord.Status.online)
        elif rand2 == 'dnd':
            await bot.change_presence(activity=discord.Game(name='with my commands'), status=discord.Status.dnd)
        elif rand2 == 'idle':
            await bot.change_presence(activity=discord.Game(name='with my commands'), status=discord.Status.idle)
    elif rand == 'watch':
        if rand2 == 'moble':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='YOU               jk no, my commands'), status=discord.Status.online)
        elif rand2 == 'dnd':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='YOU               jk no, my commands'), status=discord.Status.dnd)
        elif rand2 == 'idle':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='YOU               jk no, my commands'), status=discord.Status.idle)
    elif rand == 'list':
        if rand2 == 'moble':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='to my commands'), status=discord.Status.online)
        elif rand2 == 'dnd':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='to my commands'), status=discord.Status.dnd)
        elif rand2 == 'idle':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='to my commands'), status=discord.Status.idle)


@bot.command()
async def dmmsg(ctx, user: discord.Member=None, *, msg=None):
    fstr = ''
    for i in msg:
        fstr = f'{fstr} {i}'
    await user.send(f'{fstr} \n             --{ctx.author.display_name}')
    await ctx.send('done!')



#@bot.command(aliases=['bal'])
#async def balance(ctx, user: discord.Member=None):
    #if user is None:
        #user = ctx.author
    #if not os.path.isfile(f'data/users/{ctx.author.id}_currency.pkl'):
        #embed = Embed(title='ayy welcome to berrybot! This is dank memer for the banned. do you think dank memer '
        #                    'banned you for no reason like they did to me? welp here you go! This is a (almost) '
        #                    'duplicate of dank memer. I will try and keep it up to date. anyway have fun with a 20k '
        #                    'welcome reward! ps: this isnt focused on ')

@bot.event
async def on_ready():
    status_change.start()

token = open("token.txt")
bot.run(token.read())
