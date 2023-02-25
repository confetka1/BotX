from typing import Optional
import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())

class priglos(disnake.ui.View):

	def __init__(self):
		super().__init__(timeout=4.0)
		self.value = Optional[bool]
		


	disnake.ui.button(label="Conforim", style = disnake.ButtonStyle.red)
	async def Priglos(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
		await inter.response.send_message("Жди ссылочку пупсик")
		self.value = True
		self.stop()

	@disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.green)
	async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
		await inter.response.send_message("Хорошо я тебя понял ")
		self.value = False
		self.stop()


class LinkGAY_CLUB(disnake.ui.View):
	def __init__(self):
		super().__init__
		self.add_item(disnake.ui.Button(label="Join to us ", url = "https://wel.lenkino.adult/site/brazzers"))





@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work)!")


@bot.command(name="party")
async def as_party(ctx):
	view = priglos()
	await ctx.send("Приглашение в GAY_CLUB, согласны ли вы принять приглашение?", view=view)
	await view.wait()

	if view.value is None:
		await ctx.send("Ты просрал такой шанс попасть в GAY_CLUB....")
	elif view.value:
		await ctx.send("Отлично, держите вашу ссылку:", view.LinkGAY_CLUB)
	else:
		await ctx.send("Лох не успел ")


			
bot.run("")
	