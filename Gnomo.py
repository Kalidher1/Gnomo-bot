import discord
from discord.ext import commands,tasks
import json
import os
from random import randint
from discord.voice_client import VoiceClient
import asyncio
from time import sleep

indexLista = 0

queue = []
loop = False

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command(name='morra', help='Stops the song')
async def morra(ctx):
    await ctx.send("Morri")
    await ctx.send("https://media.tenor.com/dPAQRrb9YcoAAAAi/dead-skeleton.gif")
       
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!ajuda'))

@bot.command()
async def ajuda(ctx):
    embed=discord.Embed(title="Comandos do Gnomo", description="Temos os seguintes comandos do GNOMO BOT", color=0x6c25be)
    embed.add_field(name = "Geral", value ="⠀\n● !ajuda = Mostra os comandos do Gnomo\n", inline = True)
    embed.add_field(name = "Entretenimento", value ="⠀\n● !morra = morro\n", inline = True)          
    embed.add_field(name = "Rpg", value =
                    + "● !atributo = Rola atributos iniciais\n"
                    + "● !livros = Mostra os Livros do cenário de Higalas", inline = False)  
    embed.set_author(name="O Gnomo", icon_url="https://i.imgur.com/xR3qHfp.png")
    embed.set_footer(text="Pedido por: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@bot.command()
async def nix(ctx):
    await ctx.send("https://tenor.com/view/anya-spy-x-family-anime-spy-x-family-spy-x-family-anya-spy-family-anya-gif-25998501")
    
@bot.command()
async def goro(ctx):
    await ctx.send("https://tenor.com/view/muscular-anya-gif-26336145")
    
@bot.command()
async def sabriel(ctx):
    await ctx.send("https://tenor.com/view/anya-gif-26148058")
    
@bot.command()
async def maneki(ctx):
    await ctx.send("https://tenor.com/view/puss-in-boots-puss-in-boots-the-last-wish-eepy-puss-in-boots-tired-perrito-gif-12191803770995810762")
   
    
@bot.command()
async def atributo(ctx): 
    resultados = []
    for i in range(0, 6):
        status = []
        status.append(randint(1,6))
        status.append(randint(1,6))
        status.append(randint(1,6))
        status.append(randint(1,6))
        status.sort(reverse=True)
        resultados.append(status[0] + status[1] + status[2])
    resultados.sort(reverse = True)
    total = sum(resultados)
    embed=discord.Embed(title="Atributos gerados", description=f"Seus status serão:\nAtributo 1: **{resultados[0]}**\nAtributo 2: **{resultados[1]}**\nAtributo 3: **{resultados[2]}**\nAtributo 4: **{resultados[3]}**\nAtributo 5: **{resultados[4]}**\nAtributo 6: **{resultados[5]}**\nSeus atributos somaram: **{total}**", color=0x6c25be)
    embed.set_author(name="O Gnomo", icon_url="https://i.imgur.com/xR3qHfp.png")
    embed.set_footer(text="Pedido por: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
    if (total >= 71 and total <= 80):
        await ctx.send("Ta na média, dale")
    elif (total <= 70):
        await ctx.send("Se fudeu gostoso, bora dale dnv")
        await atributo(ctx)
    elif (total >= 81 and total <= 90):
        await ctx.send("CARALHO MLK TA FORTE")
    elif (total >= 91):
        for i in range(30):
            await ctx.send("?????????????????????????????????????????????????????????????????????")
        
@bot.command()
async def jackie(ctx):
    for i in range(8):
        await ctx.send("JACKIE PARA DE FAZER PERSONAGEM DIFICIL")
        
@bot.command()
async def livros(ctx):
    embed = discord.Embed(
        title="Livros",
        description="Confira os livros de higalas:",
        color=0x6c25be
    )

    embed.add_field(
        name="Apêndice de Higalas",
        value=(
            "**[Link para o Apêndice](https://homebrewery.naturalcrit.com/share/4nX-7kvcbaVU)**\n"
            "Um livro que reune toda a lore principal do cenário, os principais homebrews usados e todo o conteúdo novo adicionado a mesa\n"
        ),
        inline=False
    )

    embed.add_field(
        name="Sanguis Vampyricus",
        value=(
            "**[Link para o Sanguis Vampyricus](https://homebrewery.naturalcrit.com/share/jU5ZpHOPa345)**\n"
            "Um guia aos vampiros de Higalas\n"
        ),
        inline=False
    )

    embed.set_author(text="Gnomo Bot • Biblioteca", icon_url="https://i.imgur.com/xR3qHfp.png")
    embed.set_footer(text="Pedido por: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
        
