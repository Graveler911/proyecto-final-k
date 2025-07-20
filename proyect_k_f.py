import discord
from discord.ext import commands
import requests
import os
import random
# Permisos del bot
intents = discord.Intents.default()
intents.message_content = True

# Creación del bot
bot = commands.Bot(command_prefix='/', intents=intents)

#Imagen de lciama educativa
lista_cambio = ["El cambio climático se refiere a cambios significativos y duraderos ",
               "Está asociado principalmente con el aumento de gases de efecto invernadero que atrapan el calor en la atmósfera."]
lista_causas = ["Las principales causas del cambio climático son: "
          "quema de combustibles fósiles (carbón, petróleo, gas), deforestación, actividades industriales y agricultura intensiva."]
lista_consecuencias = ["Las consecuencias incluyen: aumento del nivel del mar, fenómenos meteorológicos extremos, pérdida de biodiversidad, impacto en la agricultura y salud humana."]
lista_acciones_individuales = ["Acciones que puedes tomar: reducir consumo de energía, usar transporte sostenible, reciclar, consumir productos locales y conscientes."]
lista_acciones_colectivas = ["Iniciativas colectivas: campañas de reforestación, políticas públicas para energías renovables, educación ambiental y proyectos comunitarios de reciclaje."]

@bot.command()
async def imagen_clima(ctx):
    """Envía una imagen educativa relacionada con el cambio climático."""
    imagenes=os.listdir("img")
    imagen = random.choice(imagenes)
    archivo= discord.File(f"img/{imagen}", filename=imagen)
    embed = discord.Embed(title="Imagen Educativa sobre Cambio Climático")
    embed.set_image(url=f"attachment://{imagen}")
    await ctx.send(file=archivo,embed=embed)

@bot.command()
async def info_cambio(ctx):
    """Proporciona información sobre qué es el cambio climático."""
    await ctx.send(random.choice(lista_cambio))

@bot.command()
async def causas(ctx):
    """Describe las principales causas del cambio climático."""
    await ctx.send(random.choice(lista_causas))

@bot.command()
async def consecuencias(ctx):
    """Explica las consecuencias a corto y largo plazo."""
    await ctx.send(random.choice(lista_consecuencias))

@bot.command()
async def acciones_individuales(ctx):
    """Sugiere acciones individuales para prevenir el cambio climático."""
    await ctx.send(random.choice(lista_acciones_individuales))

@bot.command()
async def acciones_colectivas(ctx):
    """Plantea iniciativas colectivas para mitigar el impacto ambiental."""
    await ctx.send(random.choice(lista_acciones_colectivas))

# Comando extra que tenías para clima actual en una ciudad (opcional)
@bot.command()
async def clima(ctx):
    await ctx.send("Escribe el nombre de la ciudad para obtener el clima actual.")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)
        city = msg.content
        api = f"https://wttr.in/{city}?format=%T+%t+%C&lang=es"
        response = requests.get(api)
        texto = response.text.strip()

        if response.status_code == 200 and texto:
            await ctx.send(f"El clima en {city} es: {texto}")
        else:
            await ctx.send("No se pudo obtener el clima. Por favor, verifica el nombre de la ciudad.")    
    except Exception as e:
        await ctx.send(f"Ocurrió un error en el proceso: {e}")


bot.run("token")
