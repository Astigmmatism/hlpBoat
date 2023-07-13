import disnake
from disnake.ext import commands
import json
import datetime

class Mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		for guild in self.bot.guilds:
			for member in guild.members:
				with open("warns_db.json", "r") as f:
					data = json.load(f)
				if not str(guild.id) in data:
					with open("warns_db.json", "w") as f:
						data[str(guild.id)] = {}
					if str(member.id) in data[str(guild.id)]:
						pass
					else:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)
				else:
					if not str(member.id) in data[str(guild.id)]:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)
		print("Mod setup")

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		for guild in self.bot.guilds:
			for member in guild.members:
				with open("warns_db.json", "r") as f:
					data = json.load(f)
				if not str(guild.id) in data:
					with open("warns_db.json", "w") as f:
						data[str(guild.id)] = {}
					if str(member.id) in data[str(guild.id)]:
						pass
					else:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)
				else:
					if not str(member.id) in data[str(guild.id)]:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)

	@commands.Cog.listener()
	async def on_member_join(self, guild):	
		for guild in self.bot.guilds:
			for member in guild.members:
				with open("warns_db.json", "r") as f:
					data = json.load(f)
				if not str(guild.id) in data:
					with open("warns_db.json", "w") as f:
						data[str(guild.id)] = {}
					if str(member.id) in data[str(guild.id)]:
						pass
					else:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)
				else:
					if not str(member.id) in data[str(guild.id)]:
						with open("warns_db.json", "w") as f:
							data[str(guild.id)][str(member.id)] = {
								"warns": 0
							}
							json.dump(data, f, indent = 4)

	@commands.command(aliases = ['пред', 'п', 'предупреждение', 'w'])
	@commands.has_permissions(moderate_members = True)
	async def warn(self, ctx, member: disnake.Member = None, *, reason: str = None):
		list_first = [0, 1, 2]
		list_two = [3, 4, 5]
		list_trhee = [6]
		if member != None:
			with open("warns_db.json", "r") as f:
				data = json.load(f)
			warns = data[str(ctx.guild.id)][str(member.id)]["warns"]
			if member.id != ctx.author.id:
				if reason is None:
					reason = 'Причина не указана'
				embed = disnake.Embed(colour = 0x2F3136, description = f'Выдал участнику {member.mention} предупреждение')
				embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
				embed.add_field(name = 'По причине:', value = reason, inline = False)
				embed.add_field(name = 'Всего предупреждений:', value = f'**{warns + 1}**')
				if warns in list_first:
					with open("warns_db.json", "w") as f:
						data[str(ctx.guild.id)][str(member.id)]["warns"] += 1
						json.dump(data, f, indent = 4)
					time = datetime.datetime.now() + datetime.timedelta(hours = 2)
					await member.timeout(reason = f'Автомотическое действие за предупреждение: {reason}', until = time)
					await ctx.send(embed = embed)
				elif warns in list_two:
					with open("warns_db.json", "w") as f:
						data[str(ctx.guild.id)][str(member.id)]["warns"] += 1
						json.dump(data, f, indent = 4)
					time = datetime.datetime.now() + datetime.timedelta(hours = 6)
					await member.timeout(reason = f'Автомотическое действие за предупреждение: {reason}', until = time)
					await ctx.send(embed = embed)
				elif warns in list_trhee:
					with open("warns_db.json", "w") as f:
						data[str(ctx.guild.id)][str(member.id)]["warns"] += 1
						json.dump(data, f, indent = 4)
					await member.ban(reason = f'Автомотическое действие за предупреждение: {reason}')
					await ctx.send(embed = embed)
			else:
				await ctx.send("Вы не можете выдать себе предупреждение!")
		else:
			await ctx.send("Укажите участника, которому хотите выдать предупреждение!")

	@commands.command(aliases = ['сп', 'снятьпред', 'rw'])
	@commands.has_permissions(moderate_members = True)
	async def remove_warn(self, ctx, member: disnake.Member = None):
		if member != None:
			with open("warns_db.json", "r") as f:
				data = json.load(f)
			embed = disnake.Embed(colour = 0x2F3136, description = f'Снял участнику {member.mention} предупреждение')
			embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
			with open("warns_db.json", "w") as f:
				data[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
				json.dump(data, f, indent = 4)
			await ctx.send(embed = embed)
		else:
			await ctx.send("Укажите участника, которому хотите снять предупреждение!")

	@commands.command(aliases = ['пы', 'преды', 'ws'])
	async def warns(self, ctx, member: disnake.Member = None):
		if member is None:
			member == ctx.author
		with open("warns_db.json", "r") as f:
			data = json.load(f)
		embed = disnake.Embed(colour = 0x2F3136)
		embed.set_author(name = member, icon_url = member.avatar)
		embed.add_field(name = f'Всего предупреждений:', value = f'**{data[str(ctx.guild.id)][str(member.id)]["warns"]}**')
		await ctx.send(embed = embed)

	@commands.command(aliases = ['м', 'мут', 'm'])
	@commands.has_permissions(moderate_members = True)
	async def mute(self, ctx, member: disnake.Member = None, time: str = None, *, reason: str = None):
		if member != None:
			if time != None:
				if member.id != ctx.author.id:
					if reason is None:
						reason = 'Причина не указана'
					time = datetime.datetime.now() + datetime.timedelta(hours = int(time))
					cool_time = disnake.utils.format_dt(time, style = 'R')
					await member.timeout(reason = f'{reason}', until = time)
					embed = disnake.Embed(colour = 0x2F3136, description = f'Выдал участнику {member.mention} мут.\nМут кончиться {cool_time}.')
					embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
					await ctx.send(embed = embed)
				else:
					await ctx.send("Вы не можете выдать себе мут!")
			else:
				await ctx.send("Укажите время мута!")
		else:
			await ctx.send("Укажите участника, которому хотите выдать мут!")

	@commands.command(aliases = ['ам', 'рм', 'анмут', 'размут', 'um'])
	@commands.has_permissions(moderate_members = True)
	async def unmute(self, ctx, member: disnake.Member = None):
		if member != None:
			await member.timeout(reason = None, until = None)
			embed = disnake.Embed(colour = 0x2F3136, description = f'Снял мут участнику {member.mention}')
			embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
			await ctx.send(embed = embed)
		else:
			await ctx.send("Укажите участника, которому хотите снять мут!")

	@commands.command(aliases = ['б', 'бан', 'b'])
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: disnake.Member = None, *, reason: str = None):
		if member != None:
			if member.id != ctx.author.id:
				if reason is None:
					reason = 'Причина не указана'
				await ctx.guild.ban(member, reason = reason)
				embed = disnake.Embed(colour = 0x2F3136, description = f'Забанил участника {member.mention}')
				embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
				await ctx.send(embed = embed)
			else:
				await ctx.send("Вы не можете забанить самого себя!")
		else:
			await ctx.send("Укажите участника, которого хотите забанить!")

	@commands.command(aliases = ['аб', 'рб', 'разбан', 'анбан', 'ub'])
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, id):
		member = await self.bot.fetch_user(id)
		try:
			await ctx.guild.unban(member)
			embed = disnake.Embed(colour = 0x2F3136, description = f'Разбанил участника {member.mention}')
			embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
			await ctx.send(embed = embed)
		except:
			await ctx.send("Данный участник не в бане!")

	@commands.command(aliases = ['к', 'кик', 'k'])
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: disnake.Member = None, *, reason: str = None):
		if member != None:
			if member.id != ctx.author.id:
				if reason is None:
					reason = 'Причина не указана'
				await member.kick(reason = reason)
				embed = disnake.Embed(colour = 0x2F3136, description = f'Кикнул участника {member.mention}')
				embed.set_author(name = f'Модератор {ctx.author}', icon_url = ctx.author.avatar)
				await ctx.send(embed = embed)
			else:
				await ctx.send("Вы не можете кикнуть самого себя!")
		else:
			await ctx.send("Укажите участника, которого хотите кикнуть!")

def setup(bot):
	bot.add_cog(Mod(bot))