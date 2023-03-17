import discord, time
from discord.ext import commands

class cmd(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        message = await ctx.send(f"``{round(self.client.latency * 1000)}``**ms**")
        time.sleep(2)
        await message.delete()

    @commands.command(aliases = [f"clean"])
    async def purge(self, ctx, clearInteger: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit = clearInteger).filter(lambda m: m.author == self.client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
        msg = await ctx.send(f"**successfully purged.**")
        time.sleep(2)
        await msg.delete()

    @commands.command()
    async def stream(self, ctx, *, msg):
        await ctx.message.delete()
        await self.client.change_presence(activity = discord.Streaming(name = msg, url = f"https://twitch.tv/kankan"))

    @commands.command(aliases = [f"cls"])
    async def clear(self, ctx):
        await ctx.message.delete()
        await self.client.change_presence(activity = None)

    @commands.command(aliases = ["avatar", "pfp"])
    async def av(self, ctx, *, member: discord.Member = None):
        await ctx.message.delete()
        member = ctx.author if not member else member
        await ctx.send(f"{member.avatar_url}")
        await ctx.send(f"``{member.display_name}'s`` **avatar**")

def setup(client):
	client.add_cog(cmd(client))
