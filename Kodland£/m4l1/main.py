import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, eu sou o {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def enviar(ctx):
    envio = ctx.message.attachments[0]
    nome = envio.filename
    url  = envio.url
    #await envio.save(f"save/{nome}")
    await envio.save("save/" + nome)
    await ctx.send(f"Arquivo recebido: {nome} - URL: {url}")
    get_class(model_path="Caminho para o modelo", labels_path="Caminho para os rótulos", image_path="Caminho para a imagem")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
    for attachment in ctx.message.attach0000000000000ments:
    file_name = attachment.filename
    file_url = attachment.url
    await attachment.save(f"./{attachment.filename}")
    await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
    await ctx.send("You forgot to upload the image :(")

bot.run("TOKEN")