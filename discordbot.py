
file = open("C:/Users/Ryan/Desktop/token.txt","r")
token = file.read()
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Running and waiting to not care about anything twiddle says.')
    async def on_message(self, message):
        if message.author == self.user: #Dont respond to bot's own messsages
            return
        if message.author.id == 201067686845874176: #Twiddle ID
            await message.add_reaction(	u"\U0001F1E9")#D
            await message.add_reaction(	u"\U0001F1F4")#O
            await message.add_reaction(	u"\U0001F1F3")#N
            await message.add_reaction(	u"\U0001F1F9")#T
            await message.add_reaction(	u"\U0001F1E8")#C
            await message.add_reaction(	u"\U0001F1E6")#A
            await message.add_reaction(	u"\U0001F1F7")#R
            await message.add_reaction(	u"\U0001F1EA")#E
client = MyClient()
client.run(token)
