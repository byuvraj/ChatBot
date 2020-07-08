import discord
import datetime
import random
import csv

client = discord.Client()
read_reply = open("chat.csv")
data=csv.reader(read_reply)
message_array=[]
for mes in data:
    message_array.append(mes)
def replies(message):
    result = False
    print("Start")
    for mes in message_array:
        if mes[0].startswith(message.lower()):
            mes=mes[1:]
            reply=random.choice(mes)
            result=True
    if result:
        return reply
    else:
        return "This is not in my database"
@client.event
async def on_message(message):
    print(message.content)
    message.content = message.content.lower()
    nowTime = datetime.datetime.now() 
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        if str(message.author) == "misteryuvraj#2376":  # make sure to change to your user name with hash code
            await message.channel.send(f"Hello Creator {str(message.author)}!")
        else:
            await message.channel.send("Hello, I am a test bot.")
    elif message.content == 'good morning':
        if nowTime.hour < 12 and nowTime.hour >= 5:
            await message.channel.send(f"Good morning Mr.{message.author} I am bot!")
        elif nowTime.hour >= 12 and nowTime.hour <=17:
            await message.channel.send(f"LOL it's not morning you lazy {message.author}")
            await message.channel.send(f"Good afternoon its {nowTime.hour}: {nowTime.minute}o'clock now")
        else:
            await message.channel.send("I don't think this is morning")
        
    elif message.content == 'good afternoon':
        if nowTime.hour >= 12 and nowTime.hour <=17:
            await message.channel.send(f"Good afternoon Mr.{message.author} I am bot!")
        else:
            await message.channel.send(f"Its not aftrnoon for me, stil good afternoon {message.author}")
            await message.channel.send("Have good day")
    elif message.content == 'good evening':
        if nowTime.hour >= 17 and nowTime.hour <=23:
            await message.channel.send(f"Good evening Mr.{message.author} I am tired now!")
        elif nowTime.hour >= 1 and nowTime.hour <=5:
            await message.channel.send(f"Good evening go and sleep buddy its {nowTime.hour} o'colck")
            await message.channel.send("This is time to say Good Night..")
        else:
            await message.channel.send("I don't think this is evening") 
    elif message.content == 'good night':
        if nowTime.hour >= 21:
            await message.channel.send(f"Good night Mr.{message.author} Go GO GO sleep")
        else:
            await message.channel.send("Really this is not time to say good night")
    elif message.author =='Ldrago#9789':
        if replies(message.content)=='This is not in my database':
            await message.channel.send(f"Abhi please don't tease I know {message.author} is you") 
            await message.channel.send("Once I develop then you can say ehat ever you want")
        else:
            await message.channel.send(replies(message.content)) 
    else:
            await message.channel.send(replies(message.content)) 
    if message.author == client.user:
        return
    
client.run('NzI1NjIwMDU5ODAzNzQ2MzQ3.XwLUyA.fq_GEwjBJNURpzXQ7JdSa-CqTL8')