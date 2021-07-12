#BUTTER'S SELFBOT

VERSION = "v1.4"

import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands, tasks
from colorama import Fore, Back, Style
from contextlib import redirect_stdout
from selenium import webdriver
from itertools import cycle
import typing
import emoji
import psutil
import sys

with open("Config.json") as f:
    config = json.load(f)

TOKEN = config.get("token")
prefix = config.get("prefix")

psutil.cpu_percent(interval=1)


def ready():
    print(f"""
{Fore.YELLOW}

                ╔╗ ╔═╗╔╦╗╔═╗  ╔╗ ╦ ╦╔╦╗╔╦╗╔═╗╦═╗
                ╠╩╗╚═╗ ║║║    ╠╩╗║ ║ ║  ║ ║╣ ╠╦╝
                ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝ ╩  ╩ ╚═╝╩╚═
{Fore.LIGHTBLACK_EX}
                 Bot developed by butter#0001

                    {Fore.WHITE}Discord Version {discord.__version__}

{Fore.GREEN}Erfolgreich eingeloggt als {Fore.WHITE}{Butter.user.name}{Fore.GREEN}.

{Fore.GREEN}Dein # ist {Fore.WHITE}{Butter.user.discriminator}{Fore.GREEN}.

{Fore.GREEN}Die Account ID ist {Fore.WHITE}{Butter.user.id}{Fore.GREEN}.

{Fore.GREEN}Du hast {Fore.WHITE}{len(Butter.user.friends)}{Fore.GREEN} Freunde.

{Fore.GREEN}Du bist auf {Fore.WHITE}{len(Butter.guilds)}{Fore.GREEN} Server.

{Fore.WHITE}Gebe {Fore.YELLOW}'{prefix}optionen' {Fore.WHITE}ein, um die Befehle anzuschauen.
    """ + Fore.RESET)

def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
Butter = client
Butter.remove_command('help')
Butter.launch_time = datetime.datetime.now()

@Butter.event
async def on_message_edit(before, after):
    await Butter.process_commands(after)

@Butter.event
async def on_connect():
    os.system("mode con: cols=100 lines=30")
    ctypes.windll.kernel32.SetConsoleTitleW(f"𝗕𝗨𝗧𝗧𝟯𝗥'𝗦 𝗦𝗘𝗟𝗙𝗕𝗢𝗧 | 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 {VERSION} | 𝗘𝗶𝗻𝗴𝗲𝗹𝗼𝗴𝗴𝘁 𝗮𝗹𝘀: {Butter.user.name}")
    ready()

@Butter.command()
async def laufzeit(ctx):
    await ctx.message.delete()
    delta_uptime = datetime.datetime.now() - Butter.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(color=RandomColor(), timestamp=ctx.message.created_at, description=f":fire: **{hours} Stunden {minutes} Minuten, {seconds} Sekunden** :fire: ")
    embed.set_author(name='𝐒𝐄𝐋𝐅𝐁𝐎𝐓 - 𝐋𝐀𝐔𝐙𝐄𝐈𝐓')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/746792750971748516/749363254593323078/b60608ed0a2023085eaf730250701c95_1.gif')
    embed.set_footer(text='BSDCv1.4')
    await ctx.send(embed=embed, delete_after=10)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich die Selfbot-Laufzeit reingesendet!")

@Butter.command()
async def ac(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich deinen Ascii Text reingesendet!")

@Butter.command()
async def em(ctx, *, a_sMessage):
    await ctx.message.delete()
    embed = discord.Embed(description=a_sMessage, color=RandomColor(), timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.message.author.name, icon_url = client.user.avatar_url)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich eine Embed Nachricht reingesendet!")

@Butter.command()
async def systeminfo(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await ctx.message.delete()
    await message.delete()
    cpuavg = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()[2]
    durround = round(duration, 3)
    embed = discord.Embed(
        title="System informationen", description="", color=RandomColor()
    )
    embed.set_thumbnail(url="https://i.imgur.com/GuRAHY1.png")
    embed.add_field(name="CPU", value=f"{cpuavg}%", inline=True)
    embed.add_field(name="Ram", value=f"{mem}%", inline=True)
    embed.add_field(name="Ping", value=f"{durround}ms", inline=True)
    embed.add_field(name="OS", value=f"{sys.platform}", inline=True)
    embed.set_footer(text="BSDCv1.4")
    await ctx.send(embed=embed)

@Butter.command()
async def restart(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Der {Fore.RED}SELFBOT{Fore.GREEN} wird nun gerestartet.")
    os.execv(sys.executable, ["Discord main.py"] + sys.argv)

@Butter.command()
async def gibmeme(ctx):
    await ctx.delete_message(ctx.message)
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=RandomColor(), timestamp=ctx.message.created_at)
    embed.set_author(name="Hier dein Meme", icon_url="https://cdn.discordapp.com/attachments/746792750971748516/764533886234918922/giphy.gif")
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich einen Meme reingesendet!")

@Butter.command()
async def l(ctx):
    with open("wörter.txt", "r") as file:
        allText = file.read()
    nachrichten = list(map(str, allText.split()))
    await ctx.message.delete()
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Der Level-Bot wurde erfolgreich gestartet.")
    for i in range(9999):
        await ctx.send(random.choice(nachrichten))
        print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich gesendet.")
        await asyncio.sleep(60)

@Butter.command()
async def bump(ctx):
    nachrichten = "!d bump"
    await ctx.message.delete()
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Der Bump-Prozess wurde gestartet. Es wird nun jede zweite Stunde ein Bump gesendet.")
    for i in range(9999):
        await ctx.send(nachrichten)
        print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den Server {Fore.RED}{ctx.guild.name}{Fore.GREEN} gebumped.")
        await asyncio.sleep(7200)

@Butter.command()
async def gibtoken(ctx, user: discord.User = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s Token ist " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s Token ist " + "".join(token))

@Butter.command()
async def leer(ctx):
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich einen Leeren Text reingesendet!")

@Butter.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich einen Nitro-Code reingesendet!")

@Butter.command()
async def userinfo(ctx):
  await ctx.message.delete()
  users = ctx.message.mentions
  print(f"{Fore.RED}[{datetime.datetime.now()}]\n{Fore.GREEN}Logge Userinfo von {len(users)} Usern...")
  for user in users:
    print(f"  {Fore.RED}Logge {user}...")
    f = open(f"Userinfo vom Nuttensohn - {user}.txt", 'w')
    f.write(f"""
BENUTZERNAME - {user}
USER ID               - {user.id}
ACCOUNT ERSTELLT AM - {user.created_at}
BOT?                  - {user.bot}
AVATAR URL            - {user.avatar_url}
[{datetime.datetime.now()}]
""")
    f.close()
    await ctx.send(
f"""
>>>
```
BENUTZERNAME - {user}
USER ID               - {user.id}
ACCOUNT ERSTELLT AM - {user.created_at}
BOT?                  - {user.bot}
AVATAR URL            - {user.avatar_url}
[{datetime.datetime.now()}]
```
""",
    file = discord.File(f'Userinfo vom Nuttensohn - {user}.txt')
    )
    os.remove(f'Userinfo vom Nuttensohn - {user}.txt')
    print(f"  {Fore.GREEN}Erfolgreich {Fore.WHITE}{user}{Fore.RED}'s Infos geloggt.")
    f.close()
    print(f"{Fore.GREEN}Userinfo bereitgestellt!\n")

@Butter.command()
async def cr(ctx):
    await ctx.message.delete()
    await ctx.send("Nihad Nudes: <ms-cxh-full://0>")

@Butter.command()
async def ip(ctx, host):
    await ctx.message.delete()
    start = datetime.datetime.now()
    r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
    ip = ctx
    geo = r.json()
    query = geo["query"]
    isp = geo["isp"]
    city = geo["city"]
    region = geo["regionName"]
    country = geo["country"]
    proxy = geo["proxy"]
    mobile = geo["mobile"]
    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    embed = discord.Embed(description=f"**Host-IP:** {query}\n**ISP:** {isp}\n**Stadt:** {city}\n**Region:** {region}\n**Land:** {country}\n**VPN/Proxy:** {proxy}\n**Mobil:** {mobile}", color=RandomColor())
    embed.set_author(name=f"IP-Tracker für {query}")
    embed.set_footer(text=f"Herausgefunden in {elapsed} Sekunden")
    embed.set_thumbnail(url="https://sitechecker.pro/wp-content/uploads/2019/04/ip-address.png")
    await ctx.send(embed=embed, delete_after=10)
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Die IP-Location von {Fore.RED}{query}{Fore.GREEN} wurde erfolgreich in den Chat geschickt!")

@Butter.command()
async def av(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den Avatar von {Fore.RED}{user.name}{Fore.GREEN} reingesendet!")

@Butter.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/ButterDerG",
    )
    await Butter.change_presence(activity=stream)
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Dein Status wurde erfolgreich zu {Fore.RED}{message}{Fore.GREEN} geändert!")

@Butter.command()
async def spielt(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Butter.change_presence(activity=game)
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Dein Status wurde erfolgreich zu {Fore.RED}{message}{Fore.GREEN} geändert!")

@Butter.command()
async def hoert(ctx, *, message):
    await ctx.message.delete()
    await Butter.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Dein Status wurde erfolgreich zu {Fore.RED}{message}{Fore.GREEN} geändert!")

@Butter.command()
async def schaut(ctx, *, message):
    await ctx.message.delete()
    await Butter.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Dein Status wurde erfolgreich zu {Fore.RED}{message}{Fore.GREEN} geändert!")

@Butter.command()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=RandomColor(), title='Dein Selfbot-Ping zum Server:', description=f"{client.latency * 1000:.4f} ms")
    await ctx.send(embed=embed, delete_after=5)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Dein Ping wurde in den Chat gesendet.")

@Butter.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        phone = res['phone']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.RED}Unbekannter Token"+Fore.RESET)
    embed = discord.Embed(color=RandomColor(),
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nErstellungsdatum: `{creation_date}`\nAvatar: [**Klicke hier**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Handynummer', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': '2FA?', 'value': res['mfa_enabled']},
        {'name': 'Verifiziert?', 'value': res['verified']},

    ]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=False)
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich die Tokeninfo reingesendet.")

@Butter.command()
async def crollen(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_role(name='#salzwasserkoenig8i', color=RandomColor())
            print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.RED}Es werden Rollen erstellt. . .")
        except:
            return
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle Rollen wurden erfolgreich erstellt!")

@Butter.command()
async def cchannel(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_text_channel(name='#salzwasserkoenig8i')
            print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Es werden Textkanäle erstellt. . .")
        except:
            return
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle Textkanäle wurden erfolgreich erstellt!")

@Butter.command()
async def sp(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Der Spam wurde gestartet. Gebe {Fore.RED}.stopp{Fore.GREEN} ein, um es abzubrechen")
  spammsg = ctx.message.content[len(prefix)+3:]
  while True:
    try:
      await ctx.send(spammsg)
    except discord.HTTPException:
      print(f"{Fore.RED}Spam wurde abgebrochen. {Fore.WHITE}[Unbekannter Fehler]")
      return
    except discord.Forbidden:
      print(f"{Fore.RED}Spam wurde abgebrochen. {Fore.WHITE}[Keine Rechte]")
      return

@Butter.command()
async def sb(ctx, amount: int, *, message):
    await ctx.message.delete()
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Deine Nachricht wird {Fore.RED}{amount}-mal{Fore.GREEN} gespammt.")
    delay = 0
    for _i in range(amount):
        try:
            await ctx.send(message)
            await asyncio.sleep(delay)
        except:
            pass
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Die Spam Nachricht {Fore.RED}{message}{Fore.GREEN} wurde erfolgreich {Fore.RED}{amount}-mal{Fore.GREEN} reingesendet mit einem Delay von {Fore.RED}{delay}s{Fore.GREEN} !")

@Butter.command()
async def reaktion(ctx, messageNo: typing.Optional[int] = 1, *, text):
    await ctx.message.delete()
    text = (c for c in text.lower())
    emotes = {
        "a": "🇦",
        "b": "🇧",
        "c": "🇨",
        "d": "🇩",
        "e": "🇪",
        "f": "🇫",
        "g": "🇬",
        "h": "🇭",
        "i": "🇮",
        "j": "🇯",
        "k": "🇰",
        "l": "🇱",
        "m": "🇲",
        "n": "🇳",
        "o": "🇴",
        "p": "🇵",
        "q": "🇶",
        "r": "🇷",
        "s": "🇸",
        "t": "🇹",
        "u": "🇺",
        "v": "🇻",
        "w": "🇼",
        "x": "🇽",
        "y": "🇾",
        "z": "🇿",
    }
    for i, m in enumerate(await ctx.channel.history(limit=100).flatten()):
        if messageNo == i:
            for c in text:
                await m.add_reaction(f"{emotes[c]}")
            break

@Butter.command()
async def butter(ctx):
    cnt = """```
████    ██    ██  ██████  ██████  ██████  ████
██  ██  ██    ██    ██      ██    ██      ██  ██
████    ██    ██    ██      ██    ████    ████
████    ██    ██    ██      ██    ██      ██  ██
██  ██  ██    ██    ██      ██    ██      ██  ██
████      ████      ██      ██    ██████  ██  ██

                            ████
                      ██████    ██
                ██████            ██
          ██████                    ██
        ████                  ██████████
        ██  ██          ██████        ██
        ██    ██  ██████          ░░░░██
        ██      ██            ░░░░░░░░██
        ██░░░░  ██      ░░░░░░░░██████
          ██░░░░██░░░░░░░░██████
            ██░░██░░██████
              ██████
```"""
    em = discord.Embed(color=RandomColor())
    em.description = cnt
    await ctx.send(embed=em)
    await ctx.message.delete()

@Butter.command()
async def serverpb(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.guild.name, colour=RandomColor())
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Das Server Profilbild von {Fore.RED}{ctx.guild.name}{Fore.GREEN} wurde reingesendet!")

@Butter.command()
async def re(ctx):
  await ctx.message.delete()
  spammsg = "\n".join(role.mention for role in ctx.message.guild.roles)
  while True:
    try:
      await ctx.send(
        f"""
        @everyone
        {spammsg}
        """,
        delete_after = 0
        )
    except discord.HTTPException:
      print(f"{Fore.RED}Spam wurde abgebrochen. {Fore.WHITE}[Unbekannter Fehler]")
      return
    except discord.Forbidden:
      print(f"{Fore.RED}Spam wurde abgebrochen. {Fore.WHITE}[Keine Rechte]")
      return

@Butter.command()
async def clear(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Butter.user).map(lambda m: m):
        try:
           await message.delete()
           print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Deine Nachrichten werden gelöscht. . .")
        except:
            pass
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Es wurden erfolgreich {Fore.RED}{amount}{Fore.GREEN} Nachrichten gelöscht!")

@Butter.command()
async def clearalles(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED}[{datetime.datetime.now()} UTC]{Fore.GREEN}\nLösche alle Nachrichten...")
  async for message in ctx.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle Nachrichten wurden erfolgreich gelöscht!")

@Butter.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="_𝐒𝐞𝐫𝐯𝐞𝐫 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧_", timestamp=ctx.message.created_at, colour=RandomColor())

    embed.set_thumbnail(url=ctx.guild.icon_url)

    embed.add_field(name="ID:", value=ctx.guild.id)
    embed.add_field(name="Ersteller:", value=ctx.guild.owner)
    embed.add_field(name="Region:", value=ctx.guild.region)
    embed.add_field(name="Mitglieder:", value=len(ctx.guild.members))
    embed.add_field(name="Bots:", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
    embed.add_field(name="Gebannte:", value=len(await ctx.guild.bans()),)
    embed.add_field(name="Textkanäle:", value=len(ctx.guild.text_channels))
    embed.add_field(name="Sprachkanäle:", value=len(ctx.guild.voice_channels))
    embed.add_field(name="Kategorien:", value=len(ctx.guild.categories))
    embed.add_field(name="Rollen:", value=len(ctx.guild.roles))
    embed.add_field(name="Einladungen", value=len(await ctx.guild.invites()))
    embed.set_author(name = "𝘽𝙐𝙏𝙏𝙀𝙍 - 𝘽𝙎𝘿𝘾𝙫𝟏.4", icon_url = client.user.avatar_url, url = "https://twitter.com/edoderg")
    await ctx.send(embed=embed, delete_after = 10)
    time.sleep(0.25)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich die Serverinformationen von {Fore.RED}{ctx.guild.name}{Fore.GREEN} reingesendet!")

@Butter.command()
async def bitcoinfranken(ctx):
    await ctx.message.delete()
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,CHF")
    r = r.json()
    francs = r["CHF"]
    embed = discord.Embed(description=f"```CHF{str(francs)}```", color=RandomColor())
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    embed.set_author(name="𝐁𝐢𝐭𝐜𝐨𝐢𝐧-𝐖𝐞𝐫𝐭 𝐅𝐑𝐀𝐍𝐊𝐄𝐍")
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den derzeitigen Bitcoin-Wert in {Fore.RED}Franken{Fore.GREEN} reingesendet!")

@Butter.command()
async def abannen(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason="#ᴮᵁᵀᵀᴱᴿ", delete_message_days=7)
        print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich {Fore.RED}{member.display_name}{Fore.GREEN} gebannt!")
        print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle wurden gebannt.")
      except Exception:
        pass

@Butter.command()
async def lkanal(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return
    await ctx.guild.create_text_channel(name='hi')
    await ctx.send('hi')
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle Channel wurden erfolgreich gelöscht.")

@Butter.command()
async def lrollen(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Alle Rollen wurden erfolgreich gelöscht.")
        except:
            pass

@Butter.command()
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Der Servername wurde erfolgreich zu {Fore.RED}{name}{Fore.GREEN} umbenannt.")

@Butter.command()
async def bitcoineuro(ctx):
    await ctx.message.delete()
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    r = r.json()
    euro = r["EUR"]
    embed = discord.Embed(description=f"```€{str(euro)}```", color=RandomColor())
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    embed.set_author(name="𝐁𝐢𝐭𝐜𝐨𝐢𝐧-𝐖𝐞𝐫𝐭 𝐄𝐔𝐑𝐎")
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den derzeitigen Bitcoin-Wert in {Fore.RED}Euro{Fore.GREEN} reingesendet!")

@Butter.command()
async def bitcoinusd(ctx):
    await ctx.message.delete()
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    embed.set_author(name="𝐁𝐢𝐭𝐜𝐨𝐢𝐧-𝐖𝐞𝐫𝐭 𝐔𝐒𝐃")
    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den derzeitigen Bitcoin-Wert in {Fore.RED}USD{Fore.GREEN} reingesendet!")

@Butter.command()
async def kopiere(ctx):
    await ctx.message.delete()
    await Butter.create_guild(f"{ctx.guild.name} Kopie")
    await asyncio.sleep(4)
    for g in Butter.guilds:
        if f"{ctx.guild.name} Kopie" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                farbe = role.colour
                rechte = role.permissions
                await g.create_role(name=name, permissions=rechte, colour=farbe)
            print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Erfolgreich den Server {Fore.RED}{ctx.guild.name}{Fore.GREEN} kopiert!")

@Butter.command()
async def speicherav(ctx, user: discord.Member):
    await ctx.message.delete()
    with open(f"Bilder/Avatars/Gespeichert/{user}.png", "wb") as f:
        r = requests.get(user.avatar_url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)
    print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.RED}Erfolgreich {user.name}'s Avatar gespeichert. Bilder/Avatars/Gespeichert")

@Butter.command()
async def erstenachricht(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    try:
        if channel is None:
            channel = ctx.channel
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        embed = discord.Embed(description=f"[Die Erste Nachricht in diesem Channel [Hier]:]({first_message.jump_url})\n```{first_message.content}\n\nGesendet von: {first_message.author}\n```", colour=0x800080)
        embed.set_footer(
            text=f"𝘽𝙐𝙏𝙏𝙀𝙍 - 𝘽𝙎𝘿𝘾𝙫𝟏.4", icon_url="https://cdn.discordapp.com/attachments/746792750971748516/764533886234918922/giphy.gif"
        )
        await ctx.send(embed=embed)
        print(f"{Fore.RED}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Die Erste Nacricht wurde erfolgreich gesendet.")
    except Exception as e:
        print(f"  {Fore.MAGENTA}[{Fore.WHITE}ERSTE-NACHRICHT{Fore.MAGENTA}] {Fore.WHITE}Error. {e}")

@Butter.command()
async def hacke(ctx, user: discord.User = None):
    await ctx.message.delete()
    alter = str(random.randrange(10, 25))
    Geschlecht = ["Männlich", "Weiblich", "Transenschwein", "Sonstiges", "Idiotensohn"]
    Gewicht = str(random.randrange(60, 300))
    haar_farbe = ["Schwarz", "Braun", "Blond", "Weiss", "Grau", "Rot"]
    haut_farbe = ["Weiss", "Braun", "Schwarz"]
    religion = ["Christensohn", "Muslim", "Atheist", "Hindu", "Buddhist", "Jude"]
    sexualität = ["Hetero", "Gay", "Homoshit", "Bi", "Bi-Sexuell", "Lesbe"]
    schule = ["Realschule", "Studium", "Hauptschule", "Gymnasium", "Gesamtschule",
                 "Behinderter geht auf Hurensohnschule, kein Wunder"]
    einkommen = ["Der Hundesohn verdient garnichts"]

    wohnort = [ "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    geburtsdatum = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    handynummer = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['passwort', '123', 'ichbinsounglaublichschwul', user.name + "warumbinichschwul23", user.name + "istking",
                    "king" + user.name, "ichliebeschwule", "gaynignogporn", "tierporns", "hund", "123456789", "apfele49",
                    "schwarzeschwänze", "wichse", "drachenlord", "password1", "1q2w3e4r", "ichbinsogay"]
        message = await ctx.send(f"`Hacke {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\nDaten werden gesucht...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\nLiebesleben Details werden gesucht...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\nLiebesleben Details werden gesucht...\nFinalisiere den Prozess...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```𝐄𝐫𝐟𝐨𝐥𝐠𝐫𝐞𝐢𝐜𝐡 {user} 𝐠𝐞𝐡𝐚𝐜𝐤𝐭\nName: {random.choice(name)}\nGeschlecht: {random.choice(Geschlecht)}\nAlter: {alter}\nGewicht: {Gewicht}kg\nHaarfarbe: {random.choice(haar_farbe)}\nHautfarbe: {random.choice(haut_farbe)}\nGDATUM: {geburtsdatum}\nWohnort: {random.choice(wohnort)}\nHandynummer: {handynummer}\nE-Mail: {user.name + random.choice(email)}\nPasswörter: {random.choices(password, k=3)}\nEinkommen: {random.choice(einkommen)}\nReligion: {random.choice(religion)}\nSexualität: {random.choice(sexualität)}\nSchule: {random.choice(schule)}```")
    else:
        password = ['passwort', '123', 'ichbinsounglaublichschwul', user.name + "warumbinichschwul23", user.name + "istking",
                    "king" + user.name, "ichliebeschwule", "gaynignogporn", "tierporns", "hund", "123456789", "apfele49",
                    "schwarzeschwänze", "wichse", "drachenlord", "password1", "1q2w3e4r", "ichbinsogay"]
        message = await ctx.send(f"`Hacke {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacke {user}...\nDas Datenzentrum wird gehackt...\nDaten werden gesucht...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum des Servers wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum des Servers wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\nLiebesleben Details werden gesucht...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacke {user}...\nDas Datenzentrum des Servers wird gehackt...\nDaten werden gesucht...\nSSN Informationen werden gecrackt...\nLiebesleben Details werden gesucht...\nFinalisiere den Prozess...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```𝐄𝐫𝐟𝐨𝐥𝐠𝐫𝐞𝐢𝐜𝐡 {user} 𝐠𝐞𝐡𝐚𝐜𝐤𝐭\nName: {random.choice(name)}\nGeschlecht: {random.choice(Geschlecht)}\nAlter: {alter}\nGewicht: {Gewicht}kg\nHaarfarbe: {random.choice(haar_farbe)}\nHautfarbe: {random.choice(haut_farbe)}\nGDATUM: {geburtsdatum}\nWohnort: {random.choice(wohnort)}\nHandynummer: {handynummer}\nE-Mail: {user.name + random.choice(email)}\nPasswörter: {random.choices(password, k=3)}\nEinkommen: {random.choice(einkommen)}\nReligion: {random.choice(religion)}\nSexualität: {random.choice(sexualität)}\nSchule: {random.choice(schule)}```")


@Butter.command()
async def login(ctx, usertoken):
    await ctx.message.delete()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{usertoken}")')

@Butter.command()
async def stopp(ctx):
    await ctx.message.delete()
    print(f"{Fore.LIGHTRED_EX}[{datetime.datetime.now()} UTC]\n{Fore.GREEN}Das Programm wurde erfolgreich beendet{Fore.RED}")
    await Butter.logout()

@Butter.command(aliases=['help'])
async def optionen(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
    color = discord.Colour.gold(),
    timestamp=ctx.message.created_at,
    description = f"""
**__𝗖𝗵𝗮𝘁 𝗕𝗲𝗳𝗲𝗵𝗹𝗲__**
```
{prefix}optionen, help
Zeigt diese Nachricht an.

{prefix}cr
Lässt einen Windows PC crashen sobald man draufklickt.

{prefix}systeminfo
Zeigt dir deine System Informationen an wie CPU, RAM usw.

{prefix}restart
Restartet den Selfbot. (Hilfreich bei Spam-Befehlen)

{prefix}clear [Anzahl]
Löscht deine Nachrichten im Channel.

{prefix}clearalles
Löscht den gesamten Chatverlauf von dir im Channel.

{prefix}reaktion [Text]
Macht einen Reaktionstext auf die Nachricht drüber

{prefix}servername [Name]
Ändert den Servernamen.

{prefix}login [Token]
Loggt dich über Google Chrome ein.

{prefix}stopp
Stoppt das Programm.

{prefix}laufzeit
Zeigt die Laufzeit des Selfbots an.

{prefix}bitcoineuro, bitcoinusd, bitcoinfranken
Zeigt dir den Bitcoin-Wert in Euro, Franken oder USD an.

{prefix}hacke [User]
Faket einen Hack

{prefix}stream [Titel]
Stellt dein Status auf Streamen.

{prefix}spielt [Titel]
Stellt dein Status auf Spielen.

{prefix}hoert [Titel]
Stellt dein Status auf Hören.

{prefix}schaut [Titel]
Stellt dein Status auf Schauen.

{prefix}ip [ip]
Zeigt die Location, ISP, usw. von der IP an.

{prefix}tokeninfo [Token]
Zeigt die Informationen an vom Account.

{prefix}gibtoken
Erstellt einen zufälligen Token

{prefix}kopiere
Kopiert den ganzen Server auf dem man drauf ist.

{prefix}speicherav [User]
Speichert das Avatar vom User.

{prefix}av
Zeigt das Avatar von dir/anderen an.

{prefix}userinfo [User]
Zeigt die Userinfo an.

{prefix}em [Text]
Macht dir in der Einbettung einen eigenen Text.

{prefix}ac [Text]
Schreibt dein Text in Ascii.

{prefix}gibmeme
Gibt dir ein random Meme.

{prefix}ping
Zeigt dir dein Ping an.

{prefix}leer
Sendet einen leeren Text.

```
**__𝗦𝗽𝗮𝗺 𝗕𝗲𝗳𝗲𝗵𝗹𝗲__**
```
{prefix}cchannel
Erstellt ganz viele Channels.

{prefix}crollen
Erstellt ganz viele Rollen.

{prefix}lkanal
Löscht alle Channels auf dem Server.

{prefix}lrollen
Löscht alle Rollen auf dem Server.

{prefix}sp [Text]
Spamt möglichst viele Nachrichten durchgehend.

{prefix}sb [Anzahl] [Text]
Spamt die gewünschte Nachricht in gewünschter Anzahl.

{prefix}re
Erwähnt alle Rollen.

```
**__𝐒𝐨𝐧𝐬𝐭𝐢𝐠𝐞𝐬__**
```
Bei Fehler usw. gerne butter#𝟬𝟬𝟬𝟭
adden und anschreiben!

```
    """)
  embed.set_author(name = "𝘽𝙐𝙏𝙏𝙀𝙍 - 𝘽𝙎𝘿𝘾𝙫𝟏.4", icon_url = client.user.avatar_url, url = "https://twitter.com/edoderg")
  await ctx.send(embed=embed, delete_after=30)

@Butter.command(aliases=['help2'])
async def optionen2(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
    color = discord.Colour.gold(),
    timestamp=ctx.message.created_at,
    description = f"""
**__𝗖𝗵𝗮𝘁 𝗕𝗲𝗳𝗲𝗵𝗹𝗲__**
```
{prefix}optionen2, help2
Zeigt diese Nachricht an.

Weitere Befehle Folgen...
```
**__𝗦𝗽𝗮𝗺 𝗕𝗲𝗳𝗲𝗵𝗹𝗲__**
```
{prefix}abannen
Bannt jeden einzelnen Member auf dem Discord Server
wo der Befehl ausgeführt wird.

```
**__𝐒𝐨𝐧𝐬𝐭𝐢𝐠𝐞𝐬__**
```
Bei Fehler usw. gerne butter#𝟬𝟬𝟬𝟭
adden und anschreiben!

```
    """)
  embed.set_author(name = "𝘽𝙐𝙏𝙏𝙀𝙍 - 𝘽𝙎𝘿𝘾𝙫𝟏.4", icon_url = client.user.avatar_url, url = "https://twitter.com/edoderg")
  await ctx.send(embed=embed, delete_after=30)

Butter.run(TOKEN, bot=False, reconnect=True)
