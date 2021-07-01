import discord
import sys
import subprocess

client = discord.Client()

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
  global msg
  msg = message
  if message.author == client.user : return

  if str(message.channel) == channel and message.content.startswith("#python3"):
    try :
      run = subprocess.run(
        ["python3", "-c", message.content], capture_output=True, text=True
      ) 
      await message.channel.send(f"<@{message.author.id}> \n Output : \n{run.stdout} \n\n Error : \n {run.stderr}")
    except Exception as e:
      await message.channel.send(f"Exception Occurs : {e}")

  elif str(message.channel) == "python-interpreter" and message.content.startswith("#python2"):
    try :
      run = subprocess.run(
        ["python2", "-c", message.content], capture_output=True, text=True
      ) 
      await message.channel.send(f"<@{message.author.id}> \n Output : \n{run.stdout} \n\n Error : \n {run.stderr}")
    except Exception as e:
      await message.channel.send(f"Exception Occurs : {e}")

if __name__ == "__main__":
	channel = sys.argv[2]  # enter channel name you want to run bot
	my_secret = sys.argv[1] # enter discord bot token
	client.run(my_secret)