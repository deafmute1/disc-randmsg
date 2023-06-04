import random
from datetime import datetime, timedelta, timezone
from discord.ext import commands 
import discord
import os 

def run(): 
    intents = discord.Intents.default() 
    intents.message_content = True
    bot = commands.Bot(command_prefix='$', intents=intents)
    tz = timezone.utc
    token = os.environ["TOKEN"]

    @bot.command()
    async def randmsg(ctx, channel:str=None): 
        
        if channel is None: 
            channel = ctx.channel
        else: 
            for c in ctx.guild.text_channels: 
                if c == channel: channel = c 

        day_delta = (datetime.now(tz) - channel.created_at).days
        on_date = channel.created_at + timedelta(days=random.randrange(day_delta))
        one_day = timedelta(days=1)
        messages = []
        first_date = on_date
        # this is kinda bad.
        while len(messages) == 0: 
            try: 
                messages = [m async for m in ctx.channel.history(limit=100, around=on_date)]
            except: 
                #the above seems to break the library itself on some (large?) channels, so this is a workaround.
                #this is cursed bcz loop will go on for _ages_ in a very sparsely used channel, making it slower than randmsgproper. 
                #let hope that sparsely populated channels work with the above.... 
                messages = [m async for m in ctx.channel.history(
                    limit=100, 
                    after=on_date, 
                    before=on_date+(one_day*7)
                )]
            on_date = on_date + one_day if on_date < datetime.now(tz) else first_date -  one_day
            
        
        msg = random.choice(messages)
        ret = discord.Embed( 
            title="Jump To Message",
            url=msg.jump_url, 
            description=msg.content, 
            ) 
        ret.add_field(name="sent by",value=msg.author.name, inline=True)
        ret.add_field(name="sent at", value=msg.created_at, inline=True)
        await ctx.send(embed=ret)
        
    
    @bot.command()
    async def randmsgproper(ctx, channel:str=None): 
        if channel is None: 
            channel = ctx.channel
        else: 
            for c in ctx.guild.text_channels: 
                if c == channel: channel = c 
        
        messages = []
        async for msg in ctx.channel.history(limit=None):
            messages.append(msg)
            
        msg = random.choice(messages)
        ret = discord.Embed( 
            title="Jump To Message",
            url=msg.jump_url, 
            description=msg.content, 
            ) 
        ret.add_field(name="sent by",value=msg.author.name, inline=True)
        ret.add_field(name="sent at", value=msg.created_at, inline=True)
        await ctx.send(embed=ret)
        
        
    bot.run(token)

if __name__ == "__main__": 
    run()