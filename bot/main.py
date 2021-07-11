import discord
import os
import time
import discord.ext
import json
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from replit import db
from keep_alive import keep_alive
from typing import Union
import praw
import random
import asyncio
import datetime as datetime



client = discord.Client

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

activity = discord.Activity(type=discord.ActivityType.watching, name="Uchiha Crest")

client = commands.Bot(command_prefix = '_', intents = intents, activity=activity, status=discord.Status.idle, case_insensitive=True) 


all_subs = []
all_subs1 = []

@client.command()
async def hello(ctx):
  await ctx.send("hui")

@client.event
async def on_connect():
    print("Connected as", client.user.name)

    reddit = praw.Reddit(
        client_id='gM4KuEZJcd4ChQ',
        client_secret=os.environ['redditone'],
        user_agent="linux:pl.furas.blog:v0.1 (by/furas_freeman)", check_for_async=False,
    )

    subreddit = reddit.subreddit("memes")  # await

    top = subreddit.hot(limit=500)

    for submission in top: 
      all_subs.append(submission)


    subreddit1 = reddit.subreddit("animememes")  # await

    top1 = subreddit1.hot(limit=500)

    for submission1 in top1:
        all_subs1.append(submission1)

    print("loaded memes")


def is_spawn1(message: discord.Message) -> Union[bool, None]:
    if message.embeds:
        embed: discord.Embed = message.embeds[0]
        return (embed.title
                and 'Tier: 5' in embed.title
                and embed.image)

def is_spawn2(message: discord.Message) -> Union[bool, None]:
    if message.embeds:
        embed: discord.Embed = message.embeds[0]
        return (embed.title
                and 'Tier: 6' in embed.title
                and embed.image)

@client.command(case_insensitive=True, aliases=['karutaping', 'karuta-ping'])
@has_permissions(administrator=True)
async def kping(ctx):
   value = db["ke"]

   if value != 'enable':
     db["ke"] = "enable"
     await ctx.send("Karuta ping is now enabled.")
   else: 
     db["ke"] = "disable"
     await ctx.send("Karuta ping is now disabled.")

@client.command(case_insensitive=True, aliases=['alt-detection'])
@has_permissions(administrator=True)
async def alt(ctx):
  valuealt = db["alt"]

  if valuealt != 'enable':
     db["alt"] = "enable"
     await ctx.send("Alt detection is now enabled.")
  else: 
     db["alt"] = "disable"
     await ctx.send("Alt detection is now disabled.")

@client.event
async def on_message(message):
  value = db["ke"]
  if value == 'enable':
    if message.author.id == 646937666251915264:
         if message.content.startswith("I'm dropping"):

             editin = await message.channel.send('<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `60` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `50` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `40` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `30` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `20` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='<@&822771362074198026> Karuta is dropping some cards. Be the one to grab them. Cards will expire in `10` seconds.')

             await asyncio.sleep(10)

             await editin.edit(content='*These cards were dropped. But they expired.*')

  await client.process_commands(message)
  
  if message.author.id == 646937666251915264:
         if message.content.startswith("A card from your wishlist"):
            await message.channel.send(" <@&860735989231910913>, A card from someone's wishlist is dropping.")
         
         
  

  if message.author.id == 673362753489993749 and is_spawn1(message) or is_spawn2(message):
     halloffame = client.get_channel(806574490460356638)
     nc = client.get_channel(768663378818236417)
     id = message.id
     msg = await nc.fetch_message(id)
     await halloffame.send(embed=msg.embeds[0])

  else:
        return



  await client.process_commands(message)


  

  

@client.command()
@has_permissions(manage_nicknames=True)
async def dm(ctx, member:discord.Member,* , message):

    channel = await member.create_dm()

    await channel.send(f"DM Message: {message}")

    logs = client.get_channel(856011540629028904)

    author = ctx.message.author.name
    authorid = ctx.message.author.id

    await logs.send(f"________________ \n Author: {author} \n Author ID: {authorid} \n Sent To: {member} \n Message: {message} \n ________________")

    await ctx.message.delete()


@client.command(case_insensitive=True, aliases=['t1', 'cooldown'])
async def cd(ctx):

  mention = ctx.author.mention

  color = ctx.author.color

  em = discord.Embed(description=f'{mention}, I will remind you in 1 minute and 50 seconds.', color=color)

  await ctx.send(embed=em)

  await asyncio.sleep(110)

  await ctx.send(f"{mention} Your T1 cooldown is over :)")



@client.command(case_insensitive=True, aliases=['memes'])
async def meme(ctx):
    
    #all_subs = []
    
    #async for submission in top:   # async
    #    all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    #await searching_msg.delete()  # remove message `Searching ...`
    #await ctx.message.delete()    # remove user message with `&meme`
    
    # --- display as image ---
    
    em = discord.Embed(title=name, color=0xF4F804)
    em.set_image(url=url)
    em.set_footer(text="Provided By Reddit")
    await ctx.send(embed=em)


@client.command(case_insensitive=True, aliases=['animememes', 'animeme', 'animemes'])
async def animememe(ctx):

    random_sub = random.choice(all_subs1)

    name = random_sub.title
    url = random_sub.url

    #await searching_msg.delete()  # remove message `Searching ...`
    #await ctx.message.delete()    # remove user message with `&meme`
    
    # --- display as image ---
    
    em = discord.Embed(title=name, color=0xF4F804)
    em.set_image(url=url)
    em.set_footer(text="Provided By Reddit")
    await ctx.send(embed=em)

@client.command()
@has_permissions(administrator=True)
async def em(ctx,*, emoji):

        emojii = get(ctx.message.guild.emojis, name=emoji)

        if emojii is not None:

          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Uchiha Crest')
          if webhook is None:
            webhook = await ctx.channel.create_webhook(name='Uchiha Crest')

            await webhook.send(
            str(emojii), username=ctx.author.display_name,  avatar_url=ctx.author.avatar_url)
            await ctx.message.delete()

          else:
            await webhook.send(
            str(emojii), username=ctx.author.display_name, avatar_url=ctx.author.avatar_url)
            await ctx.message.delete()

        else:
          await ctx.send(f"Could Not Find Any Emoji With The Name '{emoji}'")


@client.command()
@has_permissions(administrator=True)
async def embed(ctx, message):
    message1 , message2 = message.split("|")
    em = discord.Embed(title=f'{message1}', description=f'{message2}', color=0xF4F804)
    await ctx.send(embed=em)




@client.command(case_insensitive=True, aliases=['type'])
@has_permissions(administrator=True)
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")

@client.command(case_insensitive=True, aliases=['spot'])# We can only access activities from a guild
async def spotify(ctx, user: discord.Member = None):
    user = user or ctx.author  # default to the caller
    spot = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
    if spot is None:
        await ctx.send(f"{user.name} is not listening to Spotify right now.")
        return
    embedspotify = discord.Embed(title=f"{user.name}'s Spotify", color=user.top_role.color.value)
    embedspotify.add_field(name="Song", value=spot.title)
    embedspotify.add_field(name="Artist", value=spot.artist)
    embedspotify.add_field(name="Album", value=spot.album)
    embedspotify.set_thumbnail(url=spot.album_cover_url)
    await ctx.send(embed=embedspotify)


@client.command(name="whois", aliases=['memberinfo', 'userinfo'])
async def whois(ctx, member:discord.Member =  None):

    

    if member is None:
        member = ctx.author
        roles = [role for role in ctx.author.roles]

    else:
        roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name="User Info: ")
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="User Name:",value=member.display_name, inline=False)
    embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
    embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
    embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
    embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    role_string = ' '.join([r.mention for r in member.roles][1:])
    embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=False)
    embed.add_field(name="Top Role:", value=member.top_role, inline=False)
    embed.add_field(name="Bot?:", value=member.bot, inline=False)
    permstring = ', '.join([str(p[0]).replace("", "").title() for p in member.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=permstring, inline=False)

    await ctx.send(embed=embed)
    return


@client.command()
async def roleinfo(ctx, role:discord.Role):
      rid = role.id
      name = role.name
      color = role.color
      created = role.created_at.strftime("%A, %B %d %Y at %H:%M %p IST")
      position = role.position
      mentionable = role.mentionable
      hoist = role.hoist

      permstring = ', '.join([str(p[0]).replace("", "").title() for p in role.permissions if p[1]])
      perm = permstring.replace("_", " ")

      embed = discord.Embed(colour=color, timestamp=ctx.message.created_at)
      embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
      embed.add_field(name="Role ID:",value=rid)
      embed.add_field(name="Role Name:",value=name)
      embed.add_field(name="Role Color:",value=color)
      embed.add_field(name="Created At:",value=created)
      embed.add_field(name="Position:",value=position)
      embed.add_field(name="Hoist:",value=hoist)
      embed.add_field(name="Mentionable:",value=mentionable)
      embed.add_field(name="Permissions:",value=perm)
      await ctx.channel.send(embed=embed)



@client.event
async def on_member_join(member):
  created = member.created_at
  altchannel = client.get_channel(782295768693342239)
  welcomechannel = client.get_channel(768520269186728020)
  now = datetime.datetime.now() 
  delta = (now - created).days
  kickmsg = f"Kicked {member.name}"
  valuealt = db["alt"]
  reason = 'Suspected ALT'

  if valuealt == 'enable':

    if delta < 30:

      channel = await member.create_dm()
      em = discord.Embed(title="You've been automatically kicked.", color=0xF4F804)
      em.description="You've been automatically kicked from Uchiha Crest as your account is less than `30 days` old. This happend because ALT Detection module is currently enabled in Uchiha Crest. \n \nIf you still wish to join, DM `Anurag#8881` or `MeeT#4848` about it."
      await channel.send(embed=em)
      await member.kick(reason=reason)
      await altchannel.send(kickmsg)
      em1 = discord.Embed(title=f"{member.name} was kicked!", color=0xF4F804)
      em1.add_field(name="Reason:",value='Suspected ALT')
      await welcomechannel.send(embed=em1)

    print(created)
    print(now)
    print(delta)


@client.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, member : discord.Member, *, role : discord.Role):

  if ctx.author.top_role.position > role.position:
  

      if member is None:

        await ctx.send("Could not find the member!")
      else:

        if role in member.roles:
          await member.remove_roles(role)

          em = discord.Embed(color=0xF4F804)
          em.description = f"Changed roles for {member}, -{role}."

          await ctx.send(embed=em)

        else:

          await member.add_roles(role)

          em = discord.Embed(color=0xF4F804)
          em.description = f"Changed roles for {member}, +{role}."

          await ctx.send(embed=em)

  else:
    em=discord.Embed(description="You do not have enough permission to do that!")
    await ctx.send(embed=em)


@client.command(case_insensitive=True, aliases=['hof'])
@has_permissions(manage_nicknames=True)
async def spotlight(ctx):
  messagelol = await ctx.channel.fetch_message(ctx.message.reference.message_id) 

  jump = messagelol.jump_url

  channelname = ctx.channel.name

  channellol = client.get_channel(813069372813082634)

  attachment = messagelol.attachments[0].url # gets first attachment that user

  em = discord.Embed(title='Karuta Spotlight', color=0xF4F804,timestamp=datetime.datetime.utcnow())

  em.description = f'{messagelol.content} \n \n [Jump to cards]({jump})'

  em.set_image(url=attachment)

  em.set_footer(text=f'Uchiha Crest {channelname}')

  await channellol.send(embed=em)

  await ctx.message.add_reaction(emoji="✅")


@client.command()
@has_permissions(administrator=True)
async def searchalt(ctx, numberdays:int):

  members = ctx.guild.members

  for member in members:

    create = member.created_at

    join = member.joined_at

    idd = member.display_name

    name = member.id

    delta = (join - create).days

    if delta < numberdays:

      memberlist = []

      memberlist.append(f"{delta} days : {name} : {idd}")

      print(delta, idd, name)

      jointhem = '\n'.join(memberlist)

      await ctx.send(f'{jointhem}')


@client.command(aliases=['memberrole'])
@commands.has_permissions(administrator=True)
async def listrole(ctx, role:discord.Role):
    members = role.members

    if len(members) > 100:
        await ctx.send("Too many members to list!")

    else:

        memberlist = []

        for member in members:

            memberlist.append(f"{member.display_name}#{member.discriminator}")

            listlen = len(members)

        em = discord.Embed(title=f'Member List ({listlen})', color=0xF4F804,timestamp=datetime.datetime.utcnow())

        em.description = '\n'.join(memberlist)

        await ctx.send(embed=em)




####################################################### 
#errors#
#######################################################memberlist = []   memberlist.append(f"{member.display_name}#{member.discriminator}")

 ####    await ctx.send(embed=em)


@role.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@spotlight.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@dm.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@whois.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@embed.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@em.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@spotify.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")

@say.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@listrole.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")


@roleinfo.error
async def on_command_error(ctx, error):
  
  await ctx.channel.send(f"```\n{error}\n```")






keep_alive()  

client.run(os.environ['token']
)
