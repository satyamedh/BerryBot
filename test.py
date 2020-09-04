import asyncio
import re
import discord
from discord.ext import commands
import pickle
import sqlite3
import os
from num2words import num2words
import os.path
import random
import requests

bot_name = 'BerryBot'
bot_version = 'alpha 3.0(Major rewrite)'

prefix_list = ['I Will ', 'I wanna ', 'ill ', 'I\'LL ', 'ill ', 'bro ', 'hey ',
               'I want ', 'i want ', 'Hey', 'HEY']

channels = []

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('hey ', 'Hey ', 'HEY '))
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
                                             "`unlock`",
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
                                             'it whenever I get A Idea \U0001f642',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'ticket':
        embedVar = discord.Embed(title="Ticketing System Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`new`, `close` \n \n More customizableity coming soon!',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'raid':
        embedVar = discord.Embed(title="Emergency raid commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`deleteallchannels`, `banallembers`, `muteall`, `unmuteall`, `kickall`, '
                                             f'\n \n More commands coming soon!',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'gen':
        embedVar = discord.Embed(title="Generator System Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`add`, `gen`, `remove`, `stocks`,  \n \n More customizableity coming '
                                             'soon!',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)

    elif category == 'fun':
        embedVar = discord.Embed(title="Fun Commands! Do `{prefix} help (command)` for more info on "
                                       "a command",
                                 description='`8ball`, `joke` \n \n More coming soon!(memes too!) do `suggest` if '
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
                                 description='`dev`, `suggest`, `invite`, `choose`, `version`  More Later!',
                                 color=discord.Color(int(hex_number[2:], base=16)))
        await ctx.send(embed=embedVar)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, reason=None):
    try:
        log_channel = open(f'data/server_data/{ctx.guild.id}/settings/log_channel.txt')
        ch = await bot.fetch_channel(log_channel.read())
        Embedvar = discord.Embed(title='Member Banned', description=f'Member Named `{user.display_name}` was banned. '
                                                                    f'action taken by {ctx.author.display_name}. '
                                                                    f'Reason: `{reason}`')
        log_channel.close()
        await ch.send(embed=Embedvar)
    except Exception as e:
        await ctx.send('Either That user isnt bannable, or you havent set up the server. do `hey setup` and try again. if '
                 'it still wont work that person is immune to me \U0001f440 ')
    await ctx.send(f"{user.mention} has been banned woo, reason:{reason})    https://www.tenor.com/bfuQS.gif")
    await ctx.guild.ban(user, reason=reason, delete_message_days=0)
    await user.send(f"U were were BANNED FROM {ctx.guild.name} for {reason}, bye bye")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, reason=None):
    try:
        log_channel = open(f'data/server_data/{ctx.guild.id}/settings/log_channel.txt')
        ch = await bot.fetch_channel(log_channel.read())
        Embedvar = discord.Embed(title='Member Banned', description=f'Member Named `{user.display_name}` was kicked. '
                                                                    f'action taken by {ctx.author.display_name}. '
                                                                    f'\n Reason: `{reason}`')
        log_channel.close()
        await ch.send(embed=Embedvar)
    except Exception as e:
        ctx.send('Either That user isnt kickable, or you havent set up the server. do `hey setup` and try again. if '
                 'it still wont work that person is immune to me \U0001f440 ')
    await ctx.send(f"{user.mention} has been kicked woo, reason:{reason})    https://tenor.com/IDX1.gif")
    await ctx.guild.kick(user, reason=reason)
    await user.send(f"U were were KICK FROM {ctx.guild.name} for {reason}, come back soon :sad:")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, user: discord.User, reason=None):
    global wrnno
    try:
        log_channel = open(f'data/server_data/{ctx.guild.id}/settings/log_channel.txt')
        ch = await bot.fetch_channel(log_channel.read())
        Embedvar = discord.Embed(title='Member warned', description=f'Member Named `{user.display_name}` was warned. '
                                                                    f'action taken by {ctx.author.display_name}. '
                                                                    f'\n Reason: `{reason}`')
        warn_no = open(f'data/server_data/{ctx.guild.id}/warnings/{user.id}/count.txt', 'rw')
        try:
            wrnno = int(warn_no.read()) + 1
        except Exception:
            wrnno = 1
        warn_no.write(str(wrnno))
        warning_file = open(f'data/server_data/{ctx.guild.id}/warnings/{user.id}/{wrnno}.txt')
        warning_file.write(reason)
        log_channel.close()
        await ch.send(embed=Embedvar)
    except Exception as e:
        await ctx.send('Either That user hasnt opened his dms, or you havent set up the server. do `hey setup` and try '
                       'again. if '
                       'it still wont work that person is immune to me \U0001f440 ')
    await ctx.send(f"{user.mention} has been WARNED woo, reason:{reason})    https://tenor.com/zKxC.gif \n This is "
                   f"his/her {wrnno} warning")
    await user.send(f"U were were warned in {ctx.guild.name} for {reason}, behave better next time, idiot")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, n: int = 1):
    await ctx.channel.purge(limit=n + 1)


@bot.command()
@commands.has_permissions(manage_messages=True)
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
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    guild = ctx.guild
    try:
        channel = ctx.guild.system_channel
    except Exception as e:
        channel = ctx.guild.channels[0]
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
                                        "extraparam1"	BLOB,
                                        "extraparam2"	BLOB
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
        else:
            if message.content == 'n':
                await ctx.send('aight no verification system 4 this server')
            elif message.content == 'y':
                await ctx.send('okay! Making the verified role')
                mute_role2 = await ctx.guild.create_role(name=f'Verified(belongs to {bot_name})')
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
                            if channel.id == message.channel_mentions[0].id:
                                pass
                            else:

                                try:
                                    await channel.set_permissions(mute_role2, send_messages=True,
                                                                  read_messages=True)
                                    await channel.set_permissions(ctx.guild.default_role, send_messages=False,
                                                                  read_messages=False)
                                except Exception:
                                    pass
                        await message.channel_mentions[0].set_permissions(ctx.guild.default_role, read_messages=True,
                                                                          send_messages=False)
                        await ctx.send('channel perms updated, scheduling the task, this is the final step!')
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
    c.execute('SELECT * FROM config')
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
    await ctx.send('https://shrinkme.io/BerryBotInvite')


@bot.command()
async def afk(ctx, *reason):
    try:
        os.makedirs(f'data/afks/{ctx.guild.id}')
    except OSError:
        pass
    bruh = open(f'data/afks/{ctx.guild.id}/{ctx.author.id}', 'x')
    bruh.close()
    bruh = open(f'data/afks/{ctx.guild.id}/{ctx.author.id}', 'w')
    brr = ''
    for m in reason:
        brr = brr + ' ' + m
    bruh.write(brr)
    try:
        os.makedirs(f'data/afknick/{ctx.guild.id}/')
    except OSError:
        pass
    fille = open(f'data/afknick/{ctx.guild.id}/{ctx.author.id}.txt', 'x')
    fille.close()
    fille = open(f'data/afknick/{ctx.guild.id}/{ctx.author.id}.txt', 'w')
    fille.write(ctx.author.display_name)
    fille.close()
    try:
        await ctx.author.edit(nick='[AFK] ' + ctx.author.display_name)
    except discord.HTTPException:
        pass
    await ctx.send('Afk set!')
    bruh.close()


#@bot.event
#async def on_message(message):
    #if os.path.isfile(f'data/afks/{message.guild.id}/{message.author.id}'):
        #os.remove(f'data/afks/{message.guild.id}/{message.author.id}')
        #await message.channel.send(f'welcome back {message.author.mention}! I removed your afk')
        #fille = open(f'data/afknick/{message.guild.id}/{message.author.id}.txt', 'r')
        #await message.author.edit(nick=fille.read())
        #fille.close()
        #os.remove(f'data/afknick/{message.guild.id}/{message.author.id}.txt')
        #await bot.process_commands(message)
        #return
    #try:
        #var = message.mentions
    #except IndexError:
        #await bot.process_commands(message)
        #return
    #else:
        #for i in var:
            #if os.path.isfile(f'data/afks/{message.guild.id}/{i.id}'):
                #brr = open(f'data/afks/{message.guild.id}/{i.id}')
                #await message.channel.send(
                    #f'That person is afk right now {message.author.mention}. Reason: {brr.read()}')
                #await bot.process_commands(message)
                #brr.close()
                #return


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


# @bot.event
# async def on_message_delete(message):
# conn = sqlite3.connect(f'data/servers/{message.guild.id}.db')
# c = conn.cursor()
# c.execute('''INSERT INTO logs()''')

@bot.command()
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
            await ctx.guild.leave
        else:
            await ctx.send('yaay i aint leaving!')


@bot.command(aliases=['av'])
async def avatar(ctx, avamember: discord.User=None):
    if avamember is None:
        avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

token = open("token.txt")
bot.run(token.read())
