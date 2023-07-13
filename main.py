import disnake
from disnake.ext import commands
import os
import json
from config import settings

bot = commands.Bot(command_prefix = '<', intents = disnake.Intents.all())
bot.remove_command("help")

@bot.command()
async def help(ctx, name: str = None):
	if name is None:
		embed = disnake.Embed(colour = 0x2F3136, title = 'Команды')
		embed.add_field(name = '` warns `', value = 'Количество предупреждений у участника')
		await ctx.send(embed = embed)
	elif name == 'admin':
		embed = disnake.Embed(colour = 0x2F3136, title = 'Команды модерации/администрации')
		embed.add_field(name = '` warn `', value = 'Выдать предупреждение участнику')
		embed.add_field(name = '` unwarn `', value = 'Снять предупреждение')
		embed.add_field(name = '` mute `', value = 'Выдать мут участнику')
		embed.add_field(name = '` unmute `', value = 'Снять мут')
		embed.add_field(name = '` ban `', value = 'Выдать бан участнику')
		embed.add_field(name = '` unban `', value = 'Снять бан')
		embed.add_field(name = '` kick `', value = 'Изгнать участника')
		await ctx.send(embed = embed)

@bot.event
async def on_ready():
	print("Бот работает")

@bot.event
async def on_command_error(ctx, error):
    print (error)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Недостаточно прав для выполнения команды!')
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send('Недостаточно прав для выполнения команды')
    else:
        pass

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')
	print(f'Загружен ког {extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	print(f'Выгружен ког {extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.reload_extension(f'cogs.{extension}')
	print(f'Перезагружен ког {extension}')

for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])