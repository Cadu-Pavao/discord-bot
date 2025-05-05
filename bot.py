import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # Pegaremos o token da variável de ambiente

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sincroniza os comandos slash com o Discord
    print(f"Bot conectado como {bot.user}")

@bot.tree.command(name="health-test", description="Verifica se o bot está funcionando.")
async def health_test(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Serviço rodando corretamente.")

bot.run(TOKEN)
