from discord.ext import commands
import random
import datetime

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -----------------------------
    # COMANDOS SIMPLES
    # -----------------------------

    @commands.command()
    async def ping(self, ctx):
        """Responde con 'Pong!'"""
        await ctx.send("Pong!")

    @commands.command()
    async def hello(self, ctx):
        """Saluda al usuario que ejecuta el comando"""
        await ctx.send(f"¡Hola {ctx.author.mention}! 😄")

    @commands.command()
    async def say(self, ctx, *, mensaje):
        """Repite el mensaje que le envíes"""
        await ctx.send(mensaje)

    # -----------------------------
    # COMANDOS INTERMEDIOS
    # -----------------------------

    @commands.command()
    async def roll(self, ctx, lados: int = 6):
        """Tira un dado con la cantidad de lados que quieras (por defecto 6)"""
        resultado = random.randint(1, lados)
        await ctx.send(f"🎲 {ctx.author.mention} tiró un dado de {lados} lados y salió: {resultado}")

    @commands.command()
    async def info(self, ctx, miembro: commands.MemberConverter = None):
        """Muestra información de un miembro del servidor"""
        miembro = miembro or ctx.author
        await ctx.send(
            f"👤 Usuario: {miembro}\n"
            f"ID: {miembro.id}\n"
            f"Creado: {miembro.created_at.strftime('%Y-%m-%d')}\n"
            f"Unido al servidor: {miembro.joined_at.strftime('%Y-%m-%d')}"
        )

    @commands.command()
    async def server_time(self, ctx):
        """Muestra la fecha y hora actual del servidor"""
        ahora = datetime.datetime.now()
        await ctx.send(f"⏰ Hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

    # -----------------------------
    # COMANDOS MÁS COMPLEJOS
    # -----------------------------

    @commands.command()
    async def choose(self, ctx, *opciones):
        """Elige al azar entre varias opciones"""
        if not opciones:
            await ctx.send("Debes dar al menos una opción!")
            return
        eleccion = random.choice(opciones)
        await ctx.send(f"🎯 Elegí: {eleccion}")

    @commands.command()
    async def repeat(self, ctx, veces: int, *, mensaje):
        """Repite un mensaje varias veces"""
        if veces > 5:
            await ctx.send("⚠️ Puedes repetir como máximo 5 veces para no spamear.")
            veces = 5
        for _ in range(veces):
            await ctx.send(mensaje)

async def setup(bot):
    await bot.add_cog(General(bot))
from discord.ext import commands
import random
import datetime

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -----------------------------
    # COMANDOS SIMPLES
    # -----------------------------

    @commands.command()
    async def ping(self, ctx):
        """Responde con 'Pong!'"""
        await ctx.send("Pong!")

    @commands.command()
    async def hello(self, ctx):
        """Saluda al usuario que ejecuta el comando"""
        await ctx.send(f"¡Hola {ctx.author.mention}! 😄")

    @commands.command()
    async def say(self, ctx, *, mensaje):
        """Repite el mensaje que le envíes"""
        await ctx.send(mensaje)

    # -----------------------------
    # COMANDOS INTERMEDIOS
    # -----------------------------

    @commands.command()
    async def roll(self, ctx, lados: int = 6):
        """Tira un dado con la cantidad de lados que quieras (por defecto 6)"""
        resultado = random.randint(1, lados)
        await ctx.send(f"🎲 {ctx.author.mention} tiró un dado de {lados} lados y salió: {resultado}")

    @commands.command()
    async def info(self, ctx, miembro: commands.MemberConverter = None):
        """Muestra información de un miembro del servidor"""
        miembro = miembro or ctx.author
        await ctx.send(
            f"👤 Usuario: {miembro}\n"
            f"ID: {miembro.id}\n"
            f"Creado: {miembro.created_at.strftime('%Y-%m-%d')}\n"
            f"Unido al servidor: {miembro.joined_at.strftime('%Y-%m-%d')}"
        )

    @commands.command()
    async def server_time(self, ctx):
        """Muestra la fecha y hora actual del servidor"""
        ahora = datetime.datetime.now()
        await ctx.send(f"⏰ Hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

    # -----------------------------
    # COMANDOS MÁS COMPLEJOS
    # -----------------------------

    @commands.command()
    async def choose(self, ctx, *opciones):
        """Elige al azar entre varias opciones"""
        if not opciones:
            await ctx.send("Debes dar al menos una opción!")
            return
        eleccion = random.choice(opciones)
        await ctx.send(f"🎯 Elegí: {eleccion}")

    @commands.command()
    async def repeat(self, ctx, veces: int, *, mensaje):
        """Repite un mensaje varias veces"""
        if veces > 5:
            await ctx.send("⚠️ Puedes repetir como máximo 5 veces para no spamear.")
            veces = 5
        for _ in range(veces):
            await ctx.send(mensaje)

async def setup(bot):
    await bot.add_cog(General(bot))
