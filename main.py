import os
import os.path
import time
import cv2
import discord
import discord.utils
import numpy as np
import pytesseract
import requests
from discord.ext import commands
from discord.utils import get

try:
    from PIL import Image
except ImportError:
    import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
token = 'ODA1NTY5MzQzNzIyMjI1NzA1.YBcy6g.epZi7sg-P7nc1UmafyJEF4iMvzI'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=None, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Game('!help'))


@bot.event
async def on_member_join(ctx):
    nub = discord.utils.get(ctx.guild.roles, name="Nub")
    await ctx.add_roles(nub)


@bot.event
async def on_message(ctx):
    if ctx.channel.name == "verify":
        await ctx.delete()
    await bot.process_commands(ctx)

    async def give_rank_role(rank):
        if get(ctx.guild.roles, name="Master") is None:
            await ctx.guild.create_role(name="Master")
        Master = discord.utils.get(ctx.guild.roles, name="Master")
        if get(ctx.guild.roles, name="Grandmaster") is None:
            await ctx.guild.create_role(name="Grandmaster")
        Grandmaster = discord.utils.get(ctx.guild.roles, name="Grandmaster")
        if get(ctx.guild.roles, name="Hero") is None:
            await ctx.guild.create_role(name="Hero")
        Hero = discord.utils.get(ctx.guild.roles, name="Hero")
        if get(ctx.guild.roles, name="SuperHero") is None:
            await ctx.guild.create_role(name="SuperHero")
        SuperHero = discord.utils.get(ctx.guild.roles, name="SuperHero")
        if get(ctx.guild.roles, name="persona") is None:
            await ctx.guild.create_role(name="persona")
        Persona = discord.utils.get(ctx.guild.roles, name="persona")
        if get(ctx.guild.roles, name="DemiGod") is None:
            await ctx.guild.create_role(name="DemiGod")
        DemiGod = discord.utils.get(ctx.guild.roles, name="DemiGod")
        if get(ctx.guild.roles, name="Titan") is None:
            await ctx.guild.create_role(name="Titan")
        Titan = discord.utils.get(ctx.guild.roles, name="Titan")
        if get(ctx.guild.roles, name="Angelus") is None:
            await ctx.guild.create_role(name="Angelus")
        Angelus = discord.utils.get(ctx.guild.roles, name="Angelus")
        if get(ctx.guild.roles, name="Ofanim") is None:
            await ctx.guild.create_role(name="Ofanim")
        Ofanim = discord.utils.get(ctx.guild.roles, name="Ofanim")
        if get(ctx.guild.roles, name="Cherubim") is None:
            await ctx.guild.create_role(name="Cherubim")
        Cherubim = discord.utils.get(ctx.guild.roles, name="Cherubim")
        if get(ctx.guild.roles, name="Seraphim") is None:
            await ctx.guild.create_role(name="Seraphim")
        Seraphim = discord.utils.get(ctx.guild.roles, name="Seraphim")
        if get(ctx.guild.roles, name="ArchAngel") is None:
            await ctx.guild.create_role(name="ArchAngel")
        ArchAngel = discord.utils.get(ctx.guild.roles, name="ArchAngel")
        if get(ctx.guild.roles, name="Almighty") is None:
            await ctx.guild.create_role(name="Almighty")
        Almighty = discord.utils.get(ctx.guild.roles, name="Almighty")
        if ranktext.count(rank) > 0:
            user = ctx.author
            if Master in user.roles:
                await user.remove_roles(Master)
            if Grandmaster in user.roles:
                await user.remove_roles(Grandmaster)
            if Hero in user.roles:
                await user.remove_roles(Hero)
            if SuperHero in user.roles:
                await user.remove_roles(SuperHero)
            if Persona in user.roles:
                await user.remove_roles(Persona)
            if DemiGod in user.roles:
                await user.remove_roles(DemiGod)
            if Titan in user.roles:
                await user.remove_roles(Titan)
            if Angelus in user.roles:
                await user.remove_roles(Angelus)
            if Ofanim in user.roles:
                await user.remove_roles(Ofanim)
            if Cherubim in user.roles:
                await user.remove_roles(Cherubim)
            if Seraphim in user.roles:
                await user.remove_roles(Seraphim)
            if ArchAngel in user.roles:
                await user.remove_roles(ArchAngel)
            if Almighty in user.roles:
                await user.remove_roles(Almighty)
            role = discord.utils.get(ctx.guild.roles, name=rank)
            await user.add_roles(role)
            mention = user.mention
            await ctx.channel.send(f"{mention} now has the {rank} role")

    if get(ctx.guild.roles, name="Nub") is None:
        await ctx.guild.create_role(name="Nub")
    if get(ctx.guild.roles, name="member") is None:
        await ctx.guild.create_role(name="member")
    if ctx.channel.name == "verify" and ctx.content == "!verify":
        nub = discord.utils.get(ctx.guild.roles, name="Nub")
        member = discord.utils.get(ctx.guild.roles, name="member")
        if nub in ctx.author.roles:
            await ctx.author.remove_roles(nub)
        if member in ctx.author.roles:
            await ctx.author.remove_roles(member)
        await ctx.author.add_roles(member)

    if ctx.channel.name == "rank-role" and ctx.author != bot.user:
        try:
            attachment = ctx.attachments[0]
            response = requests.get(attachment.url)

            file = open("rankpic-2.png", "wb")
            file.write(response.content)
            file.close()

            img1 = cv2.imread('rankpic-2.png')
            img1[img1 == 0] = 255
            cv2.imwrite('rankpic-edited.png', img1)

            image = cv2.imread("rankpic-2.png")
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            yellow_lo = np.array([23, 120, 120])
            yellow_hi = np.array([27, 255, 255])
            mask = cv2.inRange(hsv, yellow_lo, yellow_hi)

            image[mask > 0] = (0, 0, 0)

            cv2.imwrite("rankpic-1.png", image)

            img = cv2.imread('rankpic-1.png')
            img[img != 0] = 255
            cv2.imwrite('rankpic-edited.png', img)

            ranktext = pytesseract.image_to_string(Image.open('rankpic-edited.png'), config='--psm 11')
            await give_rank_role("Master")
            await give_rank_role("Grandmaster")
            await give_rank_role("Hero")
            await give_rank_role("SuperHero")
            await give_rank_role("Persona")
            await give_rank_role("DemiGod")
            await give_rank_role("Titan")
            await give_rank_role("Angelus")
            await give_rank_role("Ofanim")
            await give_rank_role("Cherubim")
            await give_rank_role("Seraphim")
            await give_rank_role("ArchAngel")
            await give_rank_role("Almighty")
            dumb_bot_channel = discord.utils.get(ctx.guild.channels, name="bot-being-dumb")
            dumb_bot_channel_mention = dumb_bot_channel.mention
            time.sleep(10)
            await ctx.channel.purge()
            await ctx.channel.send(
                f"post a screenshot of your rank here to get a role, you must be atleast master rank."
                f" if this doesn't work then then ask for a role on {dumb_bot_channel_mention}")
        except IndexError:
            dumb_bot_channel = discord.utils.get(ctx.guild.channels, name="bot-being-dumb")
            dumb_bot_channel_mention = dumb_bot_channel.mention
            await ctx.channel.purge()
            await ctx.channel.send(
                f"post a screenshot of your rank here to get a role, you must be atleast master rank."
                f" if this doesn't work then then ask for a role on {dumb_bot_channel_mention}")


@bot.command()
async def help(ctx, arg1=None):
    if arg1 is None:
        em = discord.Embed(title="help")
        em.add_field(name="categories",
                     value="1 - wiki commands\n2 - misc. commands\nuse !help (number) to veiw a category")
        await ctx.send(embed=em)
    if arg1 == "1":
        em1 = discord.Embed()
        em1.add_field(name="wiki commands",
                      value="use !wiki (keyword) to access the wiki\nright now this only has the most common questions I get, I made it so I wouldn't have to answer these on here constantly\n\nkeywords:enhances, souls, relics, runes, turret%, turret damage, ore, relic upgrades, quests, best characters\n\nif you've got any suggestions for things to be added to this you can put it in the server suggestions channel")
        await ctx.send(embed=em1)
    if arg1 == "2":
        em2 = discord.Embed()
        em2.add_field(name="misc. commands",
                      value="!youtube - links my youtube\n!cdo_discord - links to the main cdo discord\n!github - links to this bot's github")
        await ctx.send(embed=em2)


@bot.command()
async def wiki(ctx, *, arg1):
    cwd = os.getcwd()
    argfilepath = cwd + "\\wiki-files\\" + arg1.lower() + ".txt"
    files = os.listdir(cwd + "\\wiki-files\\")
    if arg1.lower() + ".txt" in files:
        text = open(argfilepath, 'r').read()
        await ctx.send(text)


@bot.command()
async def youtube(ctx):
    await ctx.channel.send('https://www.youtube.com/channel/UCBI5BGp_tg906yt_LTT_DRw')


@bot.command()
async def cdo_discord(ctx):
    await ctx.channel.send('https://discord.gg/dUmjKAqzqx')


@bot.command()
async def github(ctx):
    await ctx.channel.send('https://github.com/UniqueName0/Unique_Bot')



bot.run(token)
