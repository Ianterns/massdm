
import discord

client = discord.Client()
print("created by council#0002")
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('put message here')
      print(f"message sent to {user.name}")
    except:
       print(f"> couldn't send a message to: {user.name} <")
       
client.run('put your token here', bot=False)


#  ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
#    dont skid this
#  ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
#   created by council#0002
#  ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
