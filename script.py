import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from requests import Session
from status import func2
import base64
import json
from avatar import func5

#The necessary headers to mask the script and gain access to the site
#Bearer is the token of one's in-game account. 
session = Session()
session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0"
session.headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInVzZXJfaWQiOjI2Nzg1NTl9.eyJpc3MiOiJldmVyc2tpZXMuY29tIiwiYXVkIjoiYXV0aCIsImp0aSI6Ik45eEFyUFRxT2kwWWxBaDRHazQzVW00Y1hjdDFORVd4IiwiaWF0IjoxNjQ4MzM4OTU1Ljk4Nzg5NywibmJmIjoxNjQ4MzM4NjU1Ljk4Nzg5OSwiZXhwIjoxNjQ4NDI1MzU1fQ.IHAoAhYlxxxQ9EAiEQM2l1xs1DpxXzSU2jkDSD-89-A"

#Navigation link
render = "https://cdn.everskies.com/render/"

#Discord command bot prefix
client = commands.Bot(command_prefix="+")



@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))
  
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Everskies")) 


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("COMMAND ERROR")
  
#A command that reveals a user's online status
@client.command()
async def status(ctx, query: str):
  results = func2(session, query)["presence"]
  
  if results == 1:
    await ctx.send(f"🟢```{query} is online```")
    
  elif results == 2:
    await ctx.send(f"🌙```{query} is idle```")
    
  elif results == 0:
     await ctx.send(f"🔴```{query} is offline```")
  
@status.error
async def status_error(ctx, error):
  await ctx.send("🚫```INVALID USERNAME```")


 #A command that reveals a user's current avatar 
@client.command()
async def av(ctx, query: str):
  
  results = func5(session, query)["avatar"]
  outfit = json.dumps(results)
  outfit_bytes = outfit.encode("ascii")
  base64_bytes = base64.b64encode(outfit_bytes)
  base64_outfit = base64_bytes.decode("ascii")
  #print(stuff+base64_outfit)
  await ctx.send(render+base64_outfit)

@av.error
async def av_error(ctx, error):
  await ctx.send("🚫```INVALID USERNAME```")

#Execute the keep_alive script and the bot's token
keep_alive()
client.run(os.environ['token'])