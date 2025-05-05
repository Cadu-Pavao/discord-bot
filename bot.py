import discord
from discord import app_commands
from discord.ext import commands
import os
from db import init_db, get_ranking

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await init_db()
    await bot.tree.sync()
    print(f"Bot conectado como {bot.user}")

@bot.tree.command(name="health-test", description="Verifica se o bot está funcionando.")
async def health_test(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Serviço rodando corretamente.")

@bot.tree.command(name="ranking", description="Mostra o ranking de jogadores.")
async def show_ranking(interaction: discord.Interaction):
    dados = await get_ranking()

    if not dados:
        await interaction.response.send_message("Nenhum dado encontrado no ranking.")
        return

    mensagem = "**🏆 Ranking de Jogadores**\n\n"
    for i, (nome, pontos, vitorias, derrotas) in enumerate(dados, start=1):
        mensagem += f"**#{i}** - {nome} | 🏅 {pontos} pts | ✅ {vitorias}V / ❌ {derrotas}D\n"

    await interaction.response.send_message(mensagem)

bot.run(TOKEN)
