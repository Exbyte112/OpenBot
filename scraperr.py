import imp
import googletrans
from nextcord import invite
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from bs4 import BeautifulSoup
import requests
import nextcord
from nextcord.ext import commands
from dummy import ts
import dummy
import datetime
import time
from datetime import date
import asyncio
import pyqrcode
import png
from pyqrcode import QRCode
from rowles import *
from googletrans import Translator
import wolframalpha
from wolframalpha import *

client = commands.Bot(command_prefix=["uku ", "Uku ", "!"], help_command=None, case_insensitive=True)

testingServerID = 942495664770809856

ans = ""

# ud: scrapes urban dictionary for definitions of a word
@client.command()
async def ud(ctx, *reply):
    wo = str(reply)
    ud = requests.get(f"https://api.urbandictionary.com/v0/define?term={wo}")
    definition = ud.json()["list"][0]["definition"]
    definition = str(definition)
    definition = definition.replace("[", "")
    definition = definition.replace("]", "")
    example = ud.json()["list"][0]["example"]
    example = str(example)
    example = example.replace("[", "")
    example = example.replace("]", "")
    author = ud.json()["list"][0]["author"]
    wor = ud.json()["list"][0]["word"]
    permalink = ud.json()["list"][0]["permalink"]
    tup = ud.json()["list"][0]["thumbs_up"]
    tdn = ud.json()["list"][0]["thumbs_down"]
    embedVar = nextcord.Embed(title=wor, description=f"{definition}\n`Example:`*{example}*\n`⬆️{tup} ⬇️{tdn}`", color=0x086253)
    embedVar.set_footer(text=f"Tips:\n{tips()}")
    await ctx.send(embed=embedVar)

# event: send the a timestamp of the time of the say inputed by the user
@client.command()
async def event(ctx, h, M, *reply):
    todays_date = date.today()
    ar = datetime.datetime(int(todays_date.year),int(todays_date.month),int(todays_date.day),int(h),int(M)).timestamp()
    ar = int(ar)-3600
    tme = float(ar)
    test = ""
    for i in reply:
        test += i + " "
    await ctx.send(f"{test}will start at <t:{int(tme)}:f>")

@client.command()
async def revent(ctx, h, M):
    todays_date = date.today()
    ar = datetime.datetime(int(todays_date.year),int(todays_date.month),int(todays_date.day),int(h),int(M)).timestamp()
    ar = int(ar)-3600
    tme = float(ar)
    await ctx.send(f"{int(tme)}")

# help: sends a list of commands and their usage
@client.command()
async def help(ctx):
    htext = f"[ud] + [text] to get word definitions from urban dictionary\n[src] + [text] to get results to your curious question :D\n[syn] + [word] to get synonyms\n[invite] to add uku to your server!\n[qr] to generate a qr code for the text/URL passed in"
    embedVar = nextcord.Embed(title="Command list", description=f"```py\n{htext}\n```", color=0x086253, timestamp=datetime.datetime.utcnow())
    embedVar.set_footer(text=f"Tips:\n{tips()}")
    await ctx.send(embed=embedVar)

# invite: sends an invite link to add uku to your server
@client.command()
async def invite(ctx):
    linkk = "https://github.com/Exbyte112/add-uku/tree/main"
    await ctx.send(linkk)
    #await ctx.send("If you want to add uku to your server, click the link or scan the QR code below")
    #await ctx.send (file=nextcord.File("ukuqr.png"))

# servers: sends a raw list of all servers uku is in
@client.command()
async def servers(ctx):
  servers = list((client.guilds))
  ver = ""
  coun = 1
  mcount = 0
  for i in servers:
    ver += f"{coun}) {i.name}\n"
    coun += 1
    mcount == i.member_count
  await ctx.send(f"Connected on: \n{str(ver)}\n server count = {str(coun-1)}")

# syn: gets synonyms of a word
@client.command()
async def syn(ctx, reply):
    an = str(reply)
    term = "https://www.thesaurus.com/browse/" + an
    page_to_scrape = requests.get(term)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    author = soup.find_all("a", attrs={"class":"css-1kg1yv8 eh475bn0"})
    food = []
    for word in author:
        food.append(word.text)
    print(food)
    synonym = ""
    for word in food:
        synonym += "__"+word+"__ "
    await ctx.send(an+": "+synonym)
    print(synonym)
    

# on_ready: prints a message to the console when the bot is ready
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name='Daya, Biyu, UKU!'))
print('We have logged in as {0.user}'.format(client))

@client.command()
async def qr(ctx, *reply):
    an = ""
    for i in reply:
        an+= i+" "
    ans = str(an)
    qr = pyqrcode.create(ans)
    qr.png('QR_by_ukubot.png', scale=6)
    await ctx.send(file=nextcord.File('QR_by_ukubot.png'))

# translate: translates a word from any language to english
@client.command()
async def translate(ctx, source, *reply):
    if source != "code":
        rep = ""
        for i in reply:
            rep += i + " "
        rep = str(rep)
        trans = Translator()
        await ctx.send(trans.translate(rep, src = source).text)
    else:
        rep = ""
        for i in reply:
            rep += i
        if source == "code":
            if rep == "all":
                codes = googletrans.LANGCODES
                cod = ""
                for code in zip(codes.values(),codes.keys()):
                    cod += str(code)+"\n"
                embedVar = nextcord.Embed(title="Language Codes", description=f"```py\n{cod}\n```", color=0x086253, timestamp=datetime.datetime.utcnow())
                await ctx.send(embed=embedVar)
            else:
                codes = googletrans.LANGCODES
                rep = str(rep.lower())
                await ctx.send(codes[rep])
@client.command()
async def t(ctx, *reply):
    rep = ""
    for i in reply:
        rep += i + " "
    trans = Translator()
    wor = trans.translate(rep)
    definition = wor.text
    embedVar = nextcord.Embed(title="Results", description=f"```{definition}```", color=0x086253)
    embedVar.set_footer(text=f"Translated from {googletrans.LANGUAGES[wor.src]}")
    await ctx.send(embed=embedVar)

@client.command()
async def test(ctx):
    await ctx.send("Hello " +ctx.author.name + "! "+"`sent in " + str(round(client.latency * 1000)) + "ms`")

@client.slash_command(guild_ids=[testingServerID])
async def ping(interaction: nextcord.Interaction):
    """Simple command that responds with Pong!"""
    await interaction.response.send_message("Pong!")
    



"""@client.event
async def on_message(message):
    if message.content.startswith('!tzone zones'):
        embedVar = nextcord.Embed(title="Timezones", description=f"```py\n{hlist()}\n```", color=0x086253, timestamp=datetime.datetime.utcnow())
        embedVar.add_field(name="Tips", value="Select your time zone by typing `tzone [timezone]`\ne.g. `tzone UTC` for UTC time", inline=False)
        await message.channel.send(embed=embedVar)
    elif message.content.startswith("!tzone") or message.content.startswith("tzone help"):
        await message.channel.send("use command `tzone zones` to get the list of selectable timezones")"""

@client.command()
async def tzone(ctx, msg):
    if msg == 'zones':
        embedVar = nextcord.Embed(title="Timezones", description=f"```py\n{hlist()}\n```", color=0x086253, timestamp=datetime.datetime.utcnow())
        embedVar.add_field(name="Tips", value="Select your time zone by typing `tzone [timezone]`\ne.g. `tzone UTC` for UTC time", inline=False)
        await ctx.send(embed=embedVar)
    elif msg == "help":
        await ctx.send("use command `tzone zones` to get the list of selectable timezones")
    elif msg in mzone:
        guild = ctx.guild
        await guild.create_role(name=msg, mentionable = True)
        if msg in ctx.author.roles: #checks all roles the member has
            if msg in mzone:
                await nextcord.Member.remove_roles(msg) #removes the role
        else:
            await nextcord.Member.add_roles(msg) #adds the role

# wolfram search
@client.command()
async def src(ctx, *reply):
    an = ""
    for i in reply:
        an+= i+" "
    ans = str(an)
    app_id = 'YOUR WOLFRAM TOKEN'
    client = Client(app_id)
    res = client.query(ans)
    fin = next(res.results).text
    embedVar = nextcord.Embed(title="Results", description=f"```txt\n{fin}\n```", color=0x086253)
    # embedVar.set_footer(text=f"Tips:\n{tips()}")
    embedVar.set_footer(text=f"Powered by Wolfram Alpha", icon_url="https://icon-library.com/images/wolfram-alpha-icon/wolfram-alpha-icon-17.jpg")
    await ctx.send(embed=embedVar)

# 8ball command
@client.command()
async def ball(ctx, *reply):
    an = ""
    for i in reply:
        an+= i+" "
    ans = str(an)
    await ctx.send(random.choice(ball_answers))

# udt: scrapes urban dictionary for definitions of a word then deletes after a 25 second delay
@client.command()
async def udt(ctx, *reply):
    ans = str(reply)
    term = "https://www.urbandictionary.com/define.php?term=" + ans 
    page_to_scrape = requests.get(term)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    author = soup.find_all("a", attrs={"class":"word"})

    definition = soup.find_all("div", attrs={"class":"meaning mb-4"})
    example = soup.find_all("div", attrs={"class":"example italic mb-4"})

    filed = {}
    food = ""
    
    for aut, defi, ex in zip(author, definition, example):
        co = 0
        if co ==0:
            food =(f"{aut.text}: {defi.text}\nE: *{ex.text}*")
            await ctx.send(food, delete_after=25)
            await asyncio.sleep(25)
            await ctx.message.delete() # Delete user's message
            break
        else:
            doof = "Sorry, couldn't retrieve text from Urban dictionary"
            await ctx.send(doof)
            co += 1
            break


client.run("YOUR BOT TOKEN")

