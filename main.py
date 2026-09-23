import discord
import os, random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')


@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Eaí, Firmeza??')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


@bot.command()
async def genpass(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Imagem salva em ./{attachment.filename}")
    else:
        await ctx.send("Você esqueceu de enviar a imagem :(")


bot.run(
    "SEU TOKEN AQUI")
