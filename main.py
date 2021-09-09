import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    Game = discord.Game("League of Legends")
    await client.change_presence(status=discord.Status.online, activity=Game)


@client.event
async def on_message(message):
    if message.content.startswith("이렐 안녕"):
        await message.channel.send("반갑습니다. 저는 이렐리아 입니다.")
    if message.content.startswith("이렐 뭐하니"):
        await message.channel.send("저는 지금 펜타킬 중입니다.")
    if message.content.startswith("!대화내용 삭제"):
        await message.channel.send("453개의 메세지를 삭제했습니다.")
    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)



access_token = os.environ['BOT_TOKEN']
client.run(access_token)
