import disnake
from disnake.ext import commands
from discord.utils import get
import youtube_dl
import os
reason = ["Пидорас","Гандон",]
bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all(), tst_guilds=[1038405592718516285])

@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work)!")

	await client.cahnge_presence(status = discord.Status.online, activity = discord.Game("Кодит в Visual Studio"))



@bot.event
async def on_member_join(member):
	role =  disnake.utils.get(member.guild.roles, id = "")
	channel = member.guild.system_channel
	embed = disnake.Embed(
		title = "Новый участник!",
		description= f"{member.name}#{member.descriminator}",
		color = 0xfffffff

	)

	await member.add_roles(role) 
	await channel.send(embed = embed)


@bot.event
async def on_message(message):
	await bot.process_commands(message)
	for msg in message.content.split():
		for reason_word in reason:
			if msg.lower() == reason_word:
				await message.delete()
				await message.channel.send(f"{message.author.mention} такие слова запрещены!")

@bot.event
async def on_command_error(ctx, error):

	print(error)
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполенения данной команды! ")
	elif isinstance(error, commands.UserInputError):

		await ctx.send(embed=disnake.Embed(
			description=f"Правильное использование команды: `{ctx.perfix}{ctx.command,name}` ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage} "
		))
		
@bot.command(usage="kick <@user> <reason=None>")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member : disnake.Member,*, reason = "Нарушение правил"): #более одного слова!
	await ctx.send(f"Модератор{ctx.author.mention} исключил пользователя {member.mention}", delete_aft= 1)
	await member.kick(reason=reason)
	await ctx.member.delete()

@bot.command(name="banned!", aliases=["ban"])
@commands.has_permissions(banned_members=True, administrator=True)
async def banned(ctx, member : disnake.Member,*, reason = "Нарушение правил"): #более одного слова!
	await ctx.send(f"Модератор{ctx.author.mention} забанил пользователя {member.mention}", delete_aft= 1)
	await member.banned(reason=reason)
	await ctx.member.delete()


async def on_member_mute(member):
	role =  disnake.utils.get(member.guild.roles, id = "")
	channel = member.guild.system_channel
	embed = disnake.Embed(
		title = "получил мут!",
		description= f"{member.name}#{member.descriminator}",
		color = 0xfffffff

bot.run("")


